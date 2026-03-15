# CI/CD

Applies to: all

## Requirements

### Pipeline Time Budget

- The **commit pipeline** (pre-merge) MUST complete in under 10 minutes.
- The **deploy pipeline** (post-merge) MUST complete in under 20 minutes.
- Pipeline stages MUST be maximally parallelized — independent stages MUST run concurrently.
- If time budgets cannot be achieved, the bottleneck MUST be documented in an ADR with a remediation plan.

### Pipeline Stages

CI/CD pipelines MUST include the following stages, organized into two pipelines. Independent stages within each pipeline MUST run in parallel.

#### Commit Pipeline (pre-merge, < 10 minutes)

Runs on every pull request. Gates merge to main.

**Track A — Code Quality** (parallel):
1. **Lint & Format** — code style enforcement (see `code-style.md`)
2. **Build** — compile/bundle
3. **Security Scan** — dependency vulnerabilities + SAST

**Track B — Testing** (after build, parallel):
4. **Architecture Tests** — structural rule enforcement
5. **Unit Tests** — with coverage check (>= 90%)
6. **Integration Tests** — with testcontainers or equivalent
7. **Contract Tests** — if applicable
8. **Property-Based Tests** — invariant verification
9. **Data Migration Tests** — migration correctness and integrity
10. **Concurrency Tests** — if shared mutable state exists

#### Deploy Pipeline (post-merge, < 20 minutes)

Runs after merge to main. Gates production deployment.

**Track C — Deep Testing** (parallel):
11. **Mutation Tests** — with kill rate check (>= 90%)
12. **Fuzz Tests** — with configurable time limit

**Track D — Staging** (parallel with Track C):
13. **Build Container Image** — Docker
14. **Infrastructure Tests** — IaC validation
15. **Deploy to Staging** — automated

**Track E — Staging Validation** (after staging deploy, parallel):
16. **E2E Tests** — against staging
17. **Chaos Tests** — fault injection against staging
18. **DAST** — against staging

**Track F — Production**:
19. **Deploy to Production** — with approval gate
20. **Smoke Tests** — post-deployment critical path verification (< 1 min, triggers rollback on failure)

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
- All GitHub Actions (or equivalent CI actions) MUST be pinned to real, verifiable commit SHAs, not tags (`@v4` is not acceptable). The SHAs MUST correspond to actual published releases — do NOT fabricate placeholder SHAs.
- All config files and scripts referenced in CI workflows MUST exist and work when invoked locally.

### Pre-Commit Hooks

- Pre-commit hooks MUST be configured (e.g., Husky, `.pre-commit-config.yaml`, lefthook) to run formatting, linting, and type-checking on staged files.

## See Also

- `testing.md` — test types and coverage requirements
- `code-style.md` — formatting and linting in CI
- `security.md` — security scanning stages
- `infrastructure.md` — Docker image building
- `dora.md` — deployment frequency, lead time for changes
- `finops.md` — CI/CD infrastructure costs

## Output Requirements

The generated CI/CD doc MUST:

- Define both pipelines (commit and deploy) with all stages as Mermaid flowcharts
- Demonstrate how stages are parallelized within each pipeline to meet time budgets
- Specify the deployment strategy with rollback procedure
- Define feature flag tooling and usage policy
- Include environment promotion flow
- Specify chosen CI/CD platform configuration
