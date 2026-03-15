# Infrastructure

Applies to: all

## Requirements

### Containers

- Docker MUST be used for all deployable services.
- Dockerfiles MUST follow best practices:
  - Multi-stage builds
  - Non-root user
  - Minimal base images
  - `.dockerignore` configured
  - `HEALTHCHECK` instruction MUST be present
- Docker Compose MUST be provided for local development with all backing services (DB, cache) including health checks.

### Container Registry

- Proprietary projects MUST use a private container registry. Open source projects MAY use a public registry.
- Container images MUST be signed and verified before deployment.
- Vulnerability scanning MUST run on every image push.
- Tags MUST be immutable — overwriting existing tags MUST NOT be allowed.
- Images MUST be tagged with the git commit SHA and semantic version.

### Infrastructure as Code

- All infrastructure MUST be defined as code.
- Choose tooling appropriate for the target platform (Terraform, Pulumi, CloudFormation, etc.).
- IaC MUST be version-controlled alongside application code or in a dedicated repo.
- At minimum, the IaC directory structure MUST exist with placeholder files documenting required resources, even if full implementation is deferred.

### Vendor Lock-in

- Architectural decisions with portability implications (cloud-specific services, proprietary APIs) MUST be documented in an ADR with an exit strategy.
- Abstraction layers SHOULD be used for cloud-specific services where practical.

### Health Checks

The following endpoints MUST be implemented:

| Endpoint | Purpose | Checks |
|---|---|---|
| `/healthz` | Liveness | Process is alive |
| `/readyz` | Readiness | Service can accept traffic (dependencies reachable) |

- Health checks MUST return appropriate HTTP status codes (200 OK / 503 Service Unavailable).
- Health checks MUST NOT require authentication.
- Startup probes MUST be configured to allow for initialization time.

### Environment Parity

- Dev, staging, and production MUST use the same container images.
- Backing services MUST be the same type across environments.

### Cost Awareness

- Cost implications MUST be documented in ADRs for infrastructure decisions.
- Resource budgets per environment SHOULD be defined.
- Cost alerts SHOULD be configured for cloud-based infrastructure.

## See Also

- `12-factor.md` — config management, dev/prod parity
- `ci-cd.md` — container image building, deployment
- `disaster-recovery.md` — backup infrastructure, failover
- `telemetry.md` — health check integration with observability
- `testing.md` — infrastructure tests validate IaC
- `finops.md` — cost visibility, tagging, budget alerts

## Output Requirements

The generated architecture doc MUST:

- Define the container architecture as a Mermaid diagram
- Specify container registry setup (signing, scanning, tagging)
- Specify health check endpoints and their logic
- Define IaC tooling and directory structure
- Document vendor lock-in risks and exit strategies
- Include local development setup instructions (single command to start)
