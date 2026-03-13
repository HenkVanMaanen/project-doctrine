# Testing

Applies to: all

## Requirements

### Methodology

- TDD (Test-Driven Development) MUST be followed: write failing test, implement, refactor.
- BDD (Behavior-Driven Development) MUST be used for acceptance criteria: Given/When/Then format.

### Coverage

- Code coverage MUST be >= 90%.
- Coverage MUST be enforced in CI — builds MUST fail below threshold.

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

### Architecture Tests

- Architecture tests MUST enforce structural rules as code:
  - Dependency direction (e.g., domain layer MUST NOT depend on infrastructure)
  - No circular dependencies between packages/modules
  - Layer isolation (e.g., controllers MUST NOT import repositories directly)
  - Naming conventions per architectural boundaries
- Architecture test failures MUST break the build.
- Choose tooling per stack (e.g., ArchUnit, NetArchTest, dependency-cruiser).

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

- IaC MUST be validated before apply (e.g., `terraform plan` assertions, manifest validation).
- Container images MUST be tested for: correct base image, non-root user, expected ports, health check endpoints.
- Choose tooling per stack (e.g., Terratest, conftest, kubeval).

### Concurrency Tests

- When the project has shared mutable state, concurrency tests MUST verify thread safety.
- Race condition detection MUST be enabled where the stack supports it (e.g., Go `-race`, thread sanitizer, JCStress).
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
- Factories or builders MUST be used over hard-coded fixtures.
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
