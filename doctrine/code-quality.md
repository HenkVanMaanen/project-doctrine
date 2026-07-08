# Code Quality (Structural)

## Standard

- ISO/IEC 5055:2021 — Automated Source Code Quality Measures (developed by CISQ): https://www.it-cisq.org/standards/code-quality-standards/
- Common Weakness Enumeration (CWE): https://cwe.mitre.org/
- CISQ Cost of Poor Software Quality report: https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/

Applies to: all

## Rationale

CISQ's Cost of Poor Software Quality research estimates poor software quality cost the US at least $2.41 trillion in 2022, with accumulated technical debt (~$1.52 trillion) identified as the single largest obstacle to changing existing codebases, and failures from weaknesses in open-source components growing 650% year over year. ISO/IEC 5055 makes structural quality measurable: it counts severe CWE weaknesses in source code across four of the ISO/IEC 25010 quality characteristics, so weaknesses can be detected and removed in CI before they cause operational failures.

## Requirements

### Four ISO 5055 Quality Characteristics

Static analysis MUST be configured to detect weaknesses in all four ISO 5055 characteristics:

| Characteristic | Measures | Example weaknesses |
|---|---|---|
| Reliability | Fault-proneness of code under operation | Null dereference, uninitialized resources, incorrect error handling |
| Security | Exploitable weaknesses (CWE-based) | Injection, path traversal, hard-coded credentials |
| Performance Efficiency | Wasteful resource usage | Expensive operations in loops, unreleased resources, N+1 data access |
| Maintainability | Difficulty of understanding and changing code | Excessive complexity, duplication, dead code, excessive coupling |

- Static analysis MUST run in the commit pipeline (see `ci-cd.md`).
- Builds MUST fail on any critical-severity reliability or security weakness.
- Weakness counts per characteristic MUST be tracked over time; the trend MUST NOT increase release over release.

### Maintainability Limits

The following limits MUST be enforced via linter/static analysis configuration, not convention:

- Cyclomatic complexity per function MUST NOT exceed 10.
- Nesting depth MUST NOT exceed 4.
- Function length SHOULD NOT exceed 50 lines; deviations MUST be justified inline.
- Duplicated code MUST NOT exceed 3% of the codebase — duplication detection MUST run in CI.
- Dead code (unused exports, unreachable branches) MUST be detected and removed.

### Technical Debt

- Technical debt MUST be tracked explicitly: every `TODO`/`FIXME` MUST reference an issue in the tracker; orphan TODOs MUST fail lint.
- Known debt items MUST be recorded with an impact assessment (what change they block or slow down).
- A fixed share of ongoing capacity (RECOMMENDED: ~20%) SHOULD be allocated to debt remediation rather than deferring it to dedicated "cleanup" phases.

### Enforcement

- Quality gates MUST be enforced in CI and MUST NOT be bypassable by configuration local to a change (no threshold lowering, no blanket suppressions).
- Suppressing an individual finding MUST require an inline justification comment, consistent with the lint exception policy in `code-style.md`.

## See Also

- `code-style.md` — formatter, linter strictness, exception policy
- `ci-cd.md` — static analysis as a commit pipeline stage
- `security.md` — SAST, OWASP; overlaps with the ISO 5055 security characteristic
- `testing.md` — mutation testing as a complementary quality signal
- `dependencies.md` — supply chain weaknesses, vulnerability scanning, SBOM
- `dora.md` — structural quality drives change failure rate and rework rate

## Output Requirements

The generated CI/CD doc MUST include a structural quality section that:

- Specifies stack-appropriate static analysis tooling mapped to each of the four ISO 5055 characteristics
- Defines the severity gate (which findings fail the build)
- Encodes the maintainability limits (complexity, nesting, duplication) in the linter configuration
- Defines the technical debt tracking process and the TODO-must-link-to-issue lint rule
