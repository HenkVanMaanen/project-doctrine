# Data Privacy

## Standard

- GDPR: https://gdpr-info.eu/

Applies to: all

## Requirements

### Data Classification

All data MUST be classified into:

| Level | Description | Examples |
|---|---|---|
| Public | No restrictions | Marketing content, public API docs |
| Internal | Not for public consumption | Internal metrics, audit logs |
| Sensitive | PII, financial, health data | Names, emails, payment info |
| Restricted | Credentials, encryption keys | API keys, passwords, private keys |

### Data Processing

- A lawful basis ([Art. 6](https://gdpr-info.eu/art-6-gdpr/)) MUST be identified for each data processing activity.
- Data minimization MUST be applied — collect only what is necessary.
- Purpose limitation MUST be enforced — use data only for stated purposes.

### Data Subject Rights

The system MUST support:

- Right of access ([Art. 15](https://gdpr-info.eu/art-15-gdpr/))
- Right to rectification ([Art. 16](https://gdpr-info.eu/art-16-gdpr/))
- Right to erasure ([Art. 17](https://gdpr-info.eu/art-17-gdpr/))
- Right to data portability ([Art. 20](https://gdpr-info.eu/art-20-gdpr/)) — export all user data as JSON or CSV

### Erasure and Audit Trail Reconciliation

- When erasure is requested, PII MUST be hard-deleted (physical deletion).
- Audit log entries referencing the deleted user MUST be anonymized or pseudonymized — never deleted entirely.
- Audit log pseudonymization MUST use `sha256(email + AUDIT_SALT)` — never store plaintext email in audit logs.
- The erasure process MUST be documented in an ADR specifying the implementation per data type.
- Anonymization MUST be irreversible — pseudonymized IDs MUST NOT be mappable back to the original user after erasure.

### Retention

- Data retention policies MUST be defined for each data category.
- Automated deletion MUST be implemented for expired data.
- IP addresses MUST be hashed before storage. An automated cleanup job (cron, scheduled task, or background worker) MUST purge IP hashes and click/analytics data older than the retention period.

### Multi-Tenancy

If the project is multi-tenant:

- Tenant data isolation MUST be enforced at the data layer (e.g., row-level security, schema-per-tenant, or database-per-tenant). For RLS: `SET LOCAL app.current_tenant_id` (or equivalent) MUST be called at the start of every request — not just WHERE clause filtering.
- Tenant context MUST be propagated through all layers of the application.
- Cross-tenant data access MUST be impossible by default — any exception requires an ADR.
- Tenant isolation MUST be verified through automated tests.

### Data Protection Impact Assessment

- A DPIA MUST be conducted when processing sensitive data at scale.

## See Also

- `security.md` — audit logging, authentication
- `database.md` — migrations, schema management
- `disaster-recovery.md` — backup and data recovery
- `secrets.md` — restricted data (credentials, keys)
- `telemetry.md` — PII exclusion from logs

## Output Requirements

The generated data privacy doc MUST:

- Include a data inventory with classifications
- Include a Mermaid data flow diagram showing where PII is processed and stored
- Define retention periods per data category
- Define data subject rights implementation plan
- Define the erasure strategy (hard delete PII, anonymize audit records)
- Define multi-tenancy isolation strategy (if applicable)
- Assess DPIA necessity
