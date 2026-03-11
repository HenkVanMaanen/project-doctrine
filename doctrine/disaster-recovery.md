# Disaster Recovery

Applies to: all

## Requirements

### Backup

- All persistent data MUST have automated backups.
- Backup frequency MUST be defined per data criticality.
- Backups MUST be stored in a separate region/location from primary data.
- Backup encryption MUST be enabled.

### Automated Recovery Testing

- Automated backup restoration tests MUST run on a schedule (at minimum weekly).
- Automated tests MUST verify data integrity after restoration.
- Restoration test results MUST be logged and monitored — failures MUST trigger alerts.

### Manual Recovery Drills

- Full disaster recovery drills MUST be conducted quarterly.
- Drills MUST simulate realistic failure scenarios (database loss, region outage, full environment rebuild).
- Drill results MUST be documented with: scenario, timeline, issues encountered, remediation actions.

### Recovery Objectives

- **RTO** (Recovery Time Objective) MUST be defined per service.
- **RPO** (Recovery Point Objective) MUST be defined per data store.
- Both MUST be validated through automated testing and quarterly drills.

### Recovery Procedures

Runbooks MUST be documented for:

- Database restoration
- Service failover
- Full environment rebuild from IaC

Recovery MUST be testable in a non-production environment.

### Incident Response

- An incident response plan MUST be defined with roles and escalation paths.
- Post-incident reviews MUST be conducted and documented (blameless postmortems).

## See Also

- `database.md` — migration rollback, schema recovery
- `infrastructure.md` — IaC for environment rebuild
- `telemetry.md` — alerting on recovery test failures
- `dora.md` — mean time to recovery metric

## Output Requirements

The generated disaster recovery doc MUST:

- Define RTO and RPO per service/data store
- Include recovery runbooks
- Define backup strategy and schedule
- Define automated recovery test configuration and schedule
- Define quarterly drill process and documentation template
- Define incident response process with escalation paths
