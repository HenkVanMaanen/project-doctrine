# Documentation

## Standards

- ADRs: https://adr.github.io/
- Keep a Changelog: https://keepachangelog.com/en/1.1.0/
- Conventional Commits: https://www.conventionalcommits.org/en/v1.0.0/
- C4 Model: https://c4model.com/

Applies to: all

## Requirements

### Architecture Decision Records

- An ADR MUST be created for every significant technical decision.
- ADRs MUST follow the format: Title, Status, Date, Context, Decision, Consequences.
- ADRs MUST be stored in `docs/adr/` with sequential numbering (`0001-*.md`).
- ADR status MUST use one of: `Proposed`, `Accepted`, `Superseded`, `Deprecated`, `Rejected`.
- Status transitions MUST include a date and rationale.
- Superseded ADRs MUST link to their successor (e.g., "Superseded by ADR-0005").
- ADRs MUST NOT be deleted.

### Changelog

- A `CHANGELOG.md` MUST be maintained following Keep a Changelog format.
- Changelog entries MUST be linked to version tags.
- Changelog generation SHOULD be automated from Conventional Commits.

### Commit Messages

- All commits MUST follow Conventional Commits format.
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`.
- Breaking changes MUST use the `BREAKING CHANGE:` footer or `!` after the type.

### Diagrams

- Architecture diagrams MUST follow the C4 model (Context, Container, Component).
- Diagrams MUST be written in Mermaid and stored alongside docs.
- A dependency graph MUST be generated and kept current.
- Diagrams MUST be updated when architecture changes.

### API Documentation

- API docs MUST be generated from OpenAPI spec or GraphQL schema.
- API docs MUST be browsable in non-production environments.

## See Also

- `git-workflow.md` — commit conventions, PR process
- `versioning.md` — release process, version bumps
- `api-design.md` — OpenAPI/GraphQL spec as doc source

## Output Requirements

The generated documentation doc MUST:

- Define the ADR template with all status values
- Specify diagram tooling setup (Mermaid)
- Define changelog automation approach
- Include commit message format with examples
- Include an initial C4 Context diagram in Mermaid
