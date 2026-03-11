# Git Workflow

Applies to: all

## Requirements

### Branching

- Trunk-based development MUST be used.
- The `main` branch MUST always be deployable.
- Feature branches MUST be short-lived (< 1 day preferred, < 3 days maximum).
- Branch naming: `<type>/<short-description>` (e.g., `feat/user-auth`, `fix/login-redirect`).

### Commits

- All commits MUST follow Conventional Commits (see `documentation.md`).
- Each commit MUST be atomic — one logical change per commit.

### Pull Requests

- All changes MUST go through a pull request.
- PRs MUST be limited to 400 lines changed (excluding generated code and lockfiles). Larger PRs MUST be split.
- PRs MUST pass all CI checks before merge.
- PRs MUST be squash-merged to keep `main` history clean.

### Branch Protection

`main` MUST be protected with:

- Required CI pass
- No force pushes
- No direct commits
- Signed commits SHOULD be required

## See Also

- `documentation.md` — Conventional Commits format, ADRs
- `versioning.md` — version bumps from commits
- `ci-cd.md` — CI checks required for PR merge
- `dora.md` — deployment frequency, lead time

## Output Requirements

The generated versioning doc MUST include git workflow sections that:

- Define branch protection rules for the chosen platform
- Define PR template
- Define merge strategy
