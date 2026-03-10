# Accessibility

## Standard

- WCAG 2.2 Level AAA: https://www.w3.org/TR/WCAG22/

Fetch the latest WCAG version when generating project docs.

Applies to: webapp

## Requirements

- All success criteria up to Level AAA MUST be met.
- Automated accessibility testing MUST run in CI.
- Manual accessibility audit MUST be documented before launch.
- Semantic HTML MUST be used over ARIA where possible.
- All interactive elements MUST be keyboard accessible.
- Color contrast MUST meet AAA ratios (7:1 normal text, 4.5:1 large text).
- Focus indicators MUST be visible and meet contrast requirements.
- Motion and animation MUST respect `prefers-reduced-motion`.
- All media MUST have captions, transcripts, and audio descriptions where applicable.

## Output Requirements

The generated accessibility doc MUST:

- List applicable WCAG AAA criteria for the project's UI components
- Specify automated testing tools for the chosen stack
- Define a manual audit checklist
- Define accessibility acceptance criteria per component type
- Include a Mermaid diagram of the accessibility testing pipeline
