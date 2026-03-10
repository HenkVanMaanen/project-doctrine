# CI/CD

Applies to: all

## Requirements

### Pipeline Stages

CI/CD pipelines MUST include these stages in order:

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

### Environment Promotion

- Artifacts MUST be built once and promoted across environments.
- Environment-specific config MUST be injected at deploy time, not baked into artifacts.

### Pipeline Security

- CI/CD secrets MUST be managed via the platform's secret store, never in pipeline files.
- Pipeline definitions MUST be version-controlled.

## Output Requirements

The generated CI/CD doc MUST:

- Define the complete pipeline with all stages as a Mermaid flowchart
- Specify the deployment strategy with rollback procedure
- Include environment promotion flow
- Specify chosen CI/CD platform configuration
