# Accessibility

## Standards

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- EN 301 549 (EU legal baseline, European Accessibility Act): https://www.etsi.org/deliver/etsi_en/301500_301599/301549/

Fetch the latest WCAG version when generating project docs.

Applies to: webapp

## Conformance Model

Blanket "Level AAA" conformance is not a valid target — the W3C itself states AAA cannot be required as general policy because some AAA criteria are impossible for certain content. Instead, this doctrine defines an exact, non-negotiable criterion set with factual applicability conditions. Whether a criterion applies is determined by the project's content inventory (established during Discovery) — never by an implementing agent's judgment of effort or value. Skipping an applicable criterion requires a user-approved waiver (see Compliance Model in the root `AGENTS.md`).

### Baseline: Level A + AA — unconditional

- ALL Level A and Level AA success criteria MUST be met. No exceptions without a user-approved waiver.
- This is also the legal baseline: products serving EU users MUST meet EN 301 549 (European Accessibility Act, in force since 2025-06-28), which incorporates WCAG Level AA.

### AAA criteria that are always achievable — unconditional

The following Level AAA criteria are achievable by construction in any webapp and MUST be met:

| Criterion | Requirement |
|---|---|
| 1.3.6 Identify Purpose | Programmatically determinable purpose of UI components and regions |
| 1.4.6 Contrast (Enhanced) | 7:1 normal text, 4.5:1 large text |
| 1.4.9 Images of Text (No Exception) | Use real text, never images of text (logos exempt per the criterion itself) |
| 2.1.3 Keyboard (No Exception) | All functionality keyboard-operable |
| 2.2.4 Interruptions | Interruptions can be postponed or suppressed by the user |
| 2.3.2 Three Flashes | Nothing flashes more than three times per second |
| 2.3.3 Animation from Interactions | Respect `prefers-reduced-motion`; motion animation can be disabled |
| 2.4.8 Location | User's location within the site is indicated (e.g., breadcrumbs, active nav state) |
| 2.4.9 Link Purpose (Link Only) | Link purpose clear from link text alone |
| 2.4.10 Section Headings | Content organized with section headings |
| 2.4.13 Focus Appearance | Focus indicator meets enhanced size and contrast requirements |
| 2.5.5 Target Size (Enhanced) | Pointer targets ≥ 44×44 CSS px (inline links exempt per the criterion) |
| 2.5.6 Concurrent Input Mechanisms | Do not restrict input modality (touch, keyboard, mouse) |
| 3.2.5 Change on Request | Context changes only on explicit user request |
| 3.3.9 Accessible Authentication (Enhanced) | No cognitive function test in any authentication step |

### AAA criteria gated on content facts — conditional

Applicability of each criterion below is a fact from the Discovery content inventory. When the fact is true, the criterion is a hard MUST. When false, the criterion is recorded as N/A with the fact stated — and it re-activates automatically if the content type is later added.

| Criterion | Applies when (fact) |
|---|---|
| 1.2.6 Sign Language (Prerecorded) | Prerecorded video with speech audio exists |
| 1.2.7 Extended Audio Description (Prerecorded) | Prerecorded video exists where pauses are insufficient for audio description |
| 1.2.8 Media Alternative (Prerecorded) | Prerecorded synchronized media exists |
| 1.2.9 Audio-only (Live) | Live audio-only content exists |
| 1.4.7 Low or No Background Audio | Prerecorded speech-only audio content exists |
| 1.4.8 Visual Presentation | Blocks of text content exist (true for nearly all webapps) |
| 2.2.3 No Timing | Any functionality is time-limited (real-time events/auctions exempt per the criterion) |
| 2.2.5 Re-authenticating | Authenticated sessions can expire |
| 2.2.6 Timeouts | Inactivity timeouts can cause data loss |
| 3.1.3 Unusual Words | Content contains jargon or idioms |
| 3.1.4 Abbreviations | Content contains abbreviations |
| 3.1.5 Reading Level | Text content requires advanced reading ability |
| 3.1.6 Pronunciation | Meaning depends on pronunciation |

## Requirements

- A **conformance table** covering every WCAG A/AA/AAA success criterion MUST be generated in the project accessibility doc, with per-criterion status: `required` or `N/A (<fact>)`. Implementing agents MUST NOT mark a criterion N/A based on effort — only based on a content-inventory fact.
- Automated accessibility testing MUST run in CI and MUST fail the build on violations of automatable criteria.
- Automated testing MUST NOT be treated as sufficient — it typically catches only 30–50% of accessibility issues. Criteria requiring manual verification MUST be documented in a manual audit checklist with assigned responsibility, and a manual audit MUST be completed and documented before launch.
- Criteria requiring external resources (e.g., sign language interpretation, extended audio description production) MUST be identified during Discovery and budgeted for — they are not waivable by the implementing agent.
- Semantic HTML MUST be used over ARIA where possible; ARIA only where no native element exists.
- All interactive elements MUST be keyboard accessible with a logical tab order.
- All media MUST have captions and transcripts per the conformance table; audio descriptions where the table requires them.
- Accessibility MUST be tested with at least one screen reader flow per critical path (documented in the manual audit checklist).

## See Also

- `i18n.md` — language support, text direction (LTR/RTL)
- `testing.md` — accessibility testing in CI
- `data-privacy.md` — EU jurisdiction facts from Discovery also drive the EN 301 549 obligation

## Output Requirements

The generated accessibility doc MUST:

- Include the full A/AA/AAA conformance table with per-criterion status derived from the Discovery content inventory
- Specify automated testing tools for the chosen stack and the CI gate
- Define the manual audit checklist with assigned responsibility
- Define accessibility acceptance criteria per component type
- Include a Mermaid diagram of the accessibility testing pipeline
