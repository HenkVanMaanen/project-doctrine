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

- Response time budgets MUST be defined with explicit targets:
  - p50 ≤ 100ms (typical API), p95 ≤ 500ms, p99 ≤ 1000ms
  - Adjust based on operation complexity (DB-heavy queries may have higher budgets, documented in the performance doc)
- Performance/load tests MUST run in CI against staging.

### Load Testing

- Load test scenarios MUST be derived from expected traffic patterns defined during discovery (concurrent users, peak RPS).
- Tests MUST cover:
  - **Sustained load** — expected normal traffic over time
  - **Spike load** — sudden traffic bursts (e.g., 10x normal)
  - **Soak testing** — extended duration to detect memory leaks and resource exhaustion
- Load test results MUST define pass/fail criteria tied to response time budgets and error rate SLOs.

### Caching

- HTTP cache headers MUST be configured per resource type:
  - Static assets: immutable with content hashing
  - API responses: `Cache-Control` with appropriate `max-age` or `no-store`
  - Reference: [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111)
- CDN MUST be used for static assets (webapp).
- Application-level caching strategy MUST be defined for frequently accessed data.
- Cache invalidation strategy MUST be documented.

## See Also

- `telemetry.md` — SLOs/SLIs, latency metrics
- `infrastructure.md` — CDN, health checks
- `ci-cd.md` — performance tests in pipeline

## Output Requirements

The generated performance doc MUST:

- Define performance budgets with specific numeric targets
- Define load test scenarios derived from discovery traffic patterns
- Specify caching strategy per resource type
- Define performance testing approach and tools
- Include CI integration for budget enforcement
