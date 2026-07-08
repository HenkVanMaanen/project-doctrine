# AI / LLM Integration

## Standards

- OWASP Top 10 for LLM Applications: https://genai.owasp.org/llm-top-10/
- OWASP GenAI Security Project: https://genai.owasp.org/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- EU AI Act: https://artificialintelligenceact.eu/

Fetch the latest versions when generating project docs.

Applies to: all with AI/LLM features (established as a Discovery fact)

## Requirements

### Trust Boundaries

- All LLM output MUST be treated as untrusted input — the same as user input. It crosses a trust boundary on every return.
- Model input assembled from external data (user content, retrieved documents, tool results, web pages) MUST be treated as potentially adversarial: prompt injection is assumed possible whenever untrusted text reaches the model.
- System prompts MUST NOT contain secrets, credentials, or data the end user is not authorized to see — assume the full prompt can be exfiltrated.
- Untrusted content MUST be delimited/labeled distinctly from instructions in prompts, and the application MUST NOT rely on that separation as a security control — enforcement happens outside the model (see Output Handling and Agency below).

### Output Handling

- LLM output MUST NOT be executed directly: no `eval`, no direct SQL execution, no shell interpolation, no unescaped HTML rendering.
- LLM output rendered in a UI MUST be escaped or sanitized exactly like user-generated content (XSS rules apply).
- Structured output MUST be validated against a schema at the boundary; parsing failures MUST follow the standard error handling strategy (`architecture.md`), never silent acceptance.
- URLs, file paths, and identifiers produced by a model MUST pass the same validation as user-supplied values, including SSRF protection (`security.md`).

### Agency and Tool Use

- Tools exposed to a model MUST follow least privilege: each tool grants the minimum capability needed, scoped to the acting user's permissions — never a service-wide credential.
- Authorization for tool actions MUST be enforced in the tool implementation (server side), not by prompt instructions.
- Destructive or irreversible actions (delete, payment, external send) triggered via a model MUST require explicit human confirmation, or be covered by a user-approved waiver (see doctrine Compliance Model in `skills/apply-doctrine/SKILL.md`).
- Per-request loop/step limits MUST bound agentic execution (maximum tool calls per request).

### Data Protection

- PII MUST NOT be sent to third-party model providers without a documented lawful basis and a data processing agreement (see `data-privacy.md`); apply redaction or pseudonymization before the call where feasible.
- Provider data-retention and training-use settings MUST be documented; training on customer data MUST be disabled unless the user explicitly approves.
- The project's EU AI Act risk classification MUST be documented when serving EU users.

### Reliability and Cost

- Model API calls MUST have explicit timeouts, bounded retries, and a defined fallback behavior on provider outage (see `resilience.md`).
- Per-request and per-user token budgets MUST be enforced; token usage MUST be recorded as a metric and cost per request tracked (see `finops.md`).
- AI endpoints MUST have rate limits at least as strict as authentication endpoints (`security.md`).
- The model identifier MUST be pinned in configuration — never an implicit "latest".

### Evaluation and Testing

- An eval suite with a version-controlled golden dataset MUST exist for each model-backed feature, with pass thresholds defined.
- Evals MUST run in CI whenever a prompt, model version, or provider changes — a model/prompt change without a passing eval run MUST NOT be merged.
- Adversarial test cases (prompt injection attempts, jailbreak patterns, malformed output) MUST be part of the eval suite.

### Observability

- Every model call MUST be traced (span with model, latency, token counts) and logged with `traceId` — prompt/completion payloads MUST be PII-redacted before logging (`telemetry.md`, `data-privacy.md`).
- Model call failures and fallback activations MUST be observable as metrics with alerting.

## See Also

- `security.md` — input validation, SSRF, rate limiting applied to AI endpoints
- `data-privacy.md` — lawful basis, PII handling, processor agreements
- `resilience.md` — timeouts, retries, fallbacks for provider calls
- `telemetry.md` — tracing and logging requirements
- `finops.md` — token cost tracking and budgets
- `testing.md` — eval suites complement the standard test types

## Output Requirements

The generated AI/LLM doc MUST:

- Define every trust boundary where model input or output crosses into the system, with a Mermaid diagram
- Specify the output validation schema approach and sanitization points
- List every tool exposed to the model with its privilege scope and confirmation requirements
- Define the data protection posture per provider (retention, training use, DPA, redaction)
- Define eval datasets, thresholds, and the CI gate for prompt/model changes
- Define token budgets, rate limits, and fallback behavior per model-backed feature
