# DORA Metrics

## Standard

- DORA (DevOps Research and Assessment): https://dora.dev/guides/dora-metrics-four-keys/

Applies to: all

## Requirements

### Four Key Metrics

All four DORA metrics MUST be measured and tracked:

| Metric | Definition | Elite Target |
|---|---|---|
| Deployment Frequency | How often code is deployed to production | On-demand (multiple times per day) |
| Lead Time for Changes | Time from commit to running in production | Less than one hour |
| Change Failure Rate | % of deployments causing a failure in production | < 5% |
| Mean Time to Recovery | Time from failure detection to resolution | Less than one hour |

### Measurement

- DORA metrics MUST be collected automatically from CI/CD pipelines, version control, and incident tracking.
- Metrics MUST be visualized on a dashboard accessible to the team.
- Trends MUST be tracked over time — point-in-time snapshots are insufficient.

### Targets

- Initial targets MUST be set based on the project's current maturity (see [DORA Quick Check](https://dora.dev/quickcheck/)).
- Teams MUST define a roadmap to reach "Elite" performance level.
- Targets MUST be reviewed quarterly and adjusted.

### Integration with Doctrine

- **Deployment Frequency** is driven by: trunk-based development (`git-workflow.md`), feature flags (`ci-cd.md`), zero-downtime deployments (`ci-cd.md`).
- **Lead Time for Changes** is driven by: 10-minute pipeline budget (`ci-cd.md`), short-lived branches (`git-workflow.md`), automated testing (`testing.md`).
- **Change Failure Rate** is driven by: test coverage and mutation testing (`testing.md`), security scanning (`security.md`), contract testing (`testing.md`).
- **Mean Time to Recovery** is driven by: automated rollback (`ci-cd.md`), health checks (`infrastructure.md`), alerting (`telemetry.md`), recovery runbooks (`disaster-recovery.md`).

## See Also

- `ci-cd.md` — pipeline, deployment strategy, feature flags
- `git-workflow.md` — trunk-based development, branch lifetime
- `testing.md` — coverage, mutation testing, change failure prevention
- `telemetry.md` — SLOs, alerting, metrics collection
- `disaster-recovery.md` — MTTR, recovery procedures
- `infrastructure.md` — health checks, rollback

## Output Requirements

The generated observability doc MUST include a DORA metrics section that:

- Defines how each metric is collected from the project's CI/CD and incident tooling
- Sets initial targets based on team maturity
- Defines the dashboard specification
- Maps each metric to the doctrine practices that drive it
