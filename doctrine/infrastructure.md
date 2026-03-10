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
- Docker Compose MUST be provided for local development.

### Infrastructure as Code

- All infrastructure MUST be defined as code.
- Choose tooling appropriate for the target platform (Terraform, Pulumi, CloudFormation, etc.).
- IaC MUST be version-controlled alongside application code or in a dedicated repo.

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

## Output Requirements

The generated architecture doc MUST:

- Define the container architecture as a Mermaid diagram
- Specify health check endpoints and their logic
- Define IaC tooling and directory structure
- Include local development setup instructions (single command to start)
