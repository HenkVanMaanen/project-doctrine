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
5. Generate starter config files and LICENSE
6. Generate an `AGENTS.md` and `CLAUDE.md` for implementation
7. Build the project, implement all features, and verify doctrine compliance

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
| [ci-cd.md](doctrine/ci-cd.md) | Dual pipeline (commit + deploy), parallel stages, feature flags | all |
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
| [finops.md](doctrine/finops.md) | Cloud cost management, tagging, budgets | all |
| [standards-versions.md](doctrine/standards-versions.md) | Baseline versions of all referenced standards | reference |

## Example Output

When applied to a project, this doctrine generates:

```
project-root/
├── docs/
│   ├── architecture.md
│   ├── security.md
│   ├── accessibility.md      # webapp only
│   ├── observability.md
│   ├── testing.md
│   ├── api.md                 # API/webapp only
│   ├── data-privacy.md
│   ├── ci-cd.md
│   ├── resilience.md
│   ├── i18n.md                # webapp only
│   ├── performance.md
│   ├── database.md            # if applicable
│   ├── versioning.md
│   ├── dependencies.md
│   ├── disaster-recovery.md
│   ├── documentation.md
│   ├── finops.md
│   └── tier1-checklist.md
├── .editorconfig
├── .gitignore
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── CHANGELOG.md
├── LICENSE
├── AGENTS.md                  # implementation instructions for agents
└── CLAUDE.md
```

Each generated doc is concise, actionable, stack-specific, and contains measurable acceptance criteria.

## Standards

This doctrine references IETF RFCs, OWASP, WCAG, OpenTelemetry, and other stable standards. LLMs are instructed to fetch the latest versions at generation time. See [standards-versions.md](doctrine/standards-versions.md) for the baseline reference list.

## License

[MIT](LICENSE)
