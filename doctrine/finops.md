# FinOps / Cloud Cost Management

## Standard

- FinOps Framework: https://www.finops.org/framework/

Applies to: all

## Requirements

### Cost Visibility

- All cloud resources MUST have cost allocation tags.
- A mandatory tag set MUST be defined: environment, service, team/owner, project.
- Untagged resources MUST be flagged and remediated.
- Cost data MUST be visible on a shared dashboard.

### Budgets and Alerts

- Monthly budgets MUST be defined per environment.
- Budget alerts MUST be configured at 50%, 80%, and 100% thresholds.
- Alerts MUST notify the responsible team immediately.

### Cost Optimization

- Right-sizing recommendations MUST be reviewed monthly.
- Idle and unused resources MUST be identified and removed automatically where possible.
- Reserved capacity or savings plans SHOULD be evaluated for stable workloads.
- Cost per transaction/request SHOULD be tracked as a metric.

### Cost in Decision Making

- Infrastructure ADRs MUST include cost impact analysis.
- Cost MUST be considered alongside performance and reliability in architectural decisions.
- Trade-offs between cost and other requirements MUST be documented.

### Anomaly Detection

- Automated cost anomaly detection MUST be configured.
- Anomalies MUST trigger alerts with an investigation SLA.

## See Also

- `infrastructure.md` — resource provisioning, IaC
- `telemetry.md` — metrics collection for cost-per-request
- `dora.md` — deployment frequency affects infrastructure costs
- `disaster-recovery.md` — backup storage costs
- `ci-cd.md` — CI/CD runner and pipeline costs

## Output Requirements

The generated finops doc MUST:

- Define the cost allocation tagging strategy
- Define budget thresholds per environment
- Define the cost review cadence and process
- Specify cost monitoring and alerting tools for the chosen cloud provider
- Include cost considerations in the ADR template
