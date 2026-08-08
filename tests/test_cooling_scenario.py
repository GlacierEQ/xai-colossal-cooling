from __future__ import annotations

import math
import unittest

from cooling_scenario import (
    CoolingScenario,
    CoolingScenarioError,
    default_demo,
    simulate_cooling_scenario,
)


class CoolingScenarioTests(unittest.TestCase):
    def test_reference_scenario_is_deterministic_and_local_only(self) -> None:
        scenario = CoolingScenario(
            heat_load_kw=120.0,
            flow_lpm=130.0,
            inlet_temp_c=30.0,
            max_outlet_temp_c=45.0,
        )
        first = simulate_cooling_scenario(scenario)
        second = simulate_cooling_scenario(scenario)
        self.assertEqual(first, second)
        self.assertEqual(first.evidence_state, "MODELED_SCENARIO_NOT_TELEMETRY")
        self.assertEqual(first.external_actions, 0)
        self.assertEqual(first.external_queries, 0)
        self.assertGreater(first.mass_flow_kg_s, 0)
        self.assertGreater(first.delta_t_c, 0)

    def test_more_flow_reduces_modeled_temperature_rise(self) -> None:
        low = simulate_cooling_scenario(
            CoolingScenario(heat_load_kw=100.0, flow_lpm=80.0, inlet_temp_c=25.0)
        )
        high = simulate_cooling_scenario(
            CoolingScenario(heat_load_kw=100.0, flow_lpm=160.0, inlet_temp_c=25.0)
        )
        self.assertLess(high.delta_t_c, low.delta_t_c)
        self.assertLess(high.outlet_temp_c, low.outlet_temp_c)

    def test_more_heat_increases_modeled_temperature_rise(self) -> None:
        low = simulate_cooling_scenario(
            CoolingScenario(heat_load_kw=60.0, flow_lpm=100.0, inlet_temp_c=25.0)
        )
        high = simulate_cooling_scenario(
            CoolingScenario(heat_load_kw=120.0, flow_lpm=100.0, inlet_temp_c=25.0)
        )
        self.assertGreater(high.delta_t_c, low.delta_t_c)
        self.assertGreater(high.outlet_temp_c, low.outlet_temp_c)

    def test_zero_heat_load_has_zero_temperature_rise(self) -> None:
        result = simulate_cooling_scenario(
            CoolingScenario(heat_load_kw=0.0, flow_lpm=100.0, inlet_temp_c=25.0)
        )
        self.assertEqual(result.delta_t_c, 0.0)
        self.assertEqual(result.outlet_temp_c, 25.0)

    def test_limit_status_is_derived_not_actuated(self) -> None:
        result = simulate_cooling_scenario(
            CoolingScenario(
                heat_load_kw=500.0,
                flow_lpm=20.0,
                inlet_temp_c=35.0,
                max_outlet_temp_c=45.0,
            )
        )
        self.assertEqual(result.status, "MODELED_LIMIT_EXCEEDED")
        self.assertLess(result.outlet_headroom_c, 0)
        self.assertEqual(result.external_actions, 0)

    def test_invalid_inputs_fail_closed(self) -> None:
        invalid = [
            CoolingScenario(-1.0, 100.0, 25.0),
            CoolingScenario(100.0, 0.0, 25.0),
            CoolingScenario(100.0, -1.0, 25.0),
            CoolingScenario(100.0, 100.0, 45.0, max_outlet_temp_c=45.0),
            CoolingScenario(100.0, 100.0, 25.0, fluid_density_kg_l=0.0),
            CoolingScenario(100.0, 100.0, 25.0, specific_heat_j_kg_k=0.0),
            CoolingScenario(math.nan, 100.0, 25.0),
            CoolingScenario(100.0, math.inf, 25.0),
        ]
        for scenario in invalid:
            with self.subTest(scenario=scenario):
                with self.assertRaises(CoolingScenarioError):
                    simulate_cooling_scenario(scenario)

    def test_demo_has_explicit_evidence_boundary(self) -> None:
        demo = default_demo()
        self.assertEqual(
            demo["result"]["evidence_state"],
            "MODELED_SCENARIO_NOT_TELEMETRY",
        )
        self.assertEqual(demo["result"]["external_actions"], 0)
        self.assertEqual(demo["result"]["external_queries"], 0)


if __name__ == "__main__":
    unittest.main()
