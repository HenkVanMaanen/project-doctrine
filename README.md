# Project Doctrine

A strict, standards-based set of meta-instructions for LLMs to generate project-specific documentation. The generated docs then guide implementation.

**This repo does not produce code. It produces docs that produce code.**

## Usage

### As a Claude Code skill (recommended)

Install once, then apply the doctrine to any repository — new or existing:

```
/plugin marketplace add HenkVanMaanen/project-doctrine
/plugin install project-doctrine@project-doctrine
```

Then, inside any target repo:

```
/apply-doctrine
```

The skill (`skills/apply-doctrine/SKILL.md`) is the authoritative workflow. It orchestrates everything with parallel subagents: Discovery questions, doctrine reading + live standards verification concurrently, one generation agent per output doc, parallel consistency validators, then implementation fanned out per vertical slice with a final evidence-based compliance walk. On existing repos it inserts a parallel audit/gap-analysis phase first. The root `AGENTS.md` is a pointer to the skill for coding agents reading the repo directly.

### As a plain prompt

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
| [accessibility.md](doctrine/accessibility.md) | WCAG 2.2 AA + enumerated AAA, EN 301 549 | webapp |
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
| [dora.md](doctrine/dora.md) | Five delivery metrics, AI as amplifier, SPACE/DevEx guardrails | all |
| [code-style.md](doctrine/code-style.md) | Formatting, linting, EditorConfig | all |
| [code-quality.md](doctrine/code-quality.md) | ISO 5055 structural quality, CWE weakness gates, technical debt | all |
| [finops.md](doctrine/finops.md) | Cloud cost management, tagging, budgets | all |
| [supply-chain.md](doctrine/supply-chain.md) | SLSA, artifact signing, provenance, CI hardening | all |
| [incident-response.md](doctrine/incident-response.md) | Severities, on-call, postmortems, error budgets | all |
| [ai-llm.md](doctrine/ai-llm.md) | Prompt injection, output handling, agency limits, evals | AI/LLM features |
| [async-messaging.md](doctrine/async-messaging.md) | Queues, outbox, idempotent consumers, DLQ, background jobs | async processing |
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
│   ├── supply-chain.md
│   ├── incident-response.md
│   ├── ai-llm.md              # AI/LLM features only
│   ├── async.md               # async processing only
│   ├── waivers.md             # user-approved exception register
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
