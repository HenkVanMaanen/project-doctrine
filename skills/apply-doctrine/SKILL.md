---
name: apply-doctrine
description: Apply the Project Doctrine to the current repository — new (greenfield) or existing. Runs Discovery, generates project docs and config from the doctrine, implements the project, and verifies compliance, fanning work out to parallel subagents at every phase. Use when the user asks to set up a project with the doctrine, generate doctrine docs, audit a codebase against the doctrine, or bring a repo into compliance.
---

# Apply Project Doctrine

This is the authoritative workflow for applying the Project Doctrine: meta-instructions for generating project-specific documentation from standardized principles, then implementing and verifying the project. The normative requirements live in the `doctrine/` files; this skill defines the process and its parallelization. Where this skill and a doctrine file conflict on a requirement, the doctrine file wins.

You are the **orchestrator**. Your job is coordination, sequencing, and verification — delegate heavy reading, generation, implementation, and auditing to subagents, launched in parallel wherever tasks are independent. Send independent subagents in a single message so they run concurrently. Do not produce code before the documentation phases are complete — docs first, then implementation.

This doctrine uses [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) keywords (MUST, SHALL, SHOULD, MAY, MUST NOT).

When referencing standards, fetch the latest version at generation time. If a referenced RFC has been superseded, use the superseding RFC instead. The URLs in doctrine files are stable fallbacks. See `doctrine/standards-versions.md` for known-good baseline versions.

## Agent-First Implementation

The generated project documentation is designed for implementation by AI agents (LLMs), not humans. This means:

- All requirements are achievable — agents can handle the full scope without scaling concerns.
- Agents MAY execute tasks in parallel using subagents or agent teams.
- Independent steps in this workflow SHOULD be parallelized across agents.
- The generated project `AGENTS.md` MUST instruct implementing agents to work in parallel where possible.
- No requirement may be softened due to perceived complexity — agents can implement comprehensive testing, full accessibility compliance, and complete observability. If a requirement genuinely cannot be met, it MUST be reported, never silently weakened (see Compliance Model).

## Compliance Model

Every requirement in this doctrine is **binary**: for any given project it is either met, waived by the user, or reported as non-compliant. There is no fourth state.

- **Requirements are verifiable.** Each requirement has a verification method: an automated test, a CI gate, an introspection query, or a named manual audit step. Generated docs MUST state how each acceptance criterion is verified.
- **Applicability is factual, not judgmental.** Whether a conditional requirement applies is determined by project facts established during Discovery (project type, multi-tenancy, content inventory, integrations) — never by an implementing agent's assessment of effort, complexity, or value. If the facts change later (e.g., video content is added to a webapp), the dependent requirements activate automatically.
- **Only the user can waive a requirement.** A waiver MUST be granted explicitly by the human user and recorded in `docs/waivers.md` with: the requirement waived, the reason, the scope, an expiry or review date, and the date granted. Generation MUST produce `docs/waivers.md` as an initially empty register.
- **ADRs are not waivers.** ADRs document decisions among doctrine-permitted options (e.g., REST vs. GraphQL, RBAC vs. ABAC). An agent-authored ADR MUST NOT be used to skip, weaken, or defer a requirement. Wherever doctrine text requires justification for a deviation, that means a user-approved waiver in `docs/waivers.md` — an ADR MAY document the context, but only the waiver grants the exception.
- **Agents MUST NOT self-exempt.** Implementing agents MUST NOT waive, reinterpret, defer, or partially implement a requirement. If a requirement cannot be met, the agent MUST report it as a failed checklist item (Phases 5.5 and 6) — visibly, never silently worked around. Faking compliance (tautological tests, stubbed verifications, placeholder values) is a worse violation than reporting the gap.

**Orchestrator duties**: put the no-self-exemption sentence in every implementation subagent prompt. Collect every "cannot comply" report and present them to the user at the end as failed items awaiting a decision (fix or waiver). Treat suspiciously convenient subagent success claims as unverified — the compliance walk (Phase 5.5) trusts evidence, not summaries.

## Locate the Doctrine Sources

Resolve `DOCTRINE_ROOT` in this order:

1. `${CLAUDE_PLUGIN_ROOT}` — when running as an installed plugin, the doctrine ships with it (`${CLAUDE_PLUGIN_ROOT}/doctrine/`).
2. The current repo, if it contains `doctrine/standards-versions.md` (you are inside the doctrine repo itself).
3. Fallback: fetch from `https://raw.githubusercontent.com/HenkVanMaanen/project-doctrine/main/` (each doctrine file). Cache fetched files in the scratchpad and pass paths to subagents.

