# Secrets Management

Applies to: all

## Requirements

### Storage

- Secrets MUST NEVER be committed to version control.
- `.gitignore` MUST exclude all secret files (`.env`, credentials, keys).
- A `.env.example` with dummy values MUST be provided for developer onboarding.
- Production secrets MUST be stored in a secret manager (cloud-native or HashiCorp Vault).

### Scanning

- Secret scanning MUST run in CI to prevent accidental commits.
- Pre-commit hooks SHOULD scan for secrets locally.

### Rotation

- A secret rotation policy MUST be defined.
- Secrets MUST be rotatable without downtime.
- Rotation SHOULD be automated where the secret manager supports it.

### Access

- Secrets MUST follow least-privilege access.
- Secret access MUST be auditable.

## Output Requirements

The generated security doc MUST:

- Specify the secret manager for the chosen infrastructure
- Define the rotation policy and schedule
- List all required secrets with their purpose (never values)
- Specify secret scanning tools for CI and pre-commit
