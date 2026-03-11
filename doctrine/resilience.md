# Resilience

Applies to: all

## Requirements

### Circuit Breaker

- Circuit breakers MUST be implemented for all external service calls.
- Define thresholds per dependency: failure rate, slow call rate, wait duration in open state.

### Retries

- Retries MUST use exponential backoff with jitter.
- Maximum retry count MUST be configured per dependency.
- Non-idempotent operations MUST NOT be retried.

### Bulkhead

- Resource isolation MUST be implemented to prevent cascade failures.
- Thread pools and connection pools MUST be bounded.

### Timeouts

- All external calls MUST have explicit timeouts.
- Timeout values MUST be documented and tunable via config.

### Graceful Degradation

- Critical paths MUST be identified and documented.
- Fallback behavior MUST be defined for each external dependency.
- The system MUST remain partially functional when non-critical dependencies fail.
- Cached or default responses SHOULD be served when upstream services are unavailable.

### Graceful Shutdown

- Services MUST handle SIGTERM and complete in-flight requests.
- Shutdown timeout MUST be configured.
- Services MUST deregister from load balancers before stopping.

## See Also

- `telemetry.md` — metrics and alerting for circuit breaker state
- `infrastructure.md` — health checks, container orchestration
- `api-design.md` — backpressure, rate limiting

## Output Requirements

The generated resilience doc MUST:

- Identify all external dependencies and their failure modes
- Define circuit breaker thresholds per dependency
- Define retry policies per operation type
- Map critical vs. non-critical paths in a Mermaid diagram
- Define fallback behavior for each dependency failure
- Specify graceful shutdown sequence
