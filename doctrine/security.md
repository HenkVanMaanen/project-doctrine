# Security

## Standards

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- GraphQL Security: https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html
- File Upload Security: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
- AuthZEN: https://openid.net/specs/openid-authzen-authorization-api-1_0.html

Fetch the latest versions when generating project docs.

Applies to: all

## Requirements

### Authentication

- OAuth 2.0 ([RFC 6749](https://www.rfc-editor.org/rfc/rfc6749)) and OpenID Connect ([spec](https://openid.net/specs/openid-connect-core-1_0.html)) MUST be used.
- JWTs ([RFC 7519](https://www.rfc-editor.org/rfc/rfc7519)) MUST be used for stateless session tokens.
- Token lifetimes MUST be short-lived with refresh token rotation.
- Refresh tokens MUST be bound to the client and rotated on use.

### Authorization

- An authorization model MUST be chosen (RBAC, ABAC, or policy-based) and documented in an ADR.
- Authorization SHOULD follow the [AuthZEN](https://openid.net/specs/openid-authzen-authorization-api-1_0.html) authorization API specification to decouple authorization decisions from business logic.
- Authorization decisions MUST be enforced at the API/service boundary, not only in the UI.

### Service-to-Service Authentication

- Service-to-service communication MUST use OAuth 2.0 client credentials flow ([RFC 6749 Section 4.4](https://www.rfc-editor.org/rfc/rfc6749#section-4.4)) or mTLS ([RFC 8705](https://www.rfc-editor.org/rfc/rfc8705)).
- API keys MUST NOT be used as the sole authentication mechanism for service-to-service communication.

### Encryption

- **In transit**: All communication MUST use TLS. TLS 1.2 MUST be the minimum version; TLS 1.3 SHOULD be preferred. Weak cipher suites MUST be disabled. Reference: [NIST SP 800-52 Rev 2](https://csrc.nist.gov/pubs/sp/800/52/r2/final).
- **At rest**: Sensitive and restricted data (see `data-privacy.md` classification) MUST be encrypted at rest. Database-level or storage-level encryption MUST be enabled for all persistent stores containing sensitive data.
- **Key management**: Encryption keys MUST be stored in a secret manager (see `secrets.md`), never alongside encrypted data. Key rotation MUST be supported without downtime. Reference: [NIST SP 800-175B](https://csrc.nist.gov/pubs/sp/800/175/b/r1/final).

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

### Cookie Security (webapp)

Per [RFC 6265bis](https://datatracker.ietf.org/doc/draft-ietf-httpbis-rfc6265bis/) — fetch the latest status, it may have been finalized:

- `Secure` flag MUST be set on all cookies.
- `HttpOnly` flag MUST be set on session and authentication cookies.
- `SameSite` MUST be set to `Strict` or `Lax` (choose per cookie, document rationale).
- Cookie name prefixes `__Host-` SHOULD be used for host-only cookies.
- Cookie expiration MUST be set explicitly — no session cookies without defined lifetime.

### GraphQL Security

If the project uses GraphQL, the following MUST be applied (per [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)):

- Query depth limiting MUST be enforced.
- Query complexity analysis MUST be implemented with a maximum cost threshold.
- Introspection MUST be disabled in production.
- Field-level authorization MUST be enforced — never rely solely on resolver-level checks.
- Batched query abuse MUST be mitigated (limit batch size).
- Persisted/allowlisted queries SHOULD be used in production.

### File Upload Security

If the project handles file uploads, the following MUST be applied (per [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)):

- File type validation MUST use an allowlist (not blocklist), checking both extension and magic bytes.
- File size limits MUST be enforced server-side.
- Uploaded files MUST be scanned for malware before storage.
- Files MUST be stored outside the web root.
- Filenames MUST be generated server-side — never use user-provided filenames.
- Uploaded files MUST NOT be served with user-controlled `Content-Type` headers.

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
- `architecture.md` — dependency rule aligns with AuthZEN decoupling

## Output Requirements

The generated security doc MUST:

- Include a threat model (STRIDE or equivalent) covering all entry points and trust boundaries
- Define the authentication/authorization flow with sequence diagram (Mermaid)
- Define the authorization model (RBAC/ABAC/policy-based) with AuthZEN integration
- Define the encryption policy (in transit, at rest, key management)
- List all required HTTP security headers with exact values
- Define cookie security policy (if webapp)
- Specify chosen scanning tools and CI integration
- Address each item in the current OWASP Top 10
- Define the audit logging strategy and storage
- Define file upload security measures (if applicable)
- Define service-to-service authentication flow (if applicable)
- Include GraphQL security measures (if applicable)
