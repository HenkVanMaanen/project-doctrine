# Project Doctrine

Meta-instructions for LLMs to generate project-specific documentation from standardized principles. This repository is a strict doctrine: it produces docs and starter config files that guide implementation — the doctrine itself contains no code.

**The complete, authoritative workflow lives in [`skills/apply-doctrine/SKILL.md`](skills/apply-doctrine/SKILL.md).** If you are reading this file directly (as a coding agent pointed at this repository, rather than via the installed `/apply-doctrine` skill), read that file in full and execute it. It defines:

- The Compliance Model (binary requirements, user-only waivers, no agent self-exemption)
- Discovery questions and the fact sheet that drives requirement applicability
- The phase-by-phase workflow with parallel subagent orchestration (research → generation → validation → implementation → compliance walk → report)
- The doctrine file applicability table and priority tiers
- The licensing rule derived from Discovery

The normative requirements live in [`doctrine/`](doctrine/) — one file per domain, using RFC 2119 keywords. `doctrine/standards-versions.md` holds known-good baseline versions of all referenced standards; fetch the latest versions at generation time.
