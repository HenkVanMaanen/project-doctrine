# Incident Response

## Standards

- Google SRE incident management: https://sre.google/sre-book/managing-incidents/
- Blameless postmortem culture: https://sre.google/sre-book/postmortem-culture/

Applies to: all

## Requirements

### Severity Levels

Incident severities MUST be defined with objective entry criteria and response targets:

| Severity | Definition (example baseline) | Acknowledge | Communicate |
|---|---|---|---|
| SEV1 | Full outage, data loss, or active security breach | ≤ 15 min | Every 30 min |
| SEV2 | Major degradation of a critical path; SLO fast-burn alert | ≤ 30 min | Every 60 min |
| SEV3 | Partial degradation, workaround exists | Same business day | Daily |
| SEV4 | Minor issue, no user impact | Next business day | On resolution |

- Severity definitions MUST be tied to measurable signals (SLO burn rate, error rate, availability), not gut feel.

### On-Call and Escalation

- An on-call rotation MUST be defined, with paging driven by the SLO-based alerts in `telemetry.md`.
- An escalation path MUST be documented: who is paged first, when to escalate, and to whom — including a security escalation path distinct from the reliability one.
- Every alert that can page a human MUST link to a runbook (`telemetry.md`); alerts without runbooks MUST NOT page.

### Incident Lifecycle

- The incident process MUST define the phases: detect → triage (assign severity) → mitigate → resolve → learn.
- Every SEV1/SEV2 incident MUST have a designated incident commander responsible for coordination and communications — separate from the person debugging.
- Mitigation MUST be preferred over root-cause fixing during the incident: roll back first (`ci-cd.md` automated rollback), diagnose after.
- A timeline of events, decisions, and actions MUST be recorded during the incident (chat channel or incident tool), not reconstructed afterwards.

### Security and Privacy Incidents

- Suspected personal data breaches MUST trigger the GDPR assessment flow: notification to the supervisory authority within 72 hours where required ([GDPR Art. 33](https://gdpr-info.eu/art-33-gdpr/)) — the runbook MUST include this decision step and contact points.
- Evidence (logs, audit trails) MUST be preserved before remediation actions that would destroy it.
- Compromised credentials MUST be rotated as part of containment (`secrets.md`).

### Postmortems

- Every SEV1 and SEV2 incident MUST have a blameless postmortem completed within 5 business days: timeline, impact quantification, contributing causes, and action items.
- Action items MUST be tracked in the issue tracker with owners and due dates; completion MUST be reviewed — a postmortem with unowned action items is incomplete.
- Postmortems MUST be stored in the repository or linked documentation system and MUST NOT name-and-blame individuals.

### Error Budget Policy

- An error budget policy MUST link SLOs (`telemetry.md`) to release decisions: when the error budget for a service is exhausted, feature deployments for that service MUST pause in favor of reliability work until the budget recovers.
- The policy MUST be documented and agreed before the first incident, not negotiated during one.

### Metrics and Drills

- Time to acknowledge (MTTA) and time to resolve (MTTR) MUST be tracked per incident; these feed the Failed Deployment Recovery Time metric (`dora.md`).
- Incident response MUST be exercised: the quarterly disaster recovery drills (`disaster-recovery.md`) MUST include running the incident process itself (paging, roles, comms), not only technical recovery.

## See Also

- `telemetry.md` — SLOs, burn-rate alerting, runbook-per-alert requirement
- `disaster-recovery.md` — recovery procedures and quarterly drills
- `dora.md` — failed deployment recovery time, change failure rate
- `data-privacy.md` — breach notification obligations
- `secrets.md` — credential rotation during containment
- `ci-cd.md` — automated rollback as first mitigation

## Output Requirements

The generated incident response doc MUST:

- Define severity levels with measurable entry criteria mapped to the project's SLOs
- Define the on-call rotation, escalation paths (reliability and security), and paging rules
- Include the incident lifecycle with roles (incident commander) and a Mermaid flow diagram
- Include the GDPR breach-assessment decision step with responsible contacts
- Define the postmortem template and action-item tracking process
- Define the error budget policy with explicit thresholds
