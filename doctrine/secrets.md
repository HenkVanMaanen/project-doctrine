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
- Pre-commit hooks MUST scan for secrets locally using the same scanning tool as CI.

### Rotation

- A secret rotation policy MUST be defined with explicit rotation intervals (e.g., 90 days for API keys, annually for encryption keys).
- Secrets MUST be rotatable without downtime.
- Rotation SHOULD be automated where the secret manager supports it.
- Secrets with hardcoded fallback values (e.g., `config["SALT"] ?? "default-salt"`) MUST NOT be used — the application MUST fail at startup if a required secret is missing.

### Access

- Secrets MUST follow least-privilege access.
- Secret access MUST be auditable.

## See Also

- `security.md` — authentication, audit logging
- `12-factor.md` — config management (env vars vs. secret manager)
- `ci-cd.md` — pipeline secret management
- `infrastructure.md` — secret manager in cloud infrastructure
- `disaster-recovery.md` — secret backup and recovery

## Output Requirements

The generated security doc MUST:

- Specify the secret manager for the chosen infrastructure
- Define the rotation policy and schedule
- List all required secrets with their purpose (never values)
- Specify secret scanning tools for CI and pre-commit
