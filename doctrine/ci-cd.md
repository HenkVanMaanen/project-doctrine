# CI/CD

Applies to: all

## Requirements

### Pipeline Time Budget

- The full CI/CD pipeline MUST complete in under 10 minutes.
- Pipeline stages MUST be parallelized where possible to meet this budget.
- If 10 minutes cannot be achieved, the bottleneck MUST be documented in an ADR with a remediation plan.

### Pipeline Stages

CI/CD pipelines MUST include these stages in order (parallelize where independent):

1. **Lint & Format** — code style enforcement (see `code-style.md`)
2. **Build** — compile/bundle
3. **Unit Tests** — with coverage check (>= 90%)
4. **Integration Tests** — with testcontainers or equivalent
5. **Security Scan** — dependency vulnerabilities + SAST
6. **Mutation Tests** — with kill rate check (>= 90%)
7. **Fuzz Tests** — with 1-minute time limit
8. **Contract Tests** — if applicable
9. **Build Container Image** — Docker
10. **Deploy to Staging** — automated
11. **E2E Tests** — against staging
12. **DAST** — against staging
13. **Deploy to Production** — with approval gate

### Deployment Strategy

- Blue/green or canary deployments MUST be used for production.
- Rollback MUST be automated and tested regularly.
- Zero-downtime deployments MUST be achieved.

### Feature Flags

- Feature flag infrastructure MUST be implemented.
- High-risk features MUST use feature flags for progressive rollout.
- Feature flags MUST support: boolean toggles, percentage-based rollouts, and user segment targeting.
- Kill switches MUST be available for critical features — disabling a flag MUST take effect immediately.
- Stale feature flags MUST be cleaned up after full rollout (track in backlog).

### Environment Promotion

- Artifacts MUST be built once and promoted across environments.
- Environment-specific config MUST be injected at deploy time, not baked into artifacts.

### Pipeline Security

- CI/CD secrets MUST be managed via the platform's secret store, never in pipeline files.
- Pipeline definitions MUST be version-controlled.

## See Also

- `testing.md` — test types and coverage requirements
- `code-style.md` — formatting and linting in CI
- `security.md` — security scanning stages
- `infrastructure.md` — Docker image building
- `dora.md` — deployment frequency, lead time for changes

## Output Requirements

The generated CI/CD doc MUST:

- Define the complete pipeline with all stages as a Mermaid flowchart
- Demonstrate how stages are parallelized to meet the 10-minute budget
- Specify the deployment strategy with rollback procedure
- Define feature flag tooling and usage policy
- Include environment promotion flow
- Specify chosen CI/CD platform configuration
