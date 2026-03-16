# 12-Factor App

Reference: https://12factor.net

Applies to: all

## Requirements

All twelve factors MUST be applied. Key decisions for this doctrine:

### III. Config

- Config MUST be stored in environment variables or a secret manager.
- Environment variables are acceptable for non-sensitive config.
- Sensitive values MUST use a secret manager. See `secrets.md`.
- All required config MUST be validated at application startup — the application MUST fail fast with a clear error if required config is missing, malformed, or out of expected range. Use the stack's idiomatic validation (e.g., Zod for TypeScript, validator for Go, Pydantic for Python, FluentValidation for C#).

### VI. Processes

- Application processes MUST be stateless.
- Session state MUST be handled externally — via JWT tokens for APIs or server-side sessions stored in a backing service (Redis/DB) for webapps with SSR (see `security.md`).
- Persistent data MUST be stored in backing services.

### X. Dev/Prod Parity

- Docker MUST be used to minimize environment gaps. See `infrastructure.md`.
- All environments MUST use the same backing service types.

### XI. Logs

- Logs MUST be treated as event streams.
- See `telemetry.md` for structured logging requirements.

## See Also

- `architecture.md` — vertical slices, CQRS, dependency rule
- `secrets.md` — secret manager selection and rotation
- `security.md` — JWT and authentication
- `telemetry.md` — structured logging
- `infrastructure.md` — Docker and environment parity

## Output Requirements

The generated architecture doc MUST:

- Map each of the 12 factors to the project's specific implementation
- Identify all backing services and their connection strategy
- Define the config management approach (env vars vs. secret manager per config item)
- Define config validation rules and startup behavior
