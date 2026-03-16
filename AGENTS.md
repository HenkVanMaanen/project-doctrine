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
- Formatter config
- Linter config
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

After generating all documentation and config files, implement the full project and verify it works. This is not scaffolding — it is a complete, working codebase. Every endpoint, every middleware, every test type, and every config file referenced in the generated docs MUST exist and function.

#### 10.1: Initialize Project

Set up the monorepo/project structure exactly as defined in `docs/architecture.md`:

- Initialize the project manifest with all required dependencies
- Create the directory structure from the architecture doc — use vertical slice directories per operation named `{entity}-{operation}` (e.g., `features/link-create/`, `features/link-delete/`, `features/link-get/`, `features/link-list/`, `features/auth-login/`, `features/auth-register/`), not entity-grouped modules or flat horizontal directories
- Install dependencies and verify they resolve
- Every build/test/lint script or command referenced in CI workflows MUST work when invoked

#### 10.2: Implement Tier 1 Foundations

Build everything required by the Tier 1 checklist (`docs/tier1-checklist.md`). Every item on the checklist MUST have corresponding code. Implement all requirements from the Tier 1 doctrine files:

- **Security** (`doctrine/security.md`): authentication (JWT/sessions/API keys), password hashing, RBAC enforcement, input validation, HTTP security headers, rate limiting, SSRF protection, audit logging, account lockout, refresh token rotation
- **Data Privacy** (`doctrine/data-privacy.md`): multi-tenant RLS, GDPR erasure and export endpoints, IP anonymization with cleanup job, audit log pseudonymization
- **Observability** (`doctrine/telemetry.md`): OpenTelemetry initialization, structured logging with all four required fields, health checks, traceId in error responses

All prescriptive implementation details — including anti-patterns to avoid, stack-specific tooling, and enforcement requirements — are in the respective doctrine files. Do not soften or skip any requirement.

#### 10.3: Implement All Features

Build every endpoint and feature defined in the generated `AGENTS.md`. Do not skip phases or endpoints:

- Every endpoint MUST be implemented with authentication middleware, input validation, parameterized queries, and audit logging
- Apply all security requirements from `doctrine/security.md` to every route: RBAC enforcement, rate limiting bound to handlers, audit logging for all state-changing operations (including logout and token refresh)
- Cache invalidation MUST occur when data changes (if caching is used)

Follow TDD for each feature: write failing test → implement → verify pass.

#### 10.4: Generate OpenAPI Spec

Generate a **committed** `openapi.yaml` (or `openapi.json`) in the project root that documents all implemented endpoints. Even if the framework can serve the spec dynamically (e.g., SpringDoc, FastAPI `/docs`), a static file MUST be committed to the repository so contract tests can load it without booting the app's spec endpoint. This spec MUST:

- Describe every endpoint from the generated `AGENTS.md`
- Include request/response schemas matching the validation schemas used in the code
- Be valid OpenAPI 3.1 (validate with a linter or parser)
- Be used by contract tests to verify routes match the spec

#### 10.5: Implement All Test Types

Every test type defined in `doctrine/testing.md` MUST have at least one working test. Follow the "Test Implementation Requirements" table, "Test Anti-Patterns" section, and "Testcontainers" section in `doctrine/testing.md` exactly.

Key requirements (see `doctrine/testing.md` for full details):

- All 13 core test types MUST have at least one file — breadth-first (one per type before deepening any type). Conditional test types (snapshot, visual regression, load) MUST be implemented when applicable
- Tests requiring infrastructure MUST use Testcontainers — no environment variable gating
- No tautological assertions, skipped tests, or empty bodies
- Each test type MUST use the technique appropriate to that type (not relabeled unit tests)
- Test data MUST use factories with randomized data
- Code coverage ≥ 90% for lines, branches, functions, and statements

#### 10.6: Implement CI/CD

Implement both pipelines as defined in `doctrine/ci-cd.md`:

- Commit pipeline (pre-merge) and deploy pipeline (post-merge) with all stages defined in the doctrine
- Follow all pipeline security requirements from `doctrine/ci-cd.md`: SHA pinning with real verifiable SHAs, pre-commit hooks, secrets management
- All config files and scripts referenced in CI MUST exist and work when invoked

#### 10.7: Implement Infrastructure

Implement all infrastructure requirements from `doctrine/infrastructure.md`:

