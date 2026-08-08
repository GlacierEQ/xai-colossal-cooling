# Colossal Cooling Scenario Laboratory

A small, inspectable liquid-cooling modeling repository that preserves a larger historical cooling-research estate while exposing one bounded, deterministic public proof surface.

> **Independent portfolio project.** This repository is not affiliated with, endorsed by, employed by, or deployed at xAI. It does not claim access to xAI facilities, Colossus infrastructure, proprietary telemetry, hardware, or operational systems.

## Recruiter view

The current verified core answers a narrow engineering question:

> Given a modeled heat load, liquid flow rate, inlet temperature, and fluid properties, what steady-state temperature rise and outlet temperature does the scenario model produce?

The canonical implementation is [`cooling_scenario.py`](cooling_scenario.py). It is intentionally local and deterministic:

- validates finite and physically valid model inputs;
- converts liquid flow from L/min to kg/s;
- applies a steady-state energy-balance calculation;
- derives modeled outlet temperature and thermal headroom;
- reports whether the modeled outlet exceeds a caller-supplied limit;
- performs **zero external queries and zero external actions**.

This is useful as a compact example of turning an ambitious infrastructure concept into a testable engineering contract with explicit evidence boundaries.

## Engineering anatomy

The implemented model uses:

```text
mass_flow_kg_s = flow_lpm * fluid_density_kg_l / 60
heat_w         = heat_load_kw * 1000
delta_t_c      = heat_w / (specific_heat_j_kg_k * mass_flow_kg_s)
outlet_temp_c  = inlet_temp_c + delta_t_c
headroom_c     = max_outlet_temp_c - outlet_temp_c
```

The model is a **steady-state scenario calculation**, not CFD, controls engineering, telemetry processing, or a facility digital twin.

### Canonical public paths

| Path | Role |
|---|---|
| `cooling_scenario.py` | validated deterministic scenario model |
| `tests/test_cooling_scenario.py` | behavioral and fail-closed regression suite |
| `scripts/verify_portfolio_core.py` | receipt-producing verifier |
| `.github/workflows/cooling-model-truth.yml` | fail-closed CI truth gate |
| `HISTORICAL_SURFACES.md` | classification of preserved experimental material |

## Run it

```bash
python cooling_scenario.py
python -m unittest discover -s tests -v
python scripts/verify_portfolio_core.py
```

The verifier emits a bounded JSON scenario plus a receipt. Successful execution establishes only the local model/test contract on that source revision.

## Evidence boundary

Current public evidence state:

```text
MODEL + TEST
```

The current proof does **not** establish:

- xAI affiliation, employment, endorsement, partnership, or proprietary access;
- live Colossus or other datacenter telemetry;
- GPU-fleet, pump, valve, chiller, network, or facility control;
- production deployment or autonomous/self-healing infrastructure;
- real-time hardware integration;
- measured PUE, cost savings, availability, latency, or production-scale efficiency;
- validation at any specific GPU count, megawatt load, rack count, or facility scale;
- laboratory calibration, CFD validation, controls certification, or physical-system safety.

Numbers passed into the model are **scenario inputs**, not claims about an operating facility.

## Historical estate

The repository predates this bounded public contract and contains architecture documents, research notes, prototype integrations, dashboards, and scripts with stronger historical language. They remain preserved so unique engineering ideas are not erased.

They are explicitly non-authoritative until independently inspected and verified. See [`HISTORICAL_SURFACES.md`](HISTORICAL_SURFACES.md).

In particular, filenames containing terms such as `deployment`, `real-time`, `optimizer`, `intelligence`, `Colossus`, or `Blackwell` describe historical project intent or experiment identity; filenames are not deployment receipts.

## Failure behavior

The canonical scenario model fails closed on:

- non-finite numeric inputs;
- negative heat load;
- zero or negative flow;
- zero or negative fluid density or specific heat;
- a modeled maximum outlet temperature that does not exceed inlet temperature.

A modeled limit exceedance is reported as `MODELED_LIMIT_EXCEEDED`. It does not trigger an actuator, network call, control command, or automated remediation.

## Portfolio contract

```json
{
  "project": "GlacierEQ/xai-colossal-cooling",
  "relationship_to_xai": "independent_portfolio_project_no_affiliation_claim",
  "current_capability": "deterministic_liquid_cooling_scenario_model",
  "evidence_level": "TEST",
  "telemetry": false,
  "external_queries": 0,
  "external_actions": 0,
  "hardware_control": false,
  "deployment_claim": false,
  "historical_surfaces_authoritative": false
}
```

The design ambition remains preserved. Present-tense public claims remain constrained to what the repository can reproduce now.
