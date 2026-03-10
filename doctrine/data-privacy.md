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
- Right to data portability ([Art. 20](https://gdpr-info.eu/art-20-gdpr/))

### Retention

- Data retention policies MUST be defined for each data category.
- Automated deletion MUST be implemented for expired data.

### Data Protection Impact Assessment

- A DPIA MUST be conducted when processing sensitive data at scale.

## Output Requirements

The generated data privacy doc MUST:

- Include a data inventory with classifications
- Include a Mermaid data flow diagram showing where PII is processed and stored
- Define retention periods per data category
- Define data subject rights implementation plan
- Assess DPIA necessity
