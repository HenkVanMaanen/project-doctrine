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

All of the following MUST be implemented:

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

### Test Isolation

- Tests MUST be independent and order-insensitive.
- External dependencies MUST be mocked/stubbed at unit level.
- Integration tests MAY use testcontainers or equivalent.

### Test Data

- Test data MUST NOT contain real user data.
- Factories or builders MUST be used over hard-coded fixtures.
- Test data MUST be isolated per test suite and cleaned up after execution.

## See Also

- `ci-cd.md` — test stages in pipeline, 10-minute budget
- `performance.md` — load testing
- `security.md` — SAST/DAST scanning
- `dora.md` — change failure rate metric

## Output Requirements

The generated testing doc MUST:

- Specify testing tools for the chosen stack (one per test type)
- Define the test directory structure
- Include CI pipeline integration for all test types
- Define mutation testing configuration and targets
- Define fuzzing targets and time budgets
- Include a Mermaid diagram of the test pyramid