- Dockerfile with multi-stage build, non-root user, and HEALTHCHECK instruction
- docker-compose.yml with all backing services and health checks
- IaC directory structure matching `docs/architecture.md` (at minimum placeholder files documenting required resources)

#### 10.8: Build Verification

Run ALL of the following steps using the stack's idiomatic commands and fix any failures before reporting:

1. **Install dependencies** — resolve and lock all dependencies
2. **Compile / build** — full production build with zero errors
3. **Lint** — run the configured linter with zero errors
4. **Run all tests** — execute the full test suite
5. **Coverage** — verify coverage ≥ 90% for lines, branches, functions, and statements

If any command fails, fix the code and re-run. Do NOT report success with failing tests.

Common pitfalls:
- Every script or command referenced in CI workflows MUST work when invoked locally
- All config files referenced by build/lint/test tools MUST exist at the specified paths
- If using a monorepo, shared packages MUST be built before dependent packages can compile

#### 10.9: Doctrine Compliance Verification

Walk through the generated `docs/tier1-checklist.md` item by item. For each item, verify the corresponding code exists. Specifically check:

- [ ] Every endpoint in the generated `AGENTS.md` has a route handler
- [ ] Every route has input validation at the boundary
- [ ] Every state-changing operation writes an audit log entry
- [ ] RLS is activated per-request (not just defined in SQL)
- [ ] RBAC is enforced (not just role stored — role checked before access)
- [ ] Passwords use a strong hash (bcrypt/argon2id/scrypt), not SHA-256 or MD5
- [ ] OpenTelemetry is initialized and tracing works
- [ ] CI workflows reference scripts/commands that exist and work
- [ ] Architecture test config exists and rules match `docs/architecture.md`
- [ ] All 13 core test types have at least one test file: unit, integration, e2e, contract, property-based, mutation, fuzz, architecture, smoke, chaos, concurrency, data migration, infrastructure
- [ ] Conditional test types are implemented when applicable: snapshot/visual regression (webapp with components), load testing (when performance budgets are defined)
- [ ] Mutation test actually invokes the mutation tool with real code mutation (not just checks config exists, not `--dryRun`, not `--list` mode)
- [ ] Contract test makes real HTTP requests and validates responses against OpenAPI schema (not just checks YAML structure)
- [ ] Every log line includes `traceId`, `spanId`, `tenantId`, and `service` — verify all four fields are present, not just traceId/spanId
- [ ] `tenantId` is logged as empty string `""` (not null or omitted) for unauthenticated requests — test by checking a login or health check log entry
- [ ] Coverage threshold is set to 90% (not 80% or lower) in both test config and CI pipeline
- [ ] OpenAPI spec exists as a committed static file and matches implemented routes
- [ ] GitHub Actions SHAs are real (not fabricated placeholders)
- [ ] Terraform directory structure exists (at minimum placeholder `main.tf` files)
- [ ] Linting passes with zero errors (verify the lint command actually works)
- [ ] Rate limiting is actually applied to route handlers (not just configured but unbound)
- [ ] API key validation uses HMAC-SHA256 with a configured secret (not plain SHA-256 hash)
- [ ] Audit logging covers login, logout, register, token refresh, and all CRUD operations
- [ ] Pre-commit hook config exists (e.g., Husky, .pre-commit-config.yaml, lefthook)
- [ ] IP data cleanup job exists (cron, scheduled task, or background worker for aged data)
- [ ] RBAC role checks are enforced on destructive operations (DELETE requires admin/owner, not just member)
- [ ] Contract test loads the committed `openapi.yaml` static file (not the app's live spec endpoint)
- [ ] OpenTelemetry SDK initializes before framework/application imports (verify import order in entry point)
- [ ] RLS policies exist in migration SQL (query `pg_policies` or equivalent — `SET LOCAL` without policies provides no isolation)
- [ ] Coverage is enforced in CI pipeline (not just set in test config — CI step MUST fail the build on coverage below 90%)
- [ ] Session-based auth (if used): sessions stored server-side in backing service, session ID regenerated on login, sessions invalidated server-side on logout

If any check fails, fix it before proceeding.

#### 10.10: Report

Summarize:
- Total files generated (source, tests, config, docs)
- All endpoints implemented with their HTTP methods
- Test results (total tests, pass/fail, coverage percentage)
- Any deviations from the generated docs with justification
- Any items from the tier1-checklist that could not be implemented with justification

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
