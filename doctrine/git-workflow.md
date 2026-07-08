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
- PRs MUST be limited to 400 lines changed (excluding generated code and lockfiles) and SHOULD stay under 200. Larger PRs MUST be split. Code review research (Google engineering practices, SmartBear/Cisco study) shows defect detection effectiveness drops sharply beyond ~400 changed lines and review turnaround grows superlinearly with size.
- AI-generated changes MUST follow the same size limits — the DORA 2024 report found AI assistance tends to inflate batch size, which measurably reduces delivery stability.
- PRs MUST pass all CI checks before merge.
- PRs MUST be squash-merged to keep `main` history clean.

### Code Review

- Every PR MUST receive a first review response within one business day; small PRs SHOULD be reviewed within hours. Slow review turnaround is a leading cause of long change lead time (`dora.md`).
- Reviewers MUST review the change itself, not rubber-stamp — a review with no comments on a non-trivial change SHOULD state what was checked.
- AI-generated code MUST be reviewed to the same standard as human-written code.

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
- `dora.md` — deployment frequency, lead time, batch size and stability

## Output Requirements

The generated versioning doc MUST include git workflow sections that:

- Define branch protection rules for the chosen platform
- Define PR template
- Define merge strategy
