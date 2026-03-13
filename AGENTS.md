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

After generating all documentation and config files, implement the full project and verify it works. This is not scaffolding — it is a complete, working codebase. Every endpoint, every middleware, every test type, and every config file referenced in the generated docs MUST exist and function.

#### 10.1: Initialize Project

Set up the monorepo/project structure exactly as defined in `docs/architecture.md`:

- Initialize `package.json` (or equivalent) with all required dependencies and scripts
- Create the directory structure from the architecture doc — use vertical slice directories (e.g., `features/links/`), not flat `routes/` + `services/` directories
- Install dependencies and verify `pnpm install` (or equivalent) succeeds
- Every npm script referenced in CI workflows MUST exist in `package.json` (e.g., `test`, `test:coverage`, `build`, `lint`, `typecheck`)

#### 10.2: Implement Tier 1 Foundations

Build everything required by the Tier 1 checklist (`docs/tier1-checklist.md`). Every item on the checklist MUST have corresponding code:

**Security:**
- Auth middleware: JWT validation (RS256) + API key validation (HMAC-SHA256)
- Password hashing: bcrypt with cost factor ≥ 12 — NOT SHA-256, NOT plain hashing
- RBAC middleware: `requireRole()` or equivalent that enforces role checks on protected routes
- Input validation: Zod schemas at every route boundary
- HTTP security headers: Helmet or equivalent with HSTS, CSP, X-Frame-Options, Referrer-Policy
- Rate limiting: per-endpoint limits as defined in `docs/security.md`
- SSRF protection: URL validation that blocks private IP ranges, localhost, cloud metadata endpoints
- Audit logging: a working service that writes to the `audit_log` table on every state-changing operation
- Account lockout: lock accounts after N consecutive failed login attempts
- Refresh token rotation: issue new refresh token on every refresh, invalidate the old one, detect reuse (family invalidation)

**Data Privacy:**
- Multi-tenant RLS: `SET LOCAL app.current_tenant_id` MUST be called at the start of every request — not just WHERE clause filtering
- GDPR erasure endpoint: implement the full erasure pipeline (hard delete PII, anonymize audit logs)
- GDPR export endpoint: return all user data as JSON/CSV
- IP anonymization: hash IPs before storage, automated cleanup job for aged data
- Audit log pseudonymization: emails stored as `sha256(email + AUDIT_SALT)`, never plaintext

**Observability:**
- OpenTelemetry: install and configure `@opentelemetry/sdk-node` with auto-instrumentation for HTTP, PostgreSQL, Redis
- Structured logging: pino with `traceId`, `spanId`, `tenantId`, `service` in every log entry
- Health checks: `/healthz` (liveness) and `/readyz` (readiness with DB+Redis checks)
- `traceId` in error responses: every RFC 9457 Problem Details response MUST include a trace/request ID

#### 10.3: Implement All Features

Build every endpoint and feature defined in the generated `AGENTS.md`. Do not skip phases or endpoints:

- Every endpoint listed in the generated `AGENTS.md` MUST be implemented
- Every route MUST have authentication (`authenticate` preHandler)
- Every state-changing route MUST call the audit logging service
- Every route that accepts user input MUST validate with Zod at the boundary
- Every database query MUST use parameterized queries
- Cache invalidation MUST occur when data changes (if caching is used)

Follow TDD for each feature: write failing test → implement → verify pass.

#### 10.4: Generate OpenAPI Spec

Generate an `openapi.yaml` (or `openapi.json`) in the project root that documents all implemented endpoints. This spec MUST:

- Describe every endpoint from the generated `AGENTS.md`
- Include request/response schemas matching the Zod validation schemas
- Be valid OpenAPI 3.1 (validate with a linter or parser)
- Be used by contract tests to verify routes match the spec

#### 10.5: Implement All Test Types

Every test type defined in `docs/testing.md` MUST have at least one working test:

| Test Type | Minimum Requirement |
|---|---|
| Unit | Tests for all services and middleware |
| Integration | Tests using real DB/Redis (Testcontainers or equivalent), not mocks |
| E2E | At least one full request flow (create link → redirect → verify analytics) |
| Contract | OpenAPI spec validation against actual routes |
| Property-based | At least one test using fast-check or equivalent for core domain logic |
| Mutation | Stryker config file with thresholds (runs in deploy pipeline, not required to pass locally) |
| Fuzz | At least one fuzz target for input parsing |
| Architecture | dependency-cruiser config (`.dependency-cruiser.cjs`) with rules enforcing the dependency direction |
| Smoke | Post-deploy smoke test script that hits health + core endpoints |
| Chaos | At least one fault injection test (e.g., Redis down → circuit breaker activates) |
| Concurrency | At least one test for concurrent writes (e.g., duplicate short code prevention) |
| Data migration | At least one test that applies migrations and verifies schema |
| Infrastructure | Container image test (correct base, non-root user, health check) |

Test data MUST use factories (e.g., `@faker-js/faker`), not hard-coded fixtures.

#### 10.6: Implement CI/CD

- Commit pipeline workflow MUST exist and be runnable (all referenced scripts and config files exist)
- Deploy pipeline workflow MUST exist with staging deploy, smoke tests, approval gate, production deploy
- All GitHub Actions MUST be pinned to commit SHA, not tags (`@v4` is not acceptable)
- All config files referenced in CI MUST exist (`.dependency-cruiser.cjs`, vitest configs, etc.)

#### 10.7: Implement Infrastructure

- Dockerfile: multi-stage build, non-root user, health check
- docker-compose.yml: all backing services (DB, cache) with health checks
- IaC stubs: at minimum, create the Terraform module directory structure with placeholder `main.tf` files that document the required resources. Full IaC implementation is optional but the structure MUST match `docs/architecture.md`.

#### 10.8: Build Verification

Run ALL of the following and fix any failures before reporting:

```bash
pnpm install          # dependencies resolve
pnpm build            # compiles with no errors
pnpm lint             # no lint errors
pnpm test             # all tests pass
pnpm test:coverage    # coverage ≥ 90%
```

If any command fails, fix the code and re-run. Do NOT report success with failing tests.

Common pitfalls to verify before running:
- ESLint flat config (`eslint.config.js` / `eslint.config.mjs`) does NOT support `--ext` flag — use `eslint .` or `eslint src/ tests/` instead
- Every `pnpm test:*` script referenced in CI workflows MUST exist in `package.json`
- Vitest config files referenced by `--config` flags MUST exist at the specified paths
- If using a monorepo, shared packages MUST be built before dependent packages can compile

#### 10.9: Doctrine Compliance Verification

Walk through the generated `docs/tier1-checklist.md` item by item. For each item, verify the corresponding code exists. Specifically check:

- [ ] Every endpoint in the generated `AGENTS.md` has a route handler
- [ ] Every route has Zod validation at the boundary
- [ ] Every state-changing operation writes an audit log entry
- [ ] RLS is activated per-request (not just defined in SQL)
- [ ] RBAC is enforced (not just role stored — role checked before access)
- [ ] Passwords use bcrypt, not SHA-256
- [ ] OpenTelemetry is initialized and tracing works
- [ ] CI workflows reference scripts that exist in `package.json`
- [ ] Architecture test config exists and rules match `docs/architecture.md`
- [ ] All test types from `docs/testing.md` have at least one test file
- [ ] OpenAPI spec exists and matches implemented routes
- [ ] Terraform directory structure exists (at minimum placeholder `main.tf` files)
- [ ] `pnpm lint` passes with no errors (verify the lint script actually works)

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
