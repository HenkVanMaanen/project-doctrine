# Project Doctrine

Meta-instructions for LLMs to generate project-specific documentation from standardized principles.

This repository is a strict doctrine. You are an LLM reading this to generate project-specific documentation that will guide implementation. Do not produce code — produce docs.

This doctrine uses [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) keywords (MUST, SHALL, SHOULD, MAY, MUST NOT).

When referencing standards, fetch the latest version at generation time. If a referenced RFC has been superseded, use the superseding RFC instead. The URLs in doctrine files are stable fallbacks.

## Workflow

### Step 1: Discovery

Ask the user the following before proceeding:

- **Project type**: webapp | API | CLI
- **Tech stack**: language, framework, database
- **Target users**: audience, expected scale (users, requests/sec)
- **Authentication**: required? existing provider?
- **Data sensitivity**: what PII or sensitive data will be handled?
- **Infrastructure**: cloud provider, CI/CD platform, container orchestration
- **Deployment targets**: regions, compliance jurisdictions
- **External integrations**: third-party APIs, services
- **Monorepo or polyrepo**: single repo or multiple?

### Step 2: Read Doctrine

Read all files in `doctrine/`. Apply only files matching the project type (see table below).

### Step 3: Fetch Live Standards

For each referenced standard (OWASP Top 10, WCAG 2.2, OpenAPI, etc.), fetch the latest version to ensure current guidance. If an RFC has been superseded, use the successor.

### Step 4: Generate Project Documentation

Generate the following in the project's `docs/` directory:

| Output File | Source Doctrine Files |
|---|---|
| `docs/architecture.md` | 12-factor, infrastructure |
| `docs/security.md` | security, secrets |
| `docs/accessibility.md` | accessibility (webapp only) |
| `docs/observability.md` | telemetry |
| `docs/testing.md` | testing |
| `docs/api.md` | api-design (API/webapp only) |
| `docs/data-privacy.md` | data-privacy |
| `docs/ci-cd.md` | ci-cd, code-style |
| `docs/resilience.md` | resilience |
| `docs/i18n.md` | i18n (webapp only) |
| `docs/performance.md` | performance |
| `docs/database.md` | database (if applicable) |
| `docs/versioning.md` | versioning, git-workflow |
| `docs/dependencies.md` | dependencies |
| `docs/disaster-recovery.md` | disaster-recovery |
| `docs/documentation.md` | documentation |

Each generated doc MUST:
- Be concise and actionable
- Specify stack-specific tooling choices
- Contain measurable acceptance criteria
- Use RFC 2119 keywords
- Link to standards rather than repeating their content

### Step 5: Generate Project AGENTS.md

Generate an `AGENTS.md` in the project root that instructs an LLM to implement the project following all generated docs in `docs/`. This file MUST reference each generated doc.

### Step 6: Generate Project CLAUDE.md

Generate a `CLAUDE.md` in the project root containing only:

```
@AGENTS.md
```

## Doctrine Files

| File | Applies To |
|---|---|
| `doctrine/12-factor.md` | all |
| `doctrine/security.md` | all |
| `doctrine/accessibility.md` | webapp |
| `doctrine/telemetry.md` | all |
| `doctrine/testing.md` | all |
| `doctrine/api-design.md` | API, webapp |
| `doctrine/data-privacy.md` | all |
| `doctrine/ci-cd.md` | all |
| `doctrine/infrastructure.md` | all |
| `doctrine/resilience.md` | all |
| `doctrine/documentation.md` | all |
| `doctrine/i18n.md` | webapp |
| `doctrine/performance.md` | all |
| `doctrine/database.md` | all with persistence |
| `doctrine/secrets.md` | all |
| `doctrine/versioning.md` | all |
| `doctrine/git-workflow.md` | all |
| `doctrine/dependencies.md` | all |
| `doctrine/disaster-recovery.md` | all |
| `doctrine/code-style.md` | all |

## Priority Tiers

### Tier 1 — Non-negotiable

MUST be fully addressed before any implementation begins:

- `security.md`
- `data-privacy.md`
- `testing.md`

### Tier 2 — Required

MUST be addressed in project documentation:

- All remaining doctrine files

## License

All projects MUST include the [MIT License](https://opensource.org/licenses/MIT).
