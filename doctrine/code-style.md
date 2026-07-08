# Code Style

Applies to: all

## Requirements

### Formatting

- An automated code formatter MUST be configured for the chosen stack.
- Formatting MUST be enforced in CI — builds MUST fail on unformatted code.
- Formatting MUST be applied via pre-commit hook.

### Linting

- A linter MUST be configured with the strictest available configuration. All rules MUST be enabled by default.
- Disabling a rule globally (in the lint config) requires a user-approved waiver (see Compliance Model in the root `AGENTS.md`), with the justification recorded in the config file next to the disabled rule. Implementing agents MUST NOT disable rules on their own authority.
- Suppressing a single finding inline is permitted with a comment explaining why (see `code-quality.md` for the suppression policy) — inline suppressions are visible in code review; global disables are not.
- Linting MUST be enforced in CI — builds MUST fail on lint errors.
- Lint rules MUST NOT be disabled inline without a comment explaining why.

### Conventions

- Naming conventions MUST follow the chosen language's idioms.
- File and directory structure MUST be defined in the architecture doc.
- Import ordering MUST be automated.

### Editor Config

- An `.editorconfig` file MUST be included.
- Reference: https://editorconfig.org/

### Pre-commit Hooks

Pre-commit hooks MUST run:

1. Code formatter
2. Linter
3. Secret scanner

## See Also

- `ci-cd.md` — lint and format as first pipeline stage
- `code-quality.md` — structural quality measures layered on top of linting
- `documentation.md` — commit message conventions

## Output Requirements

The generated CI/CD doc MUST include code style sections that:

- Specify formatter and linter for the chosen stack with config files
- Define pre-commit hook setup
- Include `.editorconfig` specification
- Define lint rule exception policy
