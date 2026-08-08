"""Deterministic liquid-cooling scenario model.

This module models a bounded heat-load/flow-rate scenario. It does not read
facility telemetry or issue hardware, pump, chiller, network, or datacenter
control commands.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from typing import Any


class CoolingScenarioError(ValueError):
    """Raised when a modeled cooling scenario contains invalid inputs."""


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise CoolingScenarioError(f"{name} must be finite")
    return value


@dataclass(frozen=True, slots=True)
class CoolingScenario:
    """Inputs for one steady-state liquid-cooling calculation."""

    heat_load_kw: float
    flow_lpm: float
    inlet_temp_c: float
    max_outlet_temp_c: float = 45.0
    fluid_density_kg_l: float = 0.997
    specific_heat_j_kg_k: float = 4180.0

    def validated(self) -> "CoolingScenario":
        values = {
            "heat_load_kw": _finite("heat_load_kw", self.heat_load_kw),
            "flow_lpm": _finite("flow_lpm", self.flow_lpm),
            "inlet_temp_c": _finite("inlet_temp_c", self.inlet_temp_c),
            "max_outlet_temp_c": _finite(
                "max_outlet_temp_c", self.max_outlet_temp_c
            ),
            "fluid_density_kg_l": _finite(
                "fluid_density_kg_l", self.fluid_density_kg_l
            ),
            "specific_heat_j_kg_k": _finite(
                "specific_heat_j_kg_k", self.specific_heat_j_kg_k
            ),
        }
        if values["heat_load_kw"] < 0:
            raise CoolingScenarioError("heat_load_kw must be non-negative")
        if values["flow_lpm"] <= 0:
            raise CoolingScenarioError("flow_lpm must be positive")
        if values["fluid_density_kg_l"] <= 0:
            raise CoolingScenarioError("fluid_density_kg_l must be positive")
        if values["specific_heat_j_kg_k"] <= 0:
            raise CoolingScenarioError("specific_heat_j_kg_k must be positive")
        if values["max_outlet_temp_c"] <= values["inlet_temp_c"]:
            raise CoolingScenarioError(
                "max_outlet_temp_c must exceed inlet_temp_c"
            )
        return CoolingScenario(**values)


@dataclass(frozen=True, slots=True)
class CoolingScenarioResult:
    """Derived modeled values for one validated scenario."""

    mass_flow_kg_s: float
    delta_t_c: float
    outlet_temp_c: float
    outlet_headroom_c: float
    status: str
    evidence_state: str = "MODELED_SCENARIO_NOT_TELEMETRY"
    external_actions: int = 0
    external_queries: int = 0

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def simulate_cooling_scenario(
    scenario: CoolingScenario,
) -> CoolingScenarioResult:
    """Compute one deterministic steady-state liquid-cooling scenario."""

    scenario = scenario.validated()
    mass_flow_kg_s = (
        scenario.flow_lpm * scenario.fluid_density_kg_l / 60.0
    )
    heat_w = scenario.heat_load_kw * 1000.0
    delta_t_c = heat_w / (
        scenario.specific_heat_j_kg_k * mass_flow_kg_s
    )
    outlet_temp_c = scenario.inlet_temp_c + delta_t_c
    outlet_headroom_c = scenario.max_outlet_temp_c - outlet_temp_c
    status = "WITHIN_MODELED_LIMIT" if outlet_headroom_c >= 0 else "MODELED_LIMIT_EXCEEDED"

    return CoolingScenarioResult(
        mass_flow_kg_s=mass_flow_kg_s,
        delta_t_c=delta_t_c,
        outlet_temp_c=outlet_temp_c,
        outlet_headroom_c=outlet_headroom_c,
        status=status,
    )


def default_demo() -> dict[str, Any]:
    """Return a small inspectable scenario for docs and verification."""

    scenario = CoolingScenario(
        heat_load_kw=120.0,
        flow_lpm=130.0,
        inlet_temp_c=30.0,
        max_outlet_temp_c=45.0,
    )
    return {
        "inputs": asdict(scenario),
        "result": simulate_cooling_scenario(scenario).as_dict(),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(default_demo(), indent=2, sort_keys=True))
