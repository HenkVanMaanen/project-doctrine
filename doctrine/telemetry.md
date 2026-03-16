# Telemetry & Observability

## Standard

- OpenTelemetry: https://opentelemetry.io/docs/

Applies to: all

## Requirements

### Logging

- Structured JSON logging MUST be used via the stack's idiomatic structured logger.
- Log levels MUST follow syslog severity ([RFC 5424](https://www.rfc-editor.org/rfc/rfc5424)).
- Every log entry MUST include ALL FOUR of these fields: `traceId`, `spanId`, `tenantId`, and `service`. The logger MUST extract trace context from OpenTelemetry's active span — do NOT log static placeholder values.
- `tenantId` MUST be injected into the logging context per-request — defining an enricher/processor class without registering it in the logging pipeline is not sufficient.
- **IMPORTANT**: For unauthenticated requests (login, register, health checks, public endpoints), `tenantId` MUST be logged as an explicit empty string `""`, NOT omitted and NOT null. The field MUST always be present in every log entry regardless of authentication state. This is the most commonly missed requirement — verify it explicitly.
- PII MUST NOT appear in logs.

### Metrics

- OpenTelemetry MUST be used for metrics collection.
- RED metrics (Rate, Errors, Duration) MUST be collected for all endpoints.
- USE metrics (Utilization, Saturation, Errors) MUST be collected for resources.

### Tracing

- Distributed tracing via OpenTelemetry MUST be implemented.
- OpenTelemetry MUST initialize unconditionally (not skip when an env var is missing) — in development/test it can export to a no-op or console exporter, but the SDK MUST be active so traceId/spanId are always available.
- OpenTelemetry SDK MUST initialize **before** any framework or application code is imported. In languages where import order matters (Node.js/TypeScript, Python), the OTel setup module MUST be the first import in the entry point. In languages with explicit initialization (Go, Java, C#, Rust), OTel MUST be initialized before the framework starts accepting requests. This ensures auto-instrumentation hooks are installed before the modules they instrument are loaded.
- All inter-service calls MUST propagate trace context ([W3C Trace Context](https://www.w3.org/TR/trace-context/)).
- Every RFC 9457 Problem Details error response MUST include a `traceId` field.

### SLOs/SLIs

Service Level Indicators MUST be defined for:

- Availability (e.g., % of successful requests)
- Latency (p50, p95, p99 response times)
- Error rate

Service Level Objectives MUST be set for each SLI with explicit targets.

### Alerting

- Alerts MUST be derived from SLOs.
- Alert when SLO burn rate indicates the error budget will be exhausted — use multi-window, multi-burn-rate alerting.
- Every alert MUST have a documented runbook.

### Meta-Monitoring

- The telemetry pipeline itself (collector, backend) SHOULD have a health check via a separate, simple monitoring path that does not depend on the primary telemetry stack.
- Telemetry pipeline failures SHOULD trigger alerts through an independent channel (e.g., basic uptime check, email).

## See Also

- `performance.md` — response time budgets, load testing
- `infrastructure.md` — health check endpoints
- `security.md` — audit logging (distinct from operational logging)
- `disaster-recovery.md` — alerting on recovery test failures
- `dora.md` — delivery performance metrics

## Output Requirements

The generated observability doc MUST:

- Define SLIs and SLOs with numeric targets
- Specify the telemetry stack (collector, backend, visualization)
- Define alerting rules derived from SLOs with burn rate thresholds
- Define meta-monitoring approach
- Include a Mermaid diagram of the telemetry data flow