Every subagent prompt MUST include the resolved paths (or fetched copies) of exactly the doctrine files that subagent needs — subagents do not inherit your context.

## Phase 0 — Detect Mode (inline, fast)

Determine greenfield vs. existing: a repo with no source files (only README/LICENSE/git scaffolding) is greenfield. Anything else is an existing project. For existing projects:

1. Audit the current state against all applicable doctrine files (Phase 2 audit agents).
2. Produce a gap analysis documenting what is missing or non-compliant.
3. Prioritize Tier 1 gaps (security, data-privacy, testing) for immediate remediation.
4. Create a roadmap for incremental adoption of Tier 2 requirements.
5. Generate project docs as normal, noting existing state and required changes.

## Phase 1 — Discovery (inline, blocking)

Ask the user the following with AskUserQuestion (batch the questions; apply the documented defaults for unanswered optional items). Record every answer as a **fact sheet** in `docs/discovery.md` — these facts drive requirement applicability under the Compliance Model. Subagents receive the fact sheet verbatim and MUST NOT re-interpret applicability.

### Required

These MUST be answered before generation can proceed:

- **Project type**: webapp | API | CLI
- **Tech stack**: language, framework, database
- **Target users**: audience, expected scale (concurrent users, peak requests/sec)
- **Data sensitivity**: what PII or sensitive data will be handled?
- **Infrastructure**: cloud provider, CI/CD platform, container orchestration

### Optional (defaults applied if not answered)

- **Authentication**: required? existing provider? (default: required, no existing provider)
- **Multi-tenant or single-tenant?** (default: single-tenant)
- **Open source or proprietary?** (default: proprietary)
- **Deployment targets**: regions, compliance jurisdictions (default: single region, GDPR)
- **Regulatory requirements beyond GDPR?** (e.g., PCI-DSS, HIPAA) (default: GDPR only)
- **External integrations**: third-party APIs, services (default: none)
- **Monorepo or polyrepo**: single repo or multiple? (default: monorepo)
- **Offline/PWA requirements?** (default: no)
- **Expected traffic patterns**: sustained load, peak spikes, seasonal variation (default: even load, 2x peak)
- **Content inventory (webapp)**: will the product include pre-recorded or live video, audio-only content, or media requiring captions/transcripts? (default: none) — this determines which media accessibility criteria apply (see `doctrine/accessibility.md`)
- **AI/LLM features**: will the product call LLMs or process model output? (default: no)
- **Asynchronous processing**: message queues, background jobs, event-driven flows? (default: none beyond scheduled cleanup jobs)

## Phase 2 — Parallel Research Fan-Out

Launch simultaneously (one message, all in parallel):

- **Standards agent**: for each standard referenced in `doctrine/standards-versions.md` (OWASP Top 10, WCAG, OpenAPI, etc.), fetch the latest version to ensure current guidance. If an RFC has been superseded, use the successor. If fetching fails, fall back to the baseline versions listed there.
- **Doctrine readers**: 3–4 agents, each reading a disjoint group of the applicable doctrine files (filter by project type and Discovery facts using the Doctrine Files table below) and returning a distilled requirement inventory with verification methods.
- **Audit agents (existing repos only)**: one per domain group (security+privacy, testing+ci-cd, architecture+api, observability+ops) — each audits the current codebase against its doctrine files and returns a gap list with file:line evidence.

## Phase 3 — Parallel Generation Fan-Out

When Phase 2 returns, launch one subagent per applicable output doc — each is independent:

| Output File | Source Doctrine Files |
|---|---|
| `docs/architecture.md` | architecture, 12-factor, infrastructure, cli (CLI only) |
| `docs/security.md` | security, secrets |
| `docs/accessibility.md` | accessibility (webapp only) |
| `docs/observability.md` | telemetry, dora |
| `docs/testing.md` | testing |
| `docs/api.md` | api-design (API/webapp only) |
| `docs/data-privacy.md` | data-privacy |
| `docs/ci-cd.md` | ci-cd, code-style, code-quality |
| `docs/resilience.md` | resilience |
| `docs/i18n.md` | i18n (webapp only) |
| `docs/performance.md` | performance |
| `docs/database.md` | database (if applicable) |
| `docs/versioning.md` | versioning, git-workflow |
| `docs/dependencies.md` | dependencies |
| `docs/disaster-recovery.md` | disaster-recovery |
| `docs/documentation.md` | documentation |
| `docs/finops.md` | finops |
| `docs/supply-chain.md` | supply-chain |
| `docs/incident-response.md` | incident-response |
| `docs/ai-llm.md` | ai-llm (only if AI/LLM features exist) |
| `docs/async.md` | async-messaging (only if async processing exists) |

