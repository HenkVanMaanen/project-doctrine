# Standards Versions

Baseline versions of all standards referenced in this doctrine. LLMs SHOULD fetch the latest version at generation time. If fetching fails or the current version cannot be determined, use these as the known-good baseline.

Last verified: 2026-03-01

## Standards

| Standard | Version / Date | URL |
|---|---|---|
| OWASP Top 10 | 2021 | https://owasp.org/www-project-top-ten/ |
| OWASP ASVS | 4.0.3 | https://owasp.org/www-project-application-security-verification-standard/ |
| WCAG | 2.2 (2023-10-05) | https://www.w3.org/TR/WCAG22/ |
| OpenAPI | 3.1.0 | https://spec.openapis.org/oas/v3.1.0 |
| OpenTelemetry | 1.x (stable) | https://opentelemetry.io/docs/ |
| Semantic Versioning | 2.0.0 | https://semver.org/ |
| Conventional Commits | 1.0.0 | https://www.conventionalcommits.org/en/v1.0.0/ |
| Keep a Changelog | 1.1.0 | https://keepachangelog.com/en/1.1.0/ |
| C4 Model | — | https://c4model.com/ |
| ICU Message Format | — | https://unicode-org.github.io/icu/userguide/format_parse/messages/ |
| Unicode CLDR | 44 | https://cldr.unicode.org/ |
| SPDX | 2.3 (ISO/IEC 5962:2021) | https://spdx.dev/ |
| FinOps Framework | — | https://www.finops.org/framework/ |
| 12-Factor App | — | https://12factor.net |
| DORA Metrics | — | https://dora.dev/guides/dora-metrics-four-keys/ |
| AuthZEN | 1.0 (draft) | https://openid.net/specs/openid-authzen-authorization-api-1_0.html |
| JSON:API | 1.1 | https://jsonapi.org/format/ |
| GraphQL | October 2021 | https://spec.graphql.org/ |
| EditorConfig | — | https://editorconfig.org/ |
| XDG Base Directory | — | https://specifications.freedesktop.org/basedir-spec/latest/ |

## RFCs

| RFC | Title | Status |
|---|---|---|
| RFC 2119 | Key words for use in RFCs | Standard |
| RFC 3339 | Date and Time on the Internet | Standard |
| RFC 5424 | Syslog Protocol | Standard |
| RFC 6265bis | Cookies | Draft — check for finalization |
| RFC 6749 | OAuth 2.0 Authorization Framework | Standard |
| RFC 7519 | JSON Web Token (JWT) | Standard |
| RFC 8594 | Sunset Header | Standard |
| RFC 8705 | OAuth 2.0 Mutual-TLS Client Authentication | Standard |
| RFC 9110 | HTTP Semantics | Standard |
| RFC 9111 | HTTP Caching | Standard |
| RFC 9457 | Problem Details for HTTP APIs | Standard |
| draft-ietf-httpapi-ratelimit-headers | Rate Limit Headers | Draft — check for finalization |
| draft-ietf-httpapi-idempotency-key-header | Idempotency Key Header | Draft — check for finalization |

When generating project docs, check whether draft RFCs have been finalized and use the final RFC number if so.
