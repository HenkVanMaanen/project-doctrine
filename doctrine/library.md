# Library / Package Design

## Standards

- Semantic Versioning 2.0.0: https://semver.org/
- SLSA provenance for package registries: https://slsa.dev/

Applies to: library

## Requirements

### Public API Surface

- The public API MUST be explicitly defined (exports declared, everything else internal) — consumers MUST NOT be able to import internals.
- Every public symbol MUST have API documentation generated from source (doc comments).
- The public API surface MUST be tracked as a committed artifact (API report/declaration file) so CI can fail on unintended surface changes.

### Compatibility

- Any change to the public API surface MUST map to the correct SemVer bump: removal/behavior change → MAJOR, addition → MINOR, fix → PATCH (`versioning.md`).
- A breaking change MUST NOT ship without: a deprecation release first (deprecated symbols emit warnings and remain functional for at least one MINOR release), a migration guide, and a changelog entry marked breaking.
- Compatibility MUST be tested: the test suite MUST include tests that consume the library exactly as a consumer would (via its packaged entry points, not internal paths).
- The supported range of language/runtime versions MUST be declared in the package manifest and tested in CI (matrix builds across the supported range).

### Dependencies

- Runtime dependencies MUST be minimized — every runtime dependency is inherited by every consumer; each new one requires the intake review from `supply-chain.md`.
- Dependency version ranges MUST be as wide as safely possible (libraries pin in lockfiles for CI but publish ranges) — exact-pinning runtime deps in a published library forces conflicts on consumers.

### Publishing

- Publication MUST happen from CI only (never a developer machine), with build provenance attached (`supply-chain.md`) — use the registry's trusted publishing/OIDC mechanism where available.
- The published artifact MUST be verified post-publish: install from the registry in a clean environment and run a consumer-level smoke test.
- The deploy pipeline of `ci-cd.md` is replaced for libraries by this publish pipeline: build → pack → provenance/sign → publish → verify install. Staging/production stages, Lighthouse, and DAST do not apply.

### Distribution Hygiene

- The package MUST exclude non-distribution files (tests, CI config, internal docs) — verify the packed file list in CI.
- The package README MUST include: install command, minimal working example, supported runtime range, and a link to full docs.
- License metadata in the package manifest MUST match the LICENSE file.

## See Also

- `versioning.md` — SemVer bumps from Conventional Commits
- `api-design.md` — deprecation policy pattern (adapted from HTTP APIs to symbols)
- `supply-chain.md` — provenance, signing, dependency intake
- `dependencies.md` — SBOM, license auditing
- `documentation.md` — changelog, migration guides

## Output Requirements

The generated library doc MUST:

- Define the public API surface tracking mechanism and CI gate
- Define the deprecation and breaking-change process with timelines
- Define the CI test matrix (language/runtime versions)
- Define the publish pipeline with provenance and post-publish verification
- Specify the packed-file allowlist verification
