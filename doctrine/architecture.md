# Application Architecture

## References

- CQRS: https://martinfowler.com/bliki/CQRS.html

Applies to: all

## Requirements

### Vertical Slice Architecture

- Vertical slice architecture MUST be used as the default project structure.
- All files for a feature MUST live in the same directory/package (handler, port, adapter, tests).
- Slices MUST be independent — a change to one feature MUST NOT require changes in another feature's slice.
- Deviations from vertical slice MUST be justified in an ADR.

### CQRS (Command Query Responsibility Segregation)

- Commands (operations that change state) MUST NOT return data, except for created resource identifiers.
- Queries (operations that read state) MUST NOT mutate state, except for audit logging.
- Commands and queries MUST be separate functions/handlers — never combine both in one operation.

### Modular Monolith First

- Projects MUST start as a modular monolith with clear module boundaries.
- Each module MUST have an explicit public API — internal implementation details MUST NOT be accessible across module boundaries.
- Extraction to microservices MUST require an ADR documenting: the reason, the communication pattern, data ownership, and operational overhead.

### Dependency Rule

- Business logic MUST NOT directly import infrastructure (database drivers, HTTP clients, framework internals).
- Infrastructure dependencies MUST be injected or abstracted at the module boundary.
- Architecture tests (see `testing.md`) MUST enforce the dependency rule in CI.

### Error Handling

- Domain-specific error types MUST be used over generic language errors/exceptions.
- Errors MUST NOT be silently swallowed — every error MUST be handled, propagated, or explicitly logged.
- Errors MUST carry context: what operation failed and why.
- Error types from external dependencies MUST be translated to domain errors at the boundary.

## See Also

- `testing.md` — architecture tests enforce structural rules
- `12-factor.md` — stateless processes, backing services
- `api-design.md` — CQRS aligns with API command/query endpoints
- `documentation.md` — ADRs for architectural deviations

## Output Requirements

The generated architecture doc MUST:

- Define the vertical slice directory structure for the chosen stack
- Define the CQRS command and query separation with examples
- Define module boundaries and their public APIs
- Specify how the dependency rule is enforced (architecture test rules)
- Define the error handling strategy with domain error type examples
- Include a Mermaid diagram of the module/slice structure
