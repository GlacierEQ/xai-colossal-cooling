# Historical and Experimental Surfaces

This repository preserves earlier architecture, research, integration, and prototype material for lineage and capability recovery. Preservation is not current verification.

The canonical public proof surface is the bounded model in [`cooling_scenario.py`](cooling_scenario.py), its tests, and its verification receipt.

## Classification

| Surface | Preserved role | Current public evidence state |
|---|---|---|
| `xai-cooling-physics-core.py` | historical thermal-model prototype | `HISTORICAL_NON_AUTHORITATIVE` |
| `xai-cooling-v4-performance-optimizer.py` | historical optimization experiment | `HISTORICAL_NON_AUTHORITATIVE` |
| `xai-cooling-v4-thermal-intelligence.py` | historical thermal-intelligence experiment | `HISTORICAL_NON_AUTHORITATIVE` |
| `historical/source_snapshots/xai-cooling-dash-monitor.py.txt` | exact source snapshot of incomplete dashboard experiment formerly named `xai-cooling-dash-monitor.py` | `HISTORICAL_NON_EXECUTABLE` |
| `historical/source_snapshots/xai-colossal-cooling-genius-integration.py.txt` | exact source snapshot of malformed integration experiment formerly named `xai-colossal-cooling-genius-integration.py` | `HISTORICAL_NON_EXECUTABLE` |
| `historical/source_snapshots/e2b-notion-integration.py.txt` | exact source snapshot of malformed E2B/Notion experiment formerly under `integrations/` | `HISTORICAL_NON_EXECUTABLE` |
| remaining `integrations/` material | connector/integration experiments | `HISTORICAL_NON_AUTHORITATIVE` |
| `BLACKWELL_DEPLOYMENT_BLUEPRINT.json` | architecture/design artifact | `ARCHITECTURE_ONLY` |
| `XAI-COOLING-v4-ARCHITECTURE.md` | architecture/design artifact | `ARCHITECTURE_ONLY` |
| `COLOSSAL_MANIFESTO.md` | historical intent/positioning | `ASPIRATION_ONLY` |
| `PHYSICS_KNOWLEDGE_NEXUS.md` | research notes | `REFERENCE_ONLY` |
| `XAI-COOLING-RESEARCH-LIBRARY.md` | research index | `REFERENCE_ONLY` |

## Archival execution rule

Historical source that is syntactically malformed or contains placeholder/fabricated integration behavior is retained as source text rather than left with an executable `.py` extension. Git history preserves its original path and bytes; the source snapshots preserve the material in the current tree for intention recovery without allowing generic Python discovery/compilation to misrepresent it as supported runtime code.

Promotion of an archived surface requires a fresh implementation review, real external boundary where applicable, behavioral tests, and a new proof receipt. Renaming it back to `.py` is not promotion.

## Interpretation rule

Historical names such as "real-time," "deployment," "self-healing," "production," "Colossus," "Blackwell," or hardware-control language inside preserved files are not evidence that this repository currently controls, observes, or was deployed to any external system.

No preserved file establishes:

- xAI employment, endorsement, partnership, or infrastructure access;
- live Colossus telemetry or facility operation;
- GPU-fleet, pump, valve, chiller, network, or datacenter control;
- measured production scale, efficiency, PUE, latency, cost savings, or reliability;
- hardware validation, safety certification, or deployment readiness.

Promotion of a historical surface requires its own bounded implementation review and fresh receipt. Until then, it remains visible for genealogy and engineering context only.