Each generated doc MUST:

- Be concise and actionable
- Specify stack-specific tooling choices
- Contain measurable acceptance criteria
- Use RFC 2119 keywords
- Link to standards rather than repeating their content

Each generation agent receives: the fact sheet, its source doctrine file paths, the standards agent's version report, and (existing repos) the relevant gap list. Skip docs whose applicability facts are false.

In the same fan-out, also launch:

- **Config agent** — generate applicable starter config files in the project root (only those applicable to the chosen stack and project type):
  - `.editorconfig`
  - `.gitignore`
  - `Dockerfile` and `docker-compose.yml`
  - Formatter config
  - Linter config
  - Pre-commit hook config
  - PR template (`.github/pull_request_template.md` or equivalent)
  - `.env.example`
  - `CHANGELOG.md` (initial)
  - `LICENSE` — derived from the Discovery answer: [MIT](https://opensource.org/licenses/MIT) (or the user's chosen OSI-approved license) for open-source projects; a proprietary all-rights-reserved notice for proprietary projects
- **Checklist agent** — generate `docs/tier1-checklist.md`: a checklist covering all Tier 1 (non-negotiable) requirements from `security.md`, `data-privacy.md`, `testing.md`, and — when AI/LLM features exist — `ai-llm.md`. This checklist MUST be reviewed and confirmed before implementation begins.

Write `docs/waivers.md` (empty register) and `docs/discovery.md` yourself — they are trivial.

## Phase 4 — Consistency Validation (parallel checkers)

Launch 3 validator agents concurrently over the generated `docs/`:

- **(a) References & tooling**: all cross-references between docs are valid; tooling choices are consistent across docs (same test framework, same CI platform, etc.)
- **(b) Contradictions & criteria**: no contradictions between docs (e.g., performance budgets vs. testing requirements); all acceptance criteria are measurable and non-overlapping; security headers don't conflict with CDN or caching config
- **(c) Budget achievability**: CI pipeline time budgets are achievable with the defined parallelization strategy; performance budgets match the test plan

If inconsistencies are found, resolve them and document the rationale; re-validate what changed.

Then generate yourself (they encode the results of everything above):

- **Project `AGENTS.md`** in the target repo root: instructs agents to implement the project following all generated docs in `docs/`. It MUST reference each generated doc, define which tasks can be parallelized across agents (use the Phase 5 plan), instruct agents to work in parallel where tasks are independent, and define the implementation order (Tier 1 requirements first).
- **Project `CLAUDE.md`** containing only: `@AGENTS.md`

## Phase 5 — Build and Verify (maximum safe parallelism)

Implement the full project and verify it works. This is not scaffolding — it is a complete, working codebase. Every endpoint, every middleware, every test type, and every config file referenced in the generated docs MUST exist and function.

### 5.1 Foundations — single agent (do not parallelize)

Set up the project structure exactly as defined in `docs/architecture.md`:

- Initialize the project manifest with all required dependencies; install and verify they resolve
- Create the directory structure — vertical slice directories per operation named `{entity}-{operation}` (e.g., `features/link-create/`, `features/auth-login/`), not entity-grouped modules or flat horizontal directories
- Build everything required by `docs/tier1-checklist.md`: **Security** (`doctrine/security.md`): authentication, password hashing, RBAC enforcement, input validation, HTTP security headers, rate limiting, SSRF protection, audit logging, account lockout, refresh token rotation. **Data Privacy** (`doctrine/data-privacy.md`): multi-tenant RLS, GDPR erasure and export endpoints, IP anonymization with cleanup job, audit log pseudonymization. **Observability** (`doctrine/telemetry.md`): OpenTelemetry initialization, structured logging with all four required fields, health checks, traceId in error responses
- Every build/test/lint script or command referenced in CI workflows MUST work when invoked

Parallelizing shared infrastructure causes conflicts — don't.

### 5.2 Vertical slices — one agent per slice, in parallel

Build every endpoint and feature defined in the generated `AGENTS.md`. The architecture mandates one directory per operation with no cross-slice imports — this is the parallelism unit. Launch one agent per slice (or per entity group of slices), each owning ONLY its slice directory plus its tests. Do not skip phases or endpoints:

- Every endpoint MUST be implemented with authentication middleware, input validation, parameterized queries, and audit logging
- Apply all security requirements from `doctrine/security.md` to every route: RBAC enforcement, rate limiting bound to handlers, audit logging for all state-changing operations (including logout and token refresh)
- Cache invalidation MUST occur when data changes (if caching is used)
- Follow TDD for each feature: write failing test → implement → verify pass

Files touched by multiple slices (route registration, DI wiring) are integrated by you or a single integrator agent afterwards — never by two slice agents concurrently. Use worktree isolation if agents must touch shared files.

### 5.3 Cross-cutting tracks — parallel with slices

One agent each, disjoint paths:

- **OpenAPI agent**: generate a **committed** `openapi.yaml` (or `openapi.json`) in the project root documenting all implemented endpoints. Even if the framework serves the spec dynamically, the static file MUST be committed so contract tests can load it without booting the app. It MUST describe every endpoint, include request/response schemas matching the code's validation schemas, and be valid OpenAPI 3.1 (validated with a linter or parser).
- **Test-types agent**: every test type in `doctrine/testing.md` MUST have at least one working test — all 13 core types breadth-first (one file per type before deepening any), conditional types (snapshot, visual regression, load) when applicable. Tests requiring infrastructure MUST use Testcontainers — no environment variable gating. No tautological assertions, skipped tests, or empty bodies. Each type MUST use its appropriate technique (not relabeled unit tests). Test data MUST use factories with randomized data. Coverage ≥ 90% for lines, branches, functions, and statements.
- **CI/CD agent**: both pipelines from `doctrine/ci-cd.md` (commit + deploy) with all stages; SHA pinning with real verifiable SHAs; pre-commit hooks; secrets management. All config files and scripts referenced in CI MUST exist and work when invoked.
- **Infrastructure agent**: Dockerfile with multi-stage build, non-root user, and HEALTHCHECK; docker-compose.yml with all backing services and health checks; IaC directory structure matching `docs/architecture.md` (at minimum placeholder files documenting required resources).

### 5.4 Build verification — single gate agent

Run ALL of the following with the stack's idiomatic commands and fix any failures before reporting:

1. **Install dependencies** — resolve and lock all dependencies
2. **Compile / build** — full production build with zero errors
3. **Lint** — zero errors
4. **Run all tests** — full suite
5. **Coverage** — ≥ 90% for lines, branches, functions, and statements

If any command fails, dispatch parallel fix agents per failure cluster and re-run until green. Do NOT report success with failing tests. Common pitfalls: every script referenced in CI MUST work locally; all config files referenced by tools MUST exist at the specified paths; in a monorepo, shared packages MUST be built before dependent packages.

### 5.5 Doctrine compliance walk — parallel verifiers with evidence

Walk through `docs/tier1-checklist.md` item by item, fanning the checklist out in groups of ~8 items to parallel verifier agents. Each verifier MUST return evidence (file paths, command output), not assertions. Specifically check:

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
- [ ] `docs/waivers.md` exists, and every deviation from a doctrine requirement maps to a user-approved waiver entry in it — deviations without a waiver are failed items
- [ ] Lighthouse budgets gate the deploy pipeline (webapp only): Performance ≥ 90, Accessibility/Best Practices/SEO = 100, measured against a staging environment seeded with representative data volume — not an empty database

If any check fails, fix it before proceeding.

## Phase 6 — Report

Summarize:

- Total files generated (source, tests, config, docs)
- All endpoints implemented with their HTTP methods
- Test results (total tests, pass/fail, coverage percentage)
- Any deviations from the generated docs, each mapped to its user-approved waiver in `docs/waivers.md`
- Any items from the tier1-checklist that could not be implemented, reported as failed items awaiting a user decision (fix or waiver) — never silently dropped

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
| `doctrine/code-quality.md` | all |
| `doctrine/finops.md` | all |
| `doctrine/supply-chain.md` | all |
| `doctrine/incident-response.md` | all |
| `doctrine/ai-llm.md` | all with AI/LLM features |
| `doctrine/async-messaging.md` | all with async processing |

## Priority Tiers

### Tier 1 — Non-negotiable

MUST be fully addressed before any implementation begins. A Tier 1 compliance checklist MUST be generated and confirmed:

- `security.md`
- `data-privacy.md`
- `testing.md`
- `ai-llm.md` (when AI/LLM features exist — its trust-boundary, output-handling, and data-protection requirements are security requirements)

### Tier 2 — Required

MUST be addressed in project documentation:

- All remaining doctrine files

## License

Every project MUST include a `LICENSE` file matching the Discovery answer:

- **Open source** (Discovery answer "open source"): [MIT License](https://opensource.org/licenses/MIT) by default; another OSI-approved license MAY be chosen by the user.
- **Proprietary** (the default): a proprietary all-rights-reserved license notice naming the copyright holder. The MIT License MUST NOT be applied to proprietary projects.

This doctrine repository itself is MIT-licensed.
