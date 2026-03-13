# Project Doctrine

Meta-instructions for LLMs to generate project-specific documentation from standardized principles.

This repository is a strict doctrine. You are an LLM reading this to generate project-specific documentation that will guide implementation. Do not produce code — produce docs and starter config files.

This doctrine uses [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) keywords (MUST, SHALL, SHOULD, MAY, MUST NOT).

When referencing standards, fetch the latest version at generation time. If a referenced RFC has been superseded, use the superseding RFC instead. The URLs in doctrine files are stable fallbacks. See `doctrine/standards-versions.md` for known-good baseline versions.

## Agent-First Implementation

The generated project documentation is designed for implementation by AI agents (LLMs), not humans. This means:

- All requirements are achievable — agents can handle the full scope without scaling concerns.
- Agents MAY execute tasks in parallel using subagents or agent teams.
- Steps in this workflow that are independent SHOULD be parallelized across agents.
- The generated project `AGENTS.md` MUST instruct implementing agents to work in parallel where possible.
- No requirement should be softened due to perceived complexity — agents can implement comprehensive testing, full accessibility compliance, and complete observability.

## Workflow

### Step 1: Discovery

Ask the user the following before proceeding.

#### Required

These MUST be answered before generation can proceed:

- **Project type**: webapp | API | CLI
- **Tech stack**: language, framework, database
- **Target users**: audience, expected scale (concurrent users, peak requests/sec)
- **Data sensitivity**: what PII or sensitive data will be handled?
- **Infrastructure**: cloud provider, CI/CD platform, container orchestration

#### Optional (defaults applied if not answered)

- **Authentication**: required? existing provider? (default: required, no existing provider)
- **Multi-tenant or single-tenant?** (default: single-tenant)
- **Open source or proprietary?** (default: proprietary)
- **Deployment targets**: regions, compliance jurisdictions (default: single region, GDPR)
- **Regulatory requirements beyond GDPR?** (e.g., PCI-DSS, HIPAA) (default: GDPR only)
- **External integrations**: third-party APIs, services (default: none)
- **Monorepo or polyrepo**: single repo or multiple? (default: monorepo)
- **Offline/PWA requirements?** (default: no)
- **Expected traffic patterns**: sustained load, peak spikes, seasonal variation (default: even load, 2x peak)

### Step 2: Read Doctrine

Read all files in `doctrine/`. Apply only files matching the project type (see table below).

This step MAY run in parallel with Step 3.

### Step 3: Fetch Live Standards

For each referenced standard (OWASP Top 10, WCAG 2.2, OpenAPI, etc.), fetch the latest version to ensure current guidance. If an RFC has been superseded, use the successor.

Use `doctrine/standards-versions.md` as the baseline. If fetching fails, fall back to the versions listed there.

This step MAY run in parallel with Step 2.

### Step 4: Generate Project Documentation

Generate the following in the project's `docs/` directory. Independent docs MAY be generated in parallel by multiple agents:

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
| `docs/finops.md` | finops |

Each generated doc MUST:
- Be concise and actionable
- Specify stack-specific tooling choices
- Contain measurable acceptance criteria
- Use RFC 2119 keywords
- Link to standards rather than repeating their content

### Step 5: Generate Starter Config Files

Alongside docs, generate applicable config files in the project root. This step MAY run in parallel with Step 4:

- `.editorconfig`
- `.gitignore`
- `Dockerfile` and `docker-compose.yml`
- Formatter config (e.g., `.prettierrc`, `rustfmt.toml`)
- Linter config (e.g., `.eslintrc.json`, `clippy.toml`)
- Pre-commit hook config
- PR template (`.github/pull_request_template.md` or equivalent)
- `.env.example`
- `CHANGELOG.md` (initial)
- `LICENSE` (MIT — required for all projects)

Only generate files applicable to the chosen stack and project type.

### Step 6: Generate Tier 1 Compliance Checklist

Generate `docs/tier1-checklist.md` — a checklist covering all Tier 1 (non-negotiable) requirements from `security.md`, `data-privacy.md`, and `testing.md`. This checklist MUST be reviewed and confirmed before implementation begins.

### Step 7: Validate Consistency

Review all generated docs for internal consistency. Verify:

- No contradictions between docs (e.g., performance budgets vs. testing requirements)
- All cross-references between docs are valid
- Tooling choices are consistent across docs (same test framework, same CI platform, etc.)
- Security headers don't conflict with CDN or caching config
- CI pipeline time budgets are achievable with the defined parallelization strategy
- All acceptance criteria are measurable and non-overlapping

If inconsistencies are found, resolve them and document the rationale.

### Step 8: Generate Project AGENTS.md

Generate an `AGENTS.md` in the project root that instructs agents to implement the project following all generated docs in `docs/`. This file MUST:

- Reference each generated doc
- Define which tasks can be parallelized across agents
- Instruct agents to work in parallel where tasks are independent
- Define the implementation order (Tier 1 requirements first)

### Step 9: Generate Project CLAUDE.md

Generate a `CLAUDE.md` in the project root containing only:

```
@AGENTS.md
```

### Step 10: Build and Verify

After generating all documentation and config files, implement the project scaffolding and verify it works:

1. **Initialize the project** — Set up the monorepo/project structure as defined in `docs/architecture.md`:
   - Initialize `package.json` (or equivalent) with all required dependencies and scripts
   - Create the directory structure from the architecture doc
   - Install dependencies and verify `pnpm install` (or equivalent) succeeds

2. **Implement Tier 1 foundations** — Build the minimum code required by the Tier 1 checklist (`docs/tier1-checklist.md`):
   - Shared infrastructure: database client, cache client, config validation, error types, telemetry setup
   - Auth middleware (JWT validation + API key validation)
   - Authorization module (RBAC)
   - Input validation setup (Zod or equivalent)
   - HTTP security headers middleware
   - Audit logging infrastructure
   - Database migrations for all tables defined in `docs/database.md`
   - RLS policies for multi-tenant isolation (if applicable)

3. **Implement core features** — Build all features defined in the generated `AGENTS.md`, following the implementation order and parallelization guidelines defined there. Each feature MUST follow TDD:
   - Write failing test first
   - Implement the feature
   - Verify test passes

4. **Build verification** — Run the following and fix any failures:
   - `pnpm install` (or equivalent) — dependencies resolve
   - `pnpm build` (or equivalent) — TypeScript compiles with no errors
   - `pnpm lint` — no lint errors
   - `pnpm test` — all tests pass
   - `pnpm test:coverage` — coverage ≥ 90%

5. **Doctrine compliance check** — Verify the implementation against the generated docs:
   - Architecture: dependency-cruiser (or equivalent) passes — no dependency rule violations
   - Security: all HTTP security headers present, input validation on all routes, parameterized queries only
   - Testing: all required test types exist (unit, integration, contract, property-based, architecture)
   - API: all endpoints match the OpenAPI spec in `docs/api.md`
   - Observability: structured logging, metrics, health check endpoints functional

6. **Report** — Summarize what was built, any deviations from the docs, and any issues found during verification.

This step ensures the generated documentation is not just correct on paper but produces a working, compliant codebase.

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
| `doctrine/finops.md` | all |

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
