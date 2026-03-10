# API Design

## Standards

- OpenAPI 3.1: https://spec.openapis.org/oas/v3.1.0
- HTTP Semantics: [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)
- Problem Details: [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457)
- JSON:API: https://jsonapi.org/format/ (if REST)
- GraphQL: https://spec.graphql.org/ (if GraphQL)

Applies to: API, webapp

## Requirements

### Protocol

- Choose REST or GraphQL per project. Document the rationale in an ADR.
- REST APIs MUST follow HTTP semantics (RFC 9110).

### Specification

- REST APIs MUST have an OpenAPI 3.1 specification.
- The spec MUST be the source of truth — code MUST be generated from or validated against it.
- GraphQL APIs MUST have a schema-first design.

### Versioning

- API versioning strategy MUST be defined and documented in an ADR.
- Choose URL path, header, or content negotiation versioning.
- Reference: [RFC 9110 Section 12](https://www.rfc-editor.org/rfc/rfc9110#section-12) for content negotiation.

### Error Handling

- Errors MUST use RFC 9457 Problem Details format (JSON).
- Error responses MUST NOT leak internal details (stack traces, internal IDs, SQL).

### Rate Limiting

- Rate limiting MUST be implemented for all public endpoints.
- Rate limit headers MUST follow [IETF draft-ietf-httpapi-ratelimit-headers](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/).
- Rate limit tiers MUST be defined per client type.

### Pagination

- Collection endpoints MUST support pagination.
- Use cursor-based pagination for large datasets; offset-based is acceptable for small, stable datasets.

## Output Requirements

The generated API doc MUST:

- Specify REST or GraphQL with ADR rationale
- Define versioning strategy
- Include error response format with examples
- Define rate limiting tiers
- Reference the OpenAPI spec or GraphQL schema location
- Include a Mermaid sequence diagram for key API flows
