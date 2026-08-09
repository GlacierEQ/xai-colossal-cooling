# Legacy Orchestrator PR #1 — Value Preservation Map

This document preserves the useful engineering ideas from `feature/orchestrator-v2-integration` without promoting that branch's production, affiliation, performance, hardware-control, or external-integration claims.

**Legacy PR:** `#1`  
**Legacy head:** `607586549f07246adc19fea61d5ee3f29c274216`  
**Canonical truth-hardened base:** `0d4aeff8d127eb8842a659fab57343612dc45297`

## Decision

Do **not** merge the legacy branch into canonical `main`.

Its nine unique files divide into two groups:

- **Six capability-donor candidates:** bounded local mechanisms worth reusing under fresh tests and nonclaims.
- **Three historical/aspirational documents:** useful as design history or operator-document patterns, but not evidence of deployment or measured performance.

## Capability donors

| Legacy file | Preserved mechanism | What is explicitly not inherited |
|---|---|---|
| `orchestrator/mastermind_orchestrator.py` | Async staged decision orchestration, dependency injection, confidence aggregation, decision record | Production readiness, hardware operation, agent/model performance, live Aspen/XAI integration |
| `orchestrator/aspen_grove_bridge.py` | Bounded local cache, stable pointer naming, summary records, filtered query | Actual Aspen Grove sync, Notion write, federation, 99.4% token savings |
| `orchestrator/shadow_agent.py` | Weighted heuristic forecast composition, agreement confidence, anomaly rules | Actual LSTM/Prophet/GB models, 93.2% accuracy, 1.69°C RMSE |
| `orchestrator/microwave_agent.py` | Stateful PID-like proposal, anti-windup, feed-forward, bounded output, gain-adaptation heuristic | Physical actuation, 0.71ms p99, 94% quality, 14.6% PUE improvement |
| `orchestrator/cost_mastermind_agent.py` | Scenario PUE/cost arithmetic, time-of-day rate model, thermal-margin weighting | Measured PUE improvement, measured savings, industry comparison |
| `orchestrator/xai_colossal_interface.py` | Constraint validation, clamping, execution-record schema, executor-adapter boundary | Real hardware execution or monitoring; the legacy implementation simulates success and returned state |

## Historical-only surfaces

| Legacy file | Classification | Preserved value |
|---|---|---|
| `docs/ARCHITECTURE.md` | `HISTORICAL_NON_AUTHORITATIVE` | Multi-stage architecture visualization and responsibility decomposition |
| `docs/DEPLOYMENT.md` | `ASPIRATION_ONLY` | Future prerequisite/checklist structure |
| `docs/QUICK_START.md` | `HISTORICAL_NON_AUTHORITATIVE` | Quick-start information architecture |

## Extraction rule

A donor mechanism may enter a canonical system only after it is:

1. separated from company-specific or production-status language;
2. reduced to its actual local behavior;
3. given repository-native tests;
4. bound to an exact source revision/receipt;
5. assigned explicit nonclaims for external integration, deployment, and measured performance.

The legacy branch remains available in Git history after PR retirement. Closing the PR therefore removes a stale promotion candidate without erasing the unique engineering record.

Machine-readable classification: [`manifests/legacy_orchestrator_pr1_value_map.json`](manifests/legacy_orchestrator_pr1_value_map.json).
