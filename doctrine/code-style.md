# Code Style

Applies to: all

## Requirements

### Formatting

- An automated code formatter MUST be configured for the chosen stack.
- Formatting MUST be enforced in CI — builds MUST fail on unformatted code.
- Formatting MUST be applied via pre-commit hook.

### Linting

- A linter MUST be configured with strict rules.
- Linting MUST be enforced in CI.
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
- `documentation.md` — commit message conventions

## Output Requirements

The generated CI/CD doc MUST include code style sections that:

- Specify formatter and linter for the chosen stack with config files
- Define pre-commit hook setup
- Include `.editorconfig` specification
- Define lint rule exception policy
