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

- Initialize the project manifest (`package.json`, `Cargo.toml`, `go.mod`, `*.csproj`, etc.) with all required dependencies
- Create the directory structure from the architecture doc — use vertical slice directories (e.g., `features/links/`), not flat `routes/` + `services/` directories
- Install dependencies and verify they resolve (e.g., `pnpm install`, `cargo build`, `go mod tidy`, `dotnet restore`)
- Every build/test/lint script or command referenced in CI workflows MUST work when invoked

#### 10.2: Implement Tier 1 Foundations

Build everything required by the Tier 1 checklist (`docs/tier1-checklist.md`). Every item on the checklist MUST have corresponding code:

**Security:**
- Auth middleware: JWT validation (RS256) + API key validation (HMAC-SHA256), or session-based auth with secure cookies (SameSite, HttpOnly, Secure) — choose the pattern appropriate for the project type (API = JWT, webapp with SSR = sessions). For API keys: HMAC-SHA256 means using a keyed hash (e.g., `HmacSHA256(key, secret)`) — NOT a plain `SHA-256(key)` digest. The HMAC secret MUST come from configuration, not be hardcoded
- Password hashing: use the strongest algorithm available in your stack — bcrypt (cost ≥ 12), argon2id (preferred for Rust/Go/C#), or scrypt. NEVER use SHA-256, MD5, or plain hashing
- RBAC middleware: enforce role checks on protected routes before allowing access. Storing roles in the database is NOT enforcement — the role MUST be checked in middleware/guard/filter/policy before allowing the request through. DELETE and admin operations MUST require admin or owner role, not just any authenticated user
- Input validation: validate all input at every route boundary using the stack's idiomatic validation library (e.g., Zod for TypeScript, validator for Go, FluentValidation for C#, serde + custom validation for Rust). Path parameters, query parameters, and request bodies MUST all be validated
- HTTP security headers: set HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy via middleware or framework configuration
- Rate limiting: per-endpoint limits as defined in `docs/security.md`. Rate limiters MUST be actually applied to route handlers (via middleware, decorator, annotation, or attribute) — defining a rate limit config without binding it to endpoints has no effect
- SSRF protection: URL validation that blocks private IP ranges, localhost, cloud metadata endpoints
- Audit logging: a working service that writes to the `audit_log` table on every state-changing operation — this explicitly includes login, logout, register, token refresh, and all CRUD operations. Do NOT forget logout
- Account lockout: lock accounts after N consecutive failed login attempts
- Refresh token rotation: issue new refresh token on every refresh, invalidate the old one, detect reuse (family invalidation)

**Data Privacy:**
- Multi-tenant RLS: `SET LOCAL app.current_tenant_id` MUST be called at the start of every request — not just WHERE clause filtering
- GDPR erasure endpoint: implement the full erasure pipeline (hard delete PII, anonymize audit logs)
- GDPR export endpoint: return all user data as JSON/CSV
- IP anonymization: hash IPs before storage. Implement an automated cleanup job (cron, scheduled task, or background worker) that purges IP hashes and click/analytics data older than the retention period
- Audit log pseudonymization: emails stored as `sha256(email + AUDIT_SALT)`, never plaintext

**Observability:**
- OpenTelemetry: install and configure the OTel SDK for your language (e.g., `@opentelemetry/sdk-node`, `opentelemetry-rust`, `go.opentelemetry.io/otel`, `OpenTelemetry.Extensions.Hosting`). OTel MUST initialize unconditionally (not skip when an env var is missing) — in development/test it can export to a no-op or console exporter, but the SDK MUST be active so traceId/spanId are always available
- Structured logging: use the idiomatic structured logger for your stack (e.g., pino for Node.js, tracing for Rust, zerolog/zap for Go, Serilog for C#). Every log entry MUST include ALL FOUR of these fields: `traceId`, `spanId`, `tenantId`, and `service`. The logger MUST extract trace context from OpenTelemetry's active span — do NOT just log static fields. `tenantId` MUST be injected into the logging context per-request (e.g., via MDC, LogContext, context vars, or span attributes) — defining an enricher/processor class without registering it in the logging pipeline is not sufficient. For unauthenticated requests, log `tenantId` as empty string, not omit it
- Health checks: `/healthz` (liveness) and `/readyz` (readiness with DB+Redis checks)
- `traceId` in error responses: every RFC 9457 Problem Details response MUST include a trace/request ID

#### 10.3: Implement All Features

Build every endpoint and feature defined in the generated `AGENTS.md`. Do not skip phases or endpoints:

- Every endpoint listed in the generated `AGENTS.md` MUST be implemented
- Every route MUST have authentication middleware (or equivalent guard/filter/extractor)
- Every state-changing route MUST call the audit logging service — this includes token refresh, not just CRUD operations. Logout MUST also write an audit entry
- Every route that accepts user input MUST validate at the boundary using the stack's validation library — this includes path parameters (e.g., validate `:id` as UUID)
- Every database query MUST use parameterized queries
- Cache invalidation MUST occur when data changes (if caching is used)
- Rate limiting MUST be per-endpoint (e.g., stricter limits on auth endpoints), not just a single global limit. The rate limiter config MUST be bound to actual route handlers — defining rate limit policies/configs without attaching them to endpoints is dead code
- RBAC roles on endpoints must be meaningful — `requireRole('member')` on a DELETE is effectively no protection since member is the lowest role

Follow TDD for each feature: write failing test → implement → verify pass.

#### 10.4: Generate OpenAPI Spec

Generate a **committed** `openapi.yaml` (or `openapi.json`) in the project root that documents all implemented endpoints. Even if the framework can serve the spec dynamically (e.g., SpringDoc, FastAPI `/docs`), a static file MUST be committed to the repository so contract tests can load it without booting the app's spec endpoint. This spec MUST:

- Describe every endpoint from the generated `AGENTS.md`
- Include request/response schemas matching the validation schemas used in the code
- Be valid OpenAPI 3.1 (validate with a linter or parser)
- Be used by contract tests to verify routes match the spec

#### 10.5: Implement All Test Types

Every test type defined in `docs/testing.md` MUST have at least one working test. "Working" means the test exercises real logic and would catch real bugs — not just `expect(true).toBe(true)` or mocks asserting against other mocks.

**Do not fake test types.** A unit test relabeled as "concurrency" is not a concurrency test. A test that reads SQL file text is not a migration test. A test that validates a YAML schema is not a contract test. Each test type MUST use the technique appropriate to that type.

**Do not stub test bodies.** Every test MUST contain real assertions that verify behavior. The following patterns are NOT acceptable and MUST NOT appear in any test file:
- `expect(true).toBe(true)`, `assert!(true)`, `Assert.True(true)`, or any tautological assertion in any language
- `describe.skip`, `it.skip`, `#[ignore]`, `[Fact(Skip=...)]`, `t.Skip()`, or any mechanism that conditionally skips tests based on environment variables
- Empty test bodies or `// TODO` placeholders
- Tests that only log output without asserting anything

Tests that require infrastructure (DB, Redis) MUST use Testcontainers (available for all major languages: testcontainers for Node.js, testcontainers-rs for Rust, testcontainers-go for Go, Testcontainers.* for C#/Java) to spin up ephemeral containers. Do NOT gate tests behind environment variables like `INTEGRATION_TESTS=1` — if the test exists, it MUST run as part of the standard test command or a named test script. Use Testcontainers so tests are self-contained and run anywhere without external services.

**Implementation order for tests:** Create one test file per type first (breadth), then deepen coverage. Do NOT write 20+ unit tests before creating the other 12 test types — every test type MUST have a file before any type gets additional tests. This prevents running out of budget before reaching all types.

| Test Type | What It MUST Do | What It MUST NOT Do |
|---|---|---|
| Unit | Test services and middleware with mocked dependencies | — |
| Integration | Use Testcontainers to start PostgreSQL and Redis, run migrations, then test auth flows, CRUD operations, and GDPR erasure/export against the real database. Every test MUST make real SQL queries and assert on real query results | Mock the database, or skip when no DB is available — that's a stub, not an integration test |
| E2E | Use Testcontainers for DB/Redis, boot the app, then execute a full flow: register → login → create resource → verify. Every step MUST assert on response status and body | Mock any infrastructure, or skip the test conditionally |
| Contract | Use Testcontainers for DB/Redis, boot the app, load the **committed** `openapi.yaml` static file from disk (NOT the app's live `/api-docs` or `/openapi.json` endpoint), make real HTTP requests to live endpoints, and validate that response status codes, headers, and body shapes match the spec. The test MUST: (1) start the real application, (2) load the committed OpenAPI spec file, (3) make actual HTTP requests, (4) compare responses against the OpenAPI schema definitions. Use a library like `openapi-response-validator` or manually validate response JSON against the spec's JSON Schema | Only validate the YAML/JSON structure of the spec file itself — that tests the spec, not the implementation. Do NOT just assert the file contains certain strings or check that endpoints return non-404 |
| Property-based | Use a property-based testing library (fast-check, proptest, FsCheck, jqwik, gopter) to test domain invariants with random inputs | Use hand-picked inputs — that's a unit test |
| Mutation | Configure and run a mutation testing tool (Stryker, cargo-mutants, go-mutesting, Stryker.NET, PITest). The test MUST either: (a) invoke the mutation tool programmatically or via shell command and assert on the exit code or score, OR (b) create a dedicated test/script that the CI pipeline runs. A config file alone is NOT sufficient — the tool MUST be invoked and verified to produce output. The mutation score threshold MUST be defined. Do NOT write manual "mutant" functions — use the real mutation tool | Only create a config file without verifying the tool runs. Do NOT write tests that merely assert a config file exists or is valid JSON/YAML — that is not mutation testing |
| Fuzz | Use the property-based testing library with arbitrary/random input generation to throw malformed data at parsers and validators | Use a small set of hand-crafted edge cases — that's a unit test |
| Architecture | Verify module dependency rules are not violated — either via a tool (dependency-cruiser, go-arch-lint, ArchUnit, etc.) or by scanning imports in source files. The test MUST fail if architectural boundaries are crossed | Silently pass if the tool is unavailable |
| Smoke | Boot the real app (or hit a deployed URL) and verify critical paths respond correctly | — |
| Chaos | Simulate real infrastructure failure: kill a Redis connection mid-request, inject network latency, or use Testcontainers to stop a container. The app MUST degrade gracefully (e.g., serve from DB when cache is down) | Only mock a module to throw — that's a unit test with extra steps |
| Concurrency | Make concurrent requests to a real running app (or use concurrent DB transactions) to verify that race conditions are handled. Use actual parallelism (goroutines, tokio::spawn, Task.WhenAll, Promise.all) with real calls | Generate values in a loop and check uniqueness — that's a unit test |
| Data migration | Use Testcontainers to start an empty PostgreSQL instance, run all migration files, then query `information_schema` and `pg_policies` to verify tables exist, columns have correct types, indexes are present, and RLS policies are active. Every assertion MUST query the real database | Only read SQL file content and check for keywords, or skip when no DB is available |
| Infrastructure | Verify Dockerfile structure (multi-stage, non-root, HEALTHCHECK), docker-compose services, and Terraform files | — |

Test data MUST use factories or builders with randomized data (e.g., `@faker-js/faker`, `fake` crate, `go-faker`, `Bogus` for C#), not hard-coded fixtures.

Code coverage MUST be configured with a threshold of 90% for lines, branches, functions, and statements. Use the appropriate coverage tool for your stack (e.g., vitest/c8/istanbul for TypeScript, tarpaulin/llvm-cov for Rust, go test -cover for Go, dotnet-coverage for C#, JaCoCo for Java).

#### 10.6: Implement CI/CD

- Commit pipeline workflow MUST exist and be runnable (all referenced scripts and config files exist)
- Deploy pipeline workflow MUST exist with staging deploy, smoke tests, approval gate, production deploy
- All GitHub Actions MUST be pinned to real, verifiable commit SHAs, not tags (`@v4` is not acceptable). The SHAs MUST correspond to actual published releases of the action — do NOT fabricate placeholder SHAs like `@a1b2c3d4...`. Look up the real SHA for each action's release tag (e.g., `actions/checkout@v4` → find the real commit SHA for v4)
- All config files and scripts referenced in CI MUST exist and work when invoked

#### 10.7: Implement Infrastructure

- Dockerfile: multi-stage build, non-root user, health check
- docker-compose.yml: all backing services (DB, cache) with health checks
- IaC stubs: at minimum, create the Terraform module directory structure with placeholder `main.tf` files that document the required resources. Full IaC implementation is optional but the structure MUST match `docs/architecture.md`.

#### 10.8: Build Verification

Run the equivalent of ALL the following for your stack and fix any failures before reporting:

```
# Install dependencies
pnpm install / cargo build / go mod tidy / dotnet restore

# Compile / build
pnpm build / cargo build --release / go build ./... / dotnet build

# Lint (zero errors)
pnpm lint / cargo clippy -- -D warnings / golangci-lint run / dotnet format --verify-no-changes

# Run all tests
pnpm test / cargo test / go test ./... / dotnet test

# Coverage ≥ 90%
pnpm test:coverage / cargo tarpaulin / go test -cover / dotnet test --collect:"XPlat Code Coverage"
```

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
- [ ] All 13 test types have at least one test file: unit, integration, e2e, contract, property-based, mutation, fuzz, architecture, smoke, chaos, concurrency, data migration, infrastructure
- [ ] Mutation test actually invokes the mutation tool (not just checks config exists)
- [ ] Contract test makes real HTTP requests and validates responses against OpenAPI schema (not just checks YAML structure)
- [ ] Every log line includes `traceId`, `spanId`, `tenantId`, and `service` — verify all four fields are present, not just traceId/spanId
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
