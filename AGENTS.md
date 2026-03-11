# Project Doctrine

Meta-instructions for LLMs to generate project-specific documentation from standardized principles.

This repository is a strict doctrine. You are an LLM reading this to generate project-specific documentation that will guide implementation. Do not produce code — produce docs and starter config files.

This doctrine uses [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) keywords (MUST, SHALL, SHOULD, MAY, MUST NOT).

When referencing standards, fetch the latest version at generation time. If a referenced RFC has been superseded, use the superseding RFC instead. The URLs in doctrine files are stable fallbacks.

## Workflow

### Step 1: Discovery

Ask the user the following before proceeding:

- **Project type**: webapp | API | CLI
- **Tech stack**: language, framework, database
- **Target users**: audience, expected scale (concurrent users, peak requests/sec)
- **Authentication**: required? existing provider?
- **Data sensitivity**: what PII or sensitive data will be handled?
- **Multi-tenant or single-tenant?**
- **Open source or proprietary?**
- **Infrastructure**: cloud provider, CI/CD platform, container orchestration
- **Deployment targets**: regions, compliance jurisdictions
- **Regulatory requirements beyond GDPR?** (e.g., PCI-DSS, HIPAA)
- **External integrations**: third-party APIs, services
- **Monorepo or polyrepo**: single repo or multiple?
- **Offline/PWA requirements?**
- **Expected traffic patterns**: sustained load, peak spikes, seasonal variation

### Step 2: Read Doctrine

Read all files in `doctrine/`. Apply only files matching the project type (see table below).

### Step 3: Fetch Live Standards

For each referenced standard (OWASP Top 10, WCAG 2.2, OpenAPI, etc.), fetch the latest version to ensure current guidance. If an RFC has been superseded, use the successor.

### Step 4: Generate Project Documentation

Generate the following in the project's `docs/` directory:

| Output File | Source Doctrine Files |
|---|---|
| `docs/architecture.md` | architecture, 12-factor, infrastructure, cli (CLI only) |
| `docs/security.md` | security, secrets |
| `docs/accessibility.md` | accessibility (webapp only) |
| `docs/observability.md` | telemetry, dora |
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

### Step 5: Generate Starter Config Files

Alongside docs, generate applicable config files in the project root:

- `.editorconfig`
- `.gitignore`
- `Dockerfile` and `docker-compose.yml`
- Formatter config (e.g., `.prettierrc`, `rustfmt.toml`)
- Linter config (e.g., `.eslintrc.json`, `clippy.toml`)
- Pre-commit hook config
- PR template (`.github/pull_request_template.md` or equivalent)
- `.env.example`
- `CHANGELOG.md` (initial)

Only generate files applicable to the chosen stack and project type.

### Step 6: Generate Tier 1 Compliance Checklist

Generate `docs/tier1-checklist.md` — a checklist covering all Tier 1 (non-negotiable) requirements from `security.md`, `data-privacy.md`, and `testing.md`. This checklist MUST be reviewed and confirmed before implementation begins.

### Step 7: Validate Consistency

Review all generated docs for internal consistency. Verify:

- No contradictions between docs (e.g., performance budgets vs. testing requirements)
- All cross-references between docs are valid
- Tooling choices are consistent across docs (same test framework, same CI platform, etc.)
- Security headers don't conflict with CDN or caching config
- All acceptance criteria are measurable and non-overlapping

If inconsistencies are found, resolve them and document the rationale.

### Step 8: Generate Project AGENTS.md

Generate an `AGENTS.md` in the project root that instructs an LLM to implement the project following all generated docs in `docs/`. This file MUST reference each generated doc.

### Step 9: Generate Project CLAUDE.md

Generate a `CLAUDE.md` in the project root containing only:

```
@AGENTS.md
```

## Doctrine Files

| File | Applies To |
|---|---|
| `doctrine/architecture.md` | all |
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
| `doctrine/dora.md` | all |
| `doctrine/cli.md` | CLI |
| `doctrine/code-style.md` | all |

## Priority Tiers

### Tier 1 — Non-negotiable

MUST be fully addressed before any implementation begins. A Tier 1 compliance checklist MUST be generated and confirmed:

- `security.md`
- `data-privacy.md`
- `testing.md`

### Tier 2 — Required

MUST be addressed in project documentation:

- All remaining doctrine files

## Existing Projects

If applying this doctrine to an existing codebase (not greenfield):

1. Audit the current state against all applicable doctrine files.
2. Produce a gap analysis documenting what is missing or non-compliant.
3. Prioritize Tier 1 gaps (security, data-privacy, testing) for immediate remediation.
4. Create a roadmap for incremental adoption of Tier 2 requirements.
5. Generate project docs as normal, noting existing state and required changes.

## License

All projects MUST include the [MIT License](https://opensource.org/licenses/MIT).
