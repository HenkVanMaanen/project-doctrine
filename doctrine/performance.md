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

### Lighthouse Budgets (webapp)

- Lighthouse audits MUST run in the deploy pipeline (Track E in `ci-cd.md`) against a production build served from the staging environment.
- Category score budgets MUST be enforced as failing gates:
  - Performance ≥ 90
  - Accessibility = 100
  - Best Practices = 100
  - SEO = 100
- Scores MUST be taken as the median of at least 3 runs with Lighthouse's default throttling — a single run MUST NOT gate (variance).
- **Measurement validity**: the environment MUST be seeded with a representative data volume derived from the Discovery scale answers, using the seed factories from `database.md`. Running Lighthouse against an empty or near-empty database is NOT a valid measurement — list, table, dashboard, and search pages MUST be measured with realistic row counts, with pagination active. The seeded volume MUST be stated in the generated performance doc.
- Budgets apply to every critical-path page: at minimum the landing page, authentication, the main list/dashboard, and the main detail view.
- A Lighthouse Accessibility score of 100 is necessary but NOT sufficient for `accessibility.md` compliance — automated tooling covers only a fraction of the criteria; the manual audit still applies.

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

- `testing.md` — load/performance test type requirements
- `telemetry.md` — SLOs/SLIs, latency metrics
- `infrastructure.md` — CDN, health checks
- `ci-cd.md` — load tests in deploy pipeline (Track E)

## Output Requirements

The generated performance doc MUST:

- Define performance budgets with specific numeric targets, including the Lighthouse category budgets and the pages they gate (webapp)
- State the seeded data volume used for Lighthouse and load test measurements
- Define load test scenarios derived from discovery traffic patterns
- Specify caching strategy per resource type
- Define performance testing approach and tools
- Include CI integration for budget enforcement
