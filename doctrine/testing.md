# Testing

Applies to: all

## Requirements

### Methodology

- TDD (Test-Driven Development) MUST be followed: write failing test, implement, refactor.
- BDD (Behavior-Driven Development) MUST be used for acceptance criteria: Given/When/Then format.

### Coverage

- Code coverage MUST be >= 90% for lines, branches, functions, and statements.
- Coverage MUST be enforced in CI — builds MUST fail below threshold.
- Use the appropriate coverage tool for the stack.

### Test Types

All of the following MUST be implemented where applicable:

| Type | Scope | Requirement |
|---|---|---|
| Unit | Individual functions/methods | MUST cover all business logic |
| Integration | Component interactions | MUST cover all integration points |
| End-to-end | Full user flows | MUST cover critical paths |
| Snapshot | UI component output | MUST be used for UI components (webapp) |
| Contract | API consumer/provider | MUST be used for inter-service APIs |
| Property-based | Invariant verification | MUST cover core domain logic |
| Mutation | Test quality validation | MUST achieve >= 90% mutation kill rate |
| Fuzz | Unexpected input handling | MUST run in CI with 1-minute time limit |
| Architecture | Structural rules enforcement | MUST enforce dependency direction and layer constraints |
| Visual regression | Screenshot comparison | SHOULD be used for UI components (webapp) |
| Smoke | Post-deployment verification | MUST run after every production deployment |
| Chaos/fault injection | Resilience under failure | MUST run in staging; MUST NOT run in production without ADR |
| Infrastructure | IaC validation | MUST validate IaC before apply |
| Concurrency | Race conditions, thread safety | MUST be used when shared mutable state exists |
| Data migration | Migration correctness | MUST verify schema and data integrity |

### Test Anti-Patterns

The following patterns MUST NOT appear in any test file:

- Tautological assertions (e.g., asserting a literal `true` is true, or any assertion that cannot fail)
- Skipped tests or tests gated behind environment variables
- Empty test bodies, `// TODO` placeholders, or tests that only log output without asserting

Each test type MUST use the technique appropriate to that type. A unit test relabeled as "concurrency" is not a concurrency test. A test that reads SQL file text is not a migration test. A test that validates a YAML schema is not a contract test.

### Test Implementation Requirements

