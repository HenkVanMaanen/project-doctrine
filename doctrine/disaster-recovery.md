# Disaster Recovery

Applies to: all

## Requirements

### Backup

- All persistent data MUST have automated backups.
- Backup frequency MUST be defined per data criticality.
- Backups MUST be stored in a separate region/location from primary data.
- Backup encryption MUST be enabled.
- Backup restoration MUST be tested regularly.

### Recovery Objectives

- **RTO** (Recovery Time Objective) MUST be defined per service.
- **RPO** (Recovery Point Objective) MUST be defined per data store.
- Both MUST be validated through regular recovery drills.

### Recovery Procedures

Runbooks MUST be documented for:

- Database restoration
- Service failover
- Full environment rebuild from IaC

Recovery MUST be testable in a non-production environment.

### Incident Response

- An incident response plan MUST be defined with roles and escalation paths.
- Post-incident reviews MUST be conducted and documented (blameless postmortems).

## Output Requirements

The generated disaster recovery doc MUST:

- Define RTO and RPO per service/data store
- Include recovery runbooks
- Define backup strategy and schedule
- Define incident response process with escalation paths
