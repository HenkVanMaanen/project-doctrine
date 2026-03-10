# Telemetry & Observability

## Standard

- OpenTelemetry: https://opentelemetry.io/docs/

Applies to: all

## Requirements

### Logging

- Structured JSON logging MUST be used.
- Log levels MUST follow syslog severity ([RFC 5424](https://www.rfc-editor.org/rfc/rfc5424)).
- Every log entry MUST include: timestamp (ISO 8601), level, correlation/trace ID, service name, message.
- PII MUST NOT appear in logs.

### Metrics

- OpenTelemetry MUST be used for metrics collection.
- RED metrics (Rate, Errors, Duration) MUST be collected for all endpoints.
- USE metrics (Utilization, Saturation, Errors) MUST be collected for resources.

### Tracing

- Distributed tracing via OpenTelemetry MUST be implemented.
- All inter-service calls MUST propagate trace context ([W3C Trace Context](https://www.w3.org/TR/trace-context/)).

### SLOs/SLIs

Service Level Indicators MUST be defined for:

- Availability (e.g., % of successful requests)
- Latency (p50, p95, p99 response times)
- Error rate

Service Level Objectives MUST be set for each SLI with explicit targets.

## Output Requirements

The generated observability doc MUST:

- Define SLIs and SLOs with numeric targets
- Specify the telemetry stack (collector, backend, visualization)
- Define alerting rules derived from SLOs
- Include a Mermaid diagram of the telemetry data flow
