# Performance

## Standards

- Core Web Vitals: https://web.dev/articles/vitals
- HTTP Caching: [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111)

Applies to: all (Core Web Vitals for webapp only)

## Requirements

### Web Performance (webapp)

- Core Web Vitals MUST meet "good" thresholds:
  - LCP <= 2.5s
  - INP <= 200ms
  - CLS <= 0.1
- JavaScript bundle size budgets MUST be defined and enforced in CI.
- Critical rendering path MUST be optimized.

### API Performance

- Response time budgets MUST be defined:
  - p50 target
  - p95 target
  - p99 target
- Performance/load tests MUST run in CI against staging.

### Caching

- HTTP cache headers MUST be configured per resource type:
  - Static assets: immutable with content hashing
  - API responses: `Cache-Control` with appropriate `max-age` or `no-store`
  - Reference: [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111)
- CDN MUST be used for static assets (webapp).
- Application-level caching strategy MUST be defined for frequently accessed data.
- Cache invalidation strategy MUST be documented.

## Output Requirements

The generated performance doc MUST:

- Define performance budgets with specific numeric targets
- Specify caching strategy per resource type
- Define performance testing approach and tools
- Include CI integration for budget enforcement
