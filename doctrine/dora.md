# DORA Metrics

## Standard

- DORA (DevOps Research and Assessment) software delivery metrics: https://dora.dev/guides/dora-metrics/
- Accelerate State of DevOps Reports: https://dora.dev/research/
- SPACE framework (developer productivity): https://queue.acm.org/detail.cfm?id=3454124
- DevEx framework (developer experience): https://queue.acm.org/detail.cfm?id=3595878

Applies to: all

## Requirements

### Five Software Delivery Metrics

DORA evolved the original "four keys" into five metrics (2024–2025 reports): Mean Time to Recovery was renamed **Failed Deployment Recovery Time** and reclassified under throughput, and **Deployment Rework Rate** was added as a stability metric. All five MUST be measured and tracked.

**Throughput** — how quickly changes move through the system:

| Metric | Definition | Target |
|---|---|---|
| Deployment Frequency | How often code is deployed to production | On-demand (multiple times per day) |
| Change Lead Time | Time from commit to running in production | Less than one day |
| Failed Deployment Recovery Time | Time to recover from a deployment that requires immediate intervention | Less than one hour |

**Stability** — how reliably deployments succeed:

| Metric | Definition | Target |
|---|---|---|
| Change Failure Rate | % of deployments requiring immediate intervention (hotfix, rollback, patch) | < 5% |
| Deployment Rework Rate | % of deployments that are unplanned, made in response to a production incident | < 2% |

Research consistently shows throughput and stability are NOT a trade-off: top performers do well across all five metrics. Neither set may be sacrificed for the other.

### Measurement

- DORA metrics MUST be collected automatically from CI/CD pipelines, version control, and incident tracking.
- Metrics MUST be visualized on a dashboard accessible to the team.
- Trends MUST be tracked over time — point-in-time snapshots are insufficient.
- Metrics MUST be measured per application/service. They MUST NOT be used to compare unrelated teams or systems.
- Delivery metrics MUST NOT be used to evaluate individual performance — per the SPACE research, activity metrics used as individual targets invite gaming (Goodhart's law) and degrade the outcomes they were meant to improve.

### Targets

- Initial targets MUST be set based on the project's current maturity (see [DORA Quick Check](https://dora.dev/quickcheck/)).
- Teams MUST define a roadmap toward the targets in the tables above.
- Targets MUST be reviewed quarterly and adjusted.

### AI-Assisted Development

Findings from the 2024–2025 State of DevOps reports:

- AI is an **amplifier**, not a substitute for sound practice: it accelerates teams with strong foundations (small batches, robust testing, loosely coupled architecture) and magnifies dysfunction in teams without them. AI adoption without these foundations measurably reduces delivery stability.
- AI-assisted development tends to increase change batch size. AI-generated changes MUST comply with the same batch-size limits as human-written changes (see `git-workflow.md`).
- AI-generated code MUST pass the same review, testing, and quality gates as human-written code — no gate may be waived because a change was machine-generated.

### Developer Experience

Delivery metrics capture outcomes, not the capacity to produce them. Per the SPACE and DevEx research:

- Delivery metrics SHOULD be complemented with developer experience measures across the three DevEx dimensions: feedback loop speed, cognitive load, and flow state.
- Fast feedback loops are a doctrine-wide requirement, not just a survey topic: the CI time budgets in `ci-cd.md` and the review turnaround requirements in `git-workflow.md` exist to keep feedback loops short.

### Integration with Doctrine

- **Deployment Frequency** is driven by: trunk-based development (`git-workflow.md`), feature flags (`ci-cd.md`), zero-downtime deployments (`ci-cd.md`).
- **Change Lead Time** is driven by: commit pipeline time budget (`ci-cd.md`), short-lived branches and small batches (`git-workflow.md`), automated testing (`testing.md`).
- **Failed Deployment Recovery Time** is driven by: automated rollback (`ci-cd.md`), health checks (`infrastructure.md`), alerting (`telemetry.md`), recovery runbooks (`disaster-recovery.md`).
- **Change Failure Rate** is driven by: test coverage and mutation testing (`testing.md`), structural quality gates (`code-quality.md`), security scanning (`security.md`), contract testing (`testing.md`).
- **Deployment Rework Rate** is driven by: structural quality gates (`code-quality.md`), post-deployment smoke tests (`ci-cd.md`), observability and alerting (`telemetry.md`), small batch sizes (`git-workflow.md`).

## See Also

- `ci-cd.md` — pipeline, deployment strategy, feature flags
- `incident-response.md` — MTTA/MTTR feed the recovery time metric
- `git-workflow.md` — trunk-based development, batch size, review turnaround
- `testing.md` — coverage, mutation testing, change failure prevention
- `code-quality.md` — structural quality gates, technical debt
- `telemetry.md` — SLOs, alerting, metrics collection
- `disaster-recovery.md` — recovery procedures
- `infrastructure.md` — health checks, rollback

## Output Requirements

The generated observability doc MUST include a DORA metrics section that:

- Defines how each of the five metrics is collected from the project's CI/CD and incident tooling
- Sets initial targets based on team maturity
- Defines the dashboard specification
- Maps each metric to the doctrine practices that drive it
- States the measurement guardrails: per-service measurement, no cross-team comparison, no individual performance evaluation
