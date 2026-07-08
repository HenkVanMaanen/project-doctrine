---
name: apply-doctrine
description: Apply the Project Doctrine to the current repository — new (greenfield) or existing. Runs Discovery, generates project docs and config from the doctrine, implements the project, and verifies compliance, fanning work out to parallel subagents at every phase. Use when the user asks to set up a project with the doctrine, generate doctrine docs, audit a codebase against the doctrine, or bring a repo into compliance.
---

# Apply Project Doctrine

You are the **orchestrator**. Your job is coordination, sequencing, and verification — delegate all heavy reading, generation, implementation, and auditing to subagents, launched in parallel wherever tasks are independent. Send independent subagents in a single message so they run concurrently.

The authoritative workflow is the doctrine repo's `AGENTS.md` (Steps 1–10) plus the files in `doctrine/`. This skill does not restate their content — it tells you how to execute them fast. Where this skill and the doctrine text conflict, the doctrine wins.

## Locate the doctrine sources

Resolve `DOCTRINE_ROOT` in this order:

1. `${CLAUDE_PLUGIN_ROOT}` — when running as an installed plugin, the doctrine ships with it (`${CLAUDE_PLUGIN_ROOT}/doctrine/`, `${CLAUDE_PLUGIN_ROOT}/AGENTS.md`).
2. The current repo, if it contains `doctrine/standards-versions.md` (you are inside the doctrine repo itself).
3. Fallback: fetch from `https://raw.githubusercontent.com/HenkVanMaanen/project-doctrine/main/` (AGENTS.md and each doctrine file). Cache fetched files in the scratchpad and pass paths to subagents.

Every subagent prompt MUST include the resolved paths (or fetched copies) of exactly the doctrine files that subagent needs — subagents do not inherit your context.

## Phase 0 — Detect mode (inline, fast)

Determine greenfield vs. existing: a repo with no source files (only README/LICENSE/git scaffolding) is greenfield. Anything else is an existing project — the doctrine's "Existing Projects" section applies, and an audit phase is inserted before generation.

## Phase 1 — Discovery (inline, blocking)

Ask the user the Discovery questions from `AGENTS.md` Step 1 with AskUserQuestion (batch them; apply documented defaults for unanswered optional items). Record every answer as a **fact sheet** — these facts drive requirement applicability under the Compliance Model, so write them to `docs/discovery.md` in the target repo. Do not let subagents re-interpret applicability later; they receive the fact sheet verbatim.

## Phase 2 — Parallel research fan-out

Launch simultaneously (one message, all background):

- **Standards agent**: verify/fetch latest versions of all standards in `doctrine/standards-versions.md`; report any superseded RFCs or new standard versions.
- **Doctrine readers**: 3–4 agents, each reading a disjoint group of the applicable doctrine files (filter by project type and Discovery facts) and returning a distilled requirement inventory with verification methods.
- **Audit agents (existing repos only)**: one per domain group (security+privacy, testing+ci-cd, architecture+api, observability+ops) — each audits the current codebase against its doctrine files and returns a gap list with file:line evidence.

## Phase 3 — Parallel generation fan-out

When Phase 2 returns, launch one subagent per output in `AGENTS.md` Step 4's table (each doc is independent), plus:

- one agent for all starter config files (Step 5),
- one agent for `docs/tier1-checklist.md` (Step 6) — it must fold in `ai-llm.md` items when AI features exist,
- `docs/waivers.md` (empty register) and `docs/discovery.md` — write these yourself, they are trivial.

Each generation agent receives: the fact sheet, its source doctrine file paths, the standards agent's version report, and (existing repos) the relevant gap list. Skip docs whose applicability facts are false (e.g., no `docs/i18n.md` for an API-only project).

## Phase 4 — Consistency validation (parallel checkers)

Launch 3 validator agents concurrently over the generated `docs/`: (a) cross-references and tooling consistency, (b) contradictions and overlapping acceptance criteria, (c) budget achievability (CI time budgets vs. pipeline definition, performance budgets vs. test plan). Fix findings yourself or dispatch fix agents; re-validate what changed. Then generate the project `AGENTS.md` and `CLAUDE.md` (Steps 8–9) yourself — they must encode the parallelization plan below for implementing agents.

## Phase 5 — Implementation (maximum safe parallelism)

Follow `AGENTS.md` Step 10, parallelized as follows:

1. **Foundations first, single agent** (10.1–10.2): project skeleton, shared infrastructure (auth middleware, logging/OTel bootstrap, DB setup, migrations). Parallelizing this causes conflicts — don't.
2. **Vertical slices in parallel** (10.3): the architecture mandates one directory per operation with no cross-slice imports — this is the parallelism unit. Launch one agent per slice (or per entity group of slices), each owning ONLY its slice directory plus its tests. Files touched by multiple slices (route registration, DI wiring) are integrated by you or a single integrator agent afterwards — never by two slice agents concurrently. Use worktree isolation if agents must touch shared files.
3. **Cross-cutting tracks in parallel with slices**: one agent each for OpenAPI spec (10.4), CI/CD workflows (10.6), infrastructure files (10.7), and the breadth-first test-type files (10.5) — each owns disjoint paths.
4. **Verification gate** (10.8): single agent runs install/build/lint/test/coverage; dispatch parallel fix agents per failure cluster; re-run until green. Never report success with failures.
5. **Compliance walk** (10.9): fan out the checklist in groups of ~8 items to parallel verifier agents; each must return evidence (file paths, command output), not assertions. Re-fix and re-verify failures.

## Compliance Model — orchestrator duties

- Subagents MUST NOT waive, reinterpret, defer, or fake any requirement. Put this sentence in every implementation subagent prompt.
- Collect every "cannot comply" report; present them to the user at the end as failed items awaiting a decision (fix or waiver). Only the user can waive; record approved waivers in `docs/waivers.md`.
- Treat suspiciously convenient subagent success claims as unverified — the compliance walk (Phase 5.5) trusts evidence, not summaries.

## Report

Finish with the Step 10.10 report: files generated, endpoints, test results and coverage, deviations mapped to waivers, and unresolved failed items.
