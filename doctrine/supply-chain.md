# Supply-Chain Security

## Standards

- SLSA (Supply-chain Levels for Software Artifacts): https://slsa.dev/
- NIST SSDF (SP 800-218): https://csrc.nist.gov/pubs/sp/800/218/final
- Sigstore: https://www.sigstore.dev/
- OpenSSF Scorecard: https://scorecard.dev/
- in-toto attestations: https://in-toto.io/

Fetch the latest versions when generating project docs.

Applies to: all

## Requirements

### Build Integrity and Provenance

- Release artifacts MUST be built by the CI platform from version-controlled sources — never from a developer machine.
- Build provenance (SLSA provenance attestation) MUST be generated for release artifacts and container images. Target SLSA Build Level 2 at minimum; Level 3 where the CI platform supports it (hardened, isolated builders).
- Builds MUST be reproducible where the stack supports it; where not, the deviation MUST be documented in the generated supply-chain doc.

### Artifact Signing

- Container images and release artifacts MUST be signed (Sigstore/cosign or the platform's equivalent) — keyless OIDC-based signing SHOULD be preferred over long-lived signing keys.
- Signatures and provenance MUST be verified before deployment; unverified artifacts MUST NOT deploy (`infrastructure.md` registry rules).
- The SBOM (`dependencies.md`) MUST be attached to release artifacts as an attestation.

### Dependency Intake

- New dependencies MUST be reviewed before adoption: maintenance activity, known vulnerabilities, and name verified against typosquatting.
- Dependency-confusion defenses MUST be configured: internal package names reserved/scoped, package manager configured to resolve internal names only from the internal registry.
- A minimum-release-age policy SHOULD be applied to automated dependency updates (e.g., no auto-merge of versions younger than 48 hours) to avoid installing freshly compromised releases.
- Install scripts of third-party packages SHOULD be disabled by default where the package manager supports it.

### CI/CD Hardening

- CI workflow tokens MUST use least-privilege permissions, declared explicitly per workflow — no default broad tokens.
- Cloud deployment credentials MUST use short-lived OIDC federation from the CI platform, not long-lived static secrets.
- Third-party CI actions/plugins MUST be pinned to verified commit SHAs (`ci-cd.md`) and treated as dependencies (reviewed at intake, updated deliberately).
- Workflows triggered by untrusted contributions MUST NOT expose secrets to untrusted code (e.g., GitHub `pull_request_target` with checkout of PR code MUST NOT be used).
- Self-hosted runners, if used, MUST be ephemeral (fresh environment per job).

### Posture Monitoring

- OpenSSF Scorecard (or equivalent) MUST run on a schedule against the repository; the score MUST be tracked over time and regressions investigated.

## See Also

- `dependencies.md` — lockfiles, vulnerability scanning, SBOM generation
- `ci-cd.md` — SHA pinning, pipeline security, secrets management
- `infrastructure.md` — image signing verification, immutable tags
- `secrets.md` — no long-lived credentials, rotation
- `code-quality.md` — CISQ findings on open-source component failures

## Output Requirements

The generated supply-chain doc MUST:

- Define the target SLSA level with the concrete CI configuration that achieves it
- Specify signing tooling and the verification gate before deployment
- Define the dependency intake checklist and dependency-confusion configuration
- Define CI token permission policy per workflow
- Specify Scorecard (or equivalent) scheduling and score tracking
