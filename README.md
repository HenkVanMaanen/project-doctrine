# Project Doctrine

A strict, standards-based set of meta-instructions for LLMs to generate project-specific documentation. The generated docs then guide implementation.

**This repo does not produce code. It produces docs that produce code.**

## Usage

Point an LLM (e.g., Claude Code) at this repository:

```
Use https://github.com/HenkVanMaanen/project-doctrine to set up this project
```

The LLM will:

1. Ask discovery questions about your project
2. Read all doctrine files
3. Fetch the latest versions of referenced standards
4. Generate project-specific docs in `docs/`
5. Generate starter config files
6. Generate an `AGENTS.md` and `CLAUDE.md` for implementation

## Doctrine Files

| File | Topic | Applies To |
|---|---|---|
| [architecture.md](doctrine/architecture.md) | Vertical slices, CQRS, modular monolith, dependency rule, timestamps | all |
| [12-factor.md](doctrine/12-factor.md) | Config, statelessness, dev/prod parity | all |
| [security.md](doctrine/security.md) | OWASP, OAuth2/OIDC, AuthZEN, encryption, headers, audit logging | all |
| [accessibility.md](doctrine/accessibility.md) | WCAG 2.2 AAA | webapp |
| [telemetry.md](doctrine/telemetry.md) | OpenTelemetry, structured logging, SLOs | all |
| [testing.md](doctrine/testing.md) | 15 test types, TDD/BDD, 90% coverage | all |
| [api-design.md](doctrine/api-design.md) | REST/GraphQL, OpenAPI, rate limiting, deprecation | API, webapp |
| [cli.md](doctrine/cli.md) | Exit codes, signals, POSIX conventions | CLI |
| [data-privacy.md](doctrine/data-privacy.md) | GDPR, data classification, retention | all |
| [ci-cd.md](doctrine/ci-cd.md) | 19-stage pipeline, 10-min budget, feature flags | all |
| [infrastructure.md](doctrine/infrastructure.md) | Docker, IaC, health checks, container registry | all |
| [resilience.md](doctrine/resilience.md) | Circuit breakers, retries, graceful degradation | all |
| [documentation.md](doctrine/documentation.md) | ADRs, changelog, Conventional Commits, Mermaid | all |
| [i18n.md](doctrine/i18n.md) | ICU Message Format, RTL, externalized strings | webapp |
| [performance.md](doctrine/performance.md) | Core Web Vitals, caching, load testing | all |
| [database.md](doctrine/database.md) | Migrations, expand-and-contract | all with persistence |
| [secrets.md](doctrine/secrets.md) | Secret management, rotation, scanning | all |
| [versioning.md](doctrine/versioning.md) | Semantic Versioning, automated bumps | all |
| [git-workflow.md](doctrine/git-workflow.md) | Trunk-based dev, short-lived branches | all |
| [dependencies.md](doctrine/dependencies.md) | Lockfiles, license auditing, vulnerability SLA, SBOM | all |
| [disaster-recovery.md](doctrine/disaster-recovery.md) | Backups, RTO/RPO, quarterly drills | all |
| [dora.md](doctrine/dora.md) | Deployment frequency, lead time, MTTR, CFR | all |
| [code-style.md](doctrine/code-style.md) | Formatting, linting, EditorConfig | all |

## Standards

This doctrine references IETF RFCs, OWASP, WCAG, OpenTelemetry, and other stable standards. LLMs are instructed to fetch the latest versions at generation time.

## License

[MIT](LICENSE)
