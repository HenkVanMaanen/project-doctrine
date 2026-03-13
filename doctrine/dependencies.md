# Dependency Management

Applies to: all

## Requirements

### Lockfiles

- Lockfiles MUST be committed to version control.
- Package installation in CI MUST use frozen/locked installs (e.g., `npm ci`, `pip install --require-hashes`).

### Updates

- Automated dependency update checks MUST be configured (e.g., Dependabot, Renovate).
- Security updates MUST be applied within 48 hours of disclosure.
- Non-security updates SHOULD be reviewed weekly.

### License Auditing

- Dependency licenses MUST be audited in CI.
- Copyleft licenses (GPL, AGPL) MUST NOT be included in MIT-licensed projects unless fully isolated (e.g., dev-only tools).
- A license allowlist MUST be maintained.

### Vulnerability Scanning

- Stack-appropriate audit tools MUST run in CI (e.g., `npm audit`, `pip audit`, `cargo audit`).
- Builds MUST fail on known high/critical vulnerabilities.

### SBOM (Software Bill of Materials)

- An SBOM MUST be generated in CI for every release.
- SBOM format MUST be [SPDX](https://spdx.dev/) ([ISO/IEC 5962:2021](https://www.iso.org/standard/81870.html)).
- The SBOM MUST be published alongside release artifacts.
- The SBOM MUST include all direct and transitive dependencies.

## See Also

- `security.md` — vulnerability scanning, SAST
- `ci-cd.md` — security scan pipeline stage
- `infrastructure.md` — container image dependency scanning

## Output Requirements

The generated dependencies doc MUST:

- Specify the dependency update tool and configuration
- Define the license allowlist
- Define the vulnerability response process and SLA
- Specify lockfile enforcement in CI
- Define SBOM generation tooling and publication
