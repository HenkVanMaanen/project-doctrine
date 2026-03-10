# 12-Factor App

Reference: https://12factor.net

Applies to: all

## Requirements

All twelve factors MUST be applied. Key decisions for this doctrine:

### III. Config

- Config MUST be stored in environment variables or a secret manager.
- Environment variables are acceptable for non-sensitive config.
- Sensitive values MUST use a secret manager. See `secrets.md`.

### VI. Processes

- Application processes MUST be stateless.
- Session state MUST be handled via JWT tokens (see `security.md`).
- Persistent data MUST be stored in backing services.

### X. Dev/Prod Parity

- Docker MUST be used to minimize environment gaps.
- All environments MUST use the same backing service types.

### XI. Logs

- Logs MUST be treated as event streams.
- See `telemetry.md` for structured logging requirements.

## Output Requirements

The generated architecture doc MUST:

- Map each of the 12 factors to the project's specific implementation
- Identify all backing services and their connection strategy
- Define the config management approach (env vars vs. secret manager per config item)
