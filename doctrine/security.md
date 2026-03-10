# Security

## Standards

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/

Fetch the latest versions of both when generating project docs.

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

### Security Scanning

- Dependency vulnerability scanning MUST run in CI.
- SAST (Static Application Security Testing) MUST run in CI.
- DAST (Dynamic Application Security Testing) SHOULD run against staging environments.
- Choose scanning tools appropriate for the stack.

### Input Validation

- All external input MUST be validated at system boundaries.
- Apply OWASP input validation guidelines.
- Parameterized queries MUST be used for all database operations.

## Output Requirements

The generated security doc MUST:

- Include a threat model (STRIDE or equivalent)
- Define the authentication/authorization flow with sequence diagram (Mermaid)
- List all required HTTP security headers with exact values
- Specify chosen scanning tools and CI integration
- Address each item in the current OWASP Top 10
