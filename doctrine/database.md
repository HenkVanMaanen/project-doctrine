# Database

Applies to: all projects with persistence

## Requirements

### Migrations

- All schema changes MUST be managed through versioned migrations.
- Migrations MUST be forward-only in production (no down migrations).
- Each migration MUST be idempotent.
- Migration tooling MUST be chosen per stack and run automatically on deployment.
- Migration file naming MUST use a consistent convention (e.g., `V001__create_users.sql`, `001_initial_schema.up.sql`, or framework-default naming).
- Idempotent migrations MUST use `IF NOT EXISTS` / `IF EXISTS` guards for DDL operations where the database supports it.

### Schema Versioning

- Schema versions MUST be tracked in the database.
- Migrations MUST be applied automatically during deployment.

### Breaking Changes

- Backward-compatible schema changes MUST be preferred.
- Breaking changes MUST use the expand-and-contract pattern:
  1. Expand: add new column/table alongside old
  2. Migrate: backfill data, update application to use new schema
  3. Contract: remove old column/table in a subsequent deployment
- Breaking schema changes MUST be split across multiple deployments.

### Connection Management

- Database connection pools MUST be bounded (maximum connections configured, not unlimited).
- Connection pool size MUST be tunable via configuration (environment variable or config file).
- The application MUST fail fast at startup if the database is unreachable, not silently retry indefinitely.
- Query timeouts MUST be configured per-connection or per-statement to prevent long-running queries from blocking the pool.

### Data Seeding

- Seed data for development/testing MUST be version-controlled.
- Seed data MUST NOT contain real user data.
- Seed data MUST use factories or builders with randomized data (same approach as test data — see `testing.md`).

## See Also

- `disaster-recovery.md` — database backup, restoration, recovery drills
- `data-privacy.md` — data classification, retention, erasure
- `ci-cd.md` — migration execution in pipeline
- `testing.md` — data migration tests verify schema and data integrity

## Output Requirements

The generated database doc MUST:

- Specify migration tooling for the chosen stack
- Define naming conventions for migration files
- Document the expand-and-contract strategy with an example
- Define seed data approach
