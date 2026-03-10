# Versioning

## Standard

- Semantic Versioning 2.0.0: https://semver.org/

Applies to: all

## Requirements

- All projects MUST follow Semantic Versioning: `MAJOR.MINOR.PATCH`.
- Version bumps MUST be derived from Conventional Commits:
  - `fix:` → PATCH
  - `feat:` → MINOR
  - `BREAKING CHANGE:` or `!` → MAJOR
- Version bumps SHOULD be automated in CI/CD.
- Git tags MUST be created for each release.
- Pre-release versions MUST use SemVer pre-release format (e.g., `1.0.0-beta.1`).

## Output Requirements

The generated versioning doc MUST:

- Define the versioning automation tool for the chosen stack
- Define the release process
- Map Conventional Commits types to version bumps