| Test Type | What It MUST Do | What It MUST NOT Do |
|---|---|---|
| Unit | Test services and middleware with mocked dependencies | — |
| Integration | Use Testcontainers to start PostgreSQL and Redis, run migrations, test auth flows and CRUD against the real database. Every test MUST make real SQL queries and assert on real query results | Mock the database, or skip when no DB is available |
| E2E | Use Testcontainers for DB/Redis, boot the app, execute a full flow: register → login → create resource → verify. Assert on response status and body | Mock any infrastructure, or skip conditionally |
| Contract | Use Testcontainers for DB/Redis, boot the app, load the **committed** `openapi.yaml` static file from disk (NOT the app's live spec endpoint), make real HTTP requests, validate response status codes, headers, and body shapes match the spec | Only validate YAML/JSON structure of the spec file, or just check endpoints return non-404 |
| Property-based | Use a property-based testing library to test domain invariants with random inputs | Use hand-picked inputs — that's a unit test |
| Mutation | Invoke a real mutation testing tool with **actual code mutation** and assert on the exit code or mutation score. The tool MUST generate real mutants and kill them — `--dryRun`, `--list`, or any mode that skips actual mutation execution is NOT acceptable. A config file alone is NOT sufficient. The mutation score threshold MUST be ≥ 80% | Only create a config file, verify the tool is installed, or run in dry-run/list mode without generating real mutants |
| Fuzz | Use the property-based testing library with arbitrary/random input generation to throw malformed data at parsers and validators | Use a small set of hand-crafted edge cases |
| Architecture | Verify module dependency rules via a tool or by scanning imports. MUST fail if boundaries are crossed | Silently pass if the tool is unavailable |
| Smoke | Boot the real app and verify critical paths respond correctly | — |
| Chaos | Simulate real infrastructure failure: kill a Redis connection, inject latency, or use Testcontainers to stop a container. App MUST degrade gracefully | Only mock a module to throw |
| Concurrency | Make concurrent requests to a real running app using actual parallelism | Generate values in a loop and check uniqueness |
| Data migration | Use Testcontainers to start empty PostgreSQL, run migrations, query `information_schema` and `pg_policies` to verify tables, types, indexes, and RLS policies | Only read SQL file content, or skip when no DB is available |
| Infrastructure | Verify Dockerfile structure (multi-stage, non-root, HEALTHCHECK), docker-compose services, and Terraform files | — |

### Testcontainers

Tests requiring infrastructure (DB, Redis) MUST use Testcontainers. Do NOT gate tests behind environment variables — if the test exists, it MUST run as part of the standard test command.

### Implementation Order

Create one test file per type first (breadth), then deepen coverage. Do NOT write 20+ unit tests before creating the other 12 test types — every test type MUST have a file before any type gets additional tests.

### Architecture Tests

- Architecture tests MUST enforce structural rules as code:
  - Dependency direction (e.g., domain layer MUST NOT depend on infrastructure)
  - No circular dependencies between packages/modules
  - Layer isolation (e.g., controllers MUST NOT import repositories directly)
  - Naming conventions per architectural boundaries
- Architecture test failures MUST break the build.
- Choose tooling appropriate for the stack.

### Smoke Tests

- A smoke test suite MUST run immediately after every production deployment.
- Smoke tests MUST verify critical paths only (authentication, main page/endpoint, core API operations).
- Smoke tests MUST complete in under 1 minute.
- Smoke test failure MUST trigger automated rollback.

### Chaos/Fault Injection Tests

- Chaos tests MUST be run against staging environments to validate resilience patterns.
- Tests MUST simulate: dependency failures, network latency, pod/container termination, resource exhaustion.
- Results MUST verify that circuit breakers, fallbacks, and graceful degradation work as documented in `resilience.md`.
- Chaos testing in production MUST NOT occur without an explicit ADR and approval.

### Infrastructure Tests

- IaC MUST be validated before apply.
- Container images MUST be tested for: correct base image, non-root user, expected ports, health check endpoints.
- Choose tooling appropriate for the stack.

### Concurrency Tests

- When the project has shared mutable state, concurrency tests MUST verify thread safety.
- Race condition detection MUST be enabled where the stack supports it.
- Deadlock detection SHOULD be included in integration tests.

### Data Migration Tests

- Every database migration MUST have a corresponding test that:
  - Applies the migration to a known state
  - Asserts the expected schema changes
  - Verifies data integrity after transformation
- Migration tests MUST run in CI before deployment.

### Test Isolation

- Tests MUST be independent and order-insensitive.
- External dependencies MUST be mocked/stubbed at unit level.
- Integration tests MAY use testcontainers or equivalent.

### Test Data

- Test data MUST NOT contain real user data.
- Factories or builders MUST be used with randomized data, not hard-coded fixtures.
- Test data MUST be isolated per test suite and cleaned up after execution.

## See Also

- `ci-cd.md` — test stages in commit and deploy pipelines
- `performance.md` — load testing
- `security.md` — SAST/DAST scanning
- `resilience.md` — patterns validated by chaos tests
- `infrastructure.md` — IaC validated by infrastructure tests
- `database.md` — migrations validated by data migration tests
- `dora.md` — change failure rate metric
- `architecture.md` — dependency rule enforced by architecture tests

## Output Requirements

The generated testing doc MUST:

- Specify testing tools for the chosen stack (one per test type)
- Define the test directory structure
- Include CI pipeline integration for all test types
- Define architecture test rules for the project's layer structure
- Define smoke test suite with critical paths
- Define chaos test scenarios mapped to resilience requirements
- Define mutation testing configuration and targets
- Define fuzzing targets and time budgets
- Include a Mermaid diagram of the test pyramid
