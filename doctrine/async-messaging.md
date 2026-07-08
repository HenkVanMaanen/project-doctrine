# Asynchronous Processing & Event-Driven Architecture

## Standards

- W3C Trace Context: https://www.w3.org/TR/trace-context/
- CloudEvents: https://cloudevents.io/ (if events cross service boundaries)

Applies to: all with asynchronous processing — message queues, event-driven flows, or background jobs (established as a Discovery fact). Scheduled cleanup jobs required elsewhere in this doctrine (e.g., `data-privacy.md`) MUST follow the Background Jobs section below.

## Requirements

### Delivery Semantics

- Consumers MUST assume at-least-once delivery: every consumer MUST be idempotent, using an idempotency key or deduplication store — never rely on exactly-once claims from the broker.
- Ordering assumptions MUST be explicit: define per-key ordering requirements where they exist; global ordering MUST NOT be assumed.

### Publishing (Outbox Pattern)

- A database state change and its corresponding event publish MUST be atomic. Dual writes (write to DB, then separately publish) MUST NOT be used — use a transactional outbox (event written to an outbox table in the same transaction, relayed asynchronously) or equivalent (change data capture).
- Events MUST be published after the owning transaction commits, never before.

### Failure Handling

- Every queue/subscription MUST have a dead-letter queue (DLQ).
- Message processing failures MUST retry with exponential backoff and jitter; after a bounded number of attempts the message MUST go to the DLQ — poison messages MUST NOT block the queue.
- DLQ depth MUST be monitored with alerting, and a documented replay procedure MUST exist.

### Event Schema Evolution

- Event schemas MUST be versioned and committed to the repository (schema registry or schema files).
- Schema changes MUST be backward compatible for existing consumers; breaking changes MUST follow expand-and-contract (`database.md` pattern applied to events).
- Contract tests MUST validate published events against the committed schemas (`testing.md`).

### Background Jobs

- Every scheduled job MUST be: idempotent, locked against concurrent double-execution (distributed lock or single-runner guarantee), and observable — last-run timestamp and outcome MUST be exported as a metric with an alert on missed or failed runs.
- Job schedules MUST be defined in code/config under version control, not configured by hand.

### Workers

- Workers MUST implement graceful shutdown: on SIGTERM, stop consuming, finish or nack in-flight messages within the shutdown timeout (`resilience.md`).
- Worker concurrency and prefetch MUST be bounded and tunable via configuration.
- Queue depth and consumer lag MUST be exported as metrics with alerting thresholds.

### Tracing

- Trace context MUST propagate through messages (W3C Trace Context in message headers/metadata) so a request can be traced across async hops (`telemetry.md`).

### Testing

- Integration tests MUST use a real broker via Testcontainers (`testing.md`) — never a mocked broker for integration-level verification.
- Chaos tests MUST kill a consumer mid-processing and verify no message loss and no duplicate side effects after restart.
- Concurrency tests MUST verify idempotency under parallel redelivery of the same message.

## See Also

- `architecture.md` — CQRS commands often become async operations
- `database.md` — outbox table migrations, expand-and-contract
- `resilience.md` — retries, backoff, graceful shutdown
- `telemetry.md` — trace propagation, queue metrics
- `data-privacy.md` — scheduled IP/analytics cleanup job follows the Background Jobs rules
- `testing.md` — Testcontainers, chaos, concurrency test types

## Output Requirements

The generated async doc MUST:

- Inventory every queue, topic, event type, and scheduled job with its delivery semantics
- Define the outbox implementation and relay mechanism
- Define retry/backoff/DLQ policy per queue with alert thresholds
- Define the event schema versioning and compatibility policy
- Include a Mermaid diagram of message flows across services/workers
- Specify broker tooling and the Testcontainers setup for tests
