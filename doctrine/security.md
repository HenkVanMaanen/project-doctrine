# Security

## Standards

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- GraphQL Security: https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html

Fetch the latest versions when generating project docs.

Applies to: all

## Requirements

### Authentication & Authorization

- OAuth 2.0 ([RFC 6749](https://www.rfc-editor.org/rfc/rfc6749)) and OpenID Connect ([spec](https://openid.net/specs/openid-connect-core-1_0.html)) MUST be used.
- JWTs ([RFC 7519](https://www.rfc-editor.org/rfc/rfc7519)) MUST be used for stateless session tokens.
- Token lifetimes MUST be short-lived with refresh token rotation.
- Refresh tokens MUST be bound to the client and rotated on use.

### HTTP Security Headers

The following MUST be configured:

| Header | Value |
|---|---|
| `Content-Security-Policy` | Strict; no `unsafe-inline`/`unsafe-eval` unless justified in an ADR |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains; preload` |
| `X-Content-Type-Options` | `nosniff` |
| `X-Frame-Options` | `DENY` (or CSP `frame-ancestors 'none'`) |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | Restrict all unnecessary browser features |

- CORS MUST be explicitly configured per endpoint. Wildcard (`*`) MUST NOT be used in production.

### GraphQL Security

If the project uses GraphQL, the following MUST be applied (per [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)):

- Query depth limiting MUST be enforced.
- Query complexity analysis MUST be implemented with a maximum cost threshold.
- Introspection MUST be disabled in production.
- Field-level authorization MUST be enforced — never rely solely on resolver-level checks.
- Batched query abuse MUST be mitigated (limit batch size).
- Persisted/allowlisted queries SHOULD be used in production.

### Security Scanning

- Dependency vulnerability scanning MUST run in CI.
- SAST (Static Application Security Testing) MUST run in CI.
- DAST (Dynamic Application Security Testing) SHOULD run against staging environments.
- Choose scanning tools appropriate for the stack.

### Input Validation

- All external input MUST be validated at system boundaries.
- Apply OWASP input validation guidelines.
- Parameterized queries MUST be used for all database operations.

### Audit Logging

- All data access and mutations MUST be logged to an audit trail.
- Audit log entries MUST include: timestamp, actor (user/service), action, resource, outcome (success/failure), source IP.
- Audit logs MUST be stored separately from application logs.
- Audit logs MUST be tamper-evident (append-only, or signed).
- Audit log retention MUST comply with `data-privacy.md` retention policies.
- PII in audit logs MUST be pseudonymized where possible.

## See Also

- `secrets.md` — secret storage, rotation, and scanning
- `data-privacy.md` — data classification and GDPR compliance
- `api-design.md` — API-level security (rate limiting, error handling)
- `telemetry.md` — operational logging (distinct from audit logging)

## Output Requirements

The generated security doc MUST:

- Include a threat model (STRIDE or equivalent) covering all entry points and trust boundaries
- Define the authentication/authorization flow with sequence diagram (Mermaid)
- List all required HTTP security headers with exact values
- Specify chosen scanning tools and CI integration
- Address each item in the current OWASP Top 10
- Define the audit logging strategy and storage
- Include GraphQL security measures (if applicable)
