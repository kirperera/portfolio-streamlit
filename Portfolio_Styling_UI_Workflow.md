# Portfolio Website — Styling & UI Workflow (Streamlit / Python)

Applies on top of `Portfolio_Build_Workflow.md`. Priority order for every decision below: **1) professional/formal first, 2) attractive second.** If a feature conflicts with the formal tone, drop the feature, not the tone.

---

## 1. Design Ground Rules

| Rule | Why |
|---|---|
| One accent colour, used sparingly | A recruiter-facing site should read as calm and deliberate, not decorative |
| No gradients, neon, drop-shadows heavier than a subtle card lift | Reads as a marketing/template site, not a technical one |
| No auto-playing motion, no bouncing, no confetti/emoji-heavy UI | Undermines the formal tone regardless of how polished the code is |
| Every "attractive" feature must have a job (organize, clarify, or speed up scanning) | Decoration without function is the thing to avoid |
| Consistent spacing and alignment everywhere | Inconsistency reads as unpolished faster than plain styling does |

"Attractive" in this plan means: precise spacing, clear hierarchy, subtle interactivity (hover states, tabs, filters), and good data visualization — not bright colours or heavy animation.

---

## 2. Visual System

### 2.1 Colour

```
Primary (headers, nav, key accents):   #0B1F3A   (deep navy)
Accent (links, active states, tags):   #0E7C86   (teal)
Ink (body text):                       #1F2937
Muted (secondary text/metadata):       #64748B
Surface:                               #FFFFFF
Surface-alt (section backgrounds):     #F5F7FA
Border:                                #E2E8F0
```

Usage ratio: ~65% surface/white, ~25% navy, ~10% teal accent. Teal never appears on more than one element type per view (e.g., only links and tags — not also buttons and headings).

### 2.2 Typography

- Headings: one clean sans-serif (e.g., **Inter** or **IBM Plex Sans**) at a slightly heavier weight (600–700).
- Body: the same family at regular weight (400), 16px, line-height 1.6.
- Monospace (for tool tags, code): **JetBrains Mono** or **Fira Code**, used only in small tag chips — never for body text.
- Maximum two font families total.

### 2.3 Spacing & Layout

- Base unit: 8px. All padding/margin values are multiples of it (8, 16, 24, 32, 48).
- Content max-width: ~880px, centered, with consistent side padding on mobile.
- Section vertical rhythm: 48–64px between major sections, 16–24px between related elements.

---

## 3. Streamlit-Specific Implementation

### 3.1 Theme (`.streamlit/config.toml`)

```toml
[theme]
base = "light"
primaryColor = "#0E7C86"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F5F7FA"
textColor = "#1F2937"
font = "sans serif"
```

### 3.2 Custom CSS (`assets/style.css`)

Inject once via `st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)` in the entrypoint. Target Streamlit's stable CSS hooks (`data-testid` attributes) rather than auto-generated class names, since those change between versions.

Cover, at minimum:
- Card component (project cards, cert cards): white background, 1px `--color-border`, 12px radius, 24px padding, subtle `box-shadow: 0 1px 3px rgba(0,0,0,0.06)`.
- Hover state on cards/links: border shifts to accent colour, 1–2px lift, 150ms transition — nothing more.
- Tag/chip style for tools and domains: small pill, `surface-alt` background, `ink` text, no colour-per-category (keeps it formal, not a rainbow).
- Section headers: consistent size, a thin accent-colour underline or left border rather than a background block.
- Sidebar/nav: navy background, white text, active item marked with the accent colour, not a full colour swap.
- Remove Streamlit's default top padding/branding elements where it opens up unnecessary whitespace, but keep the "Made with Streamlit" footer only if the platform requires it.

### 3.3 Reusable render helpers (`assets/components.py`)

Build small Python helper functions used across every page, so styling stays consistent without copy-pasted HTML:

- `section_header(title: str, subtitle: str = "")`
- `card(content_fn)` — wraps any block in the card CSS class via `st.container(border=True)` styled through CSS
- `tag_row(tags: list[str])`
- `metric_row(items: list[tuple[str, str]])` — for compact stats if ever needed (e.g., project count, cert count)

Agent should build these once in Step 2 below and reuse them in every page — never restyle inline per page.

---

## 4. Attractive-but-Formal UI Features

Each feature below is scoped to stay inside the ground rules in Section 1.

| Feature | Where | Why it fits |
|---|---|---|
| **Domain filter as pill/segmented control** (`st.pills` or styled `st.multiselect`) | Projects page | Functional interactivity, not decoration; helps a recruiter jump straight to GIS or ML work |
| **Tabs for project detail** (Overview / Tech / Links) inside a project card, using `st.tabs` | Projects page | Keeps cards compact without walls of text |
| **Skill chips grouped by category with subtle hover** | Skills page | Scannable, avoids fabricated progress bars |
| **Expand/collapse for older or secondary content** (`st.expander`) — e.g., certifications marked "Ongoing" vs completed | Education page | Keeps the page short by default, detail on demand |
| **Sticky, minimal top nav** with current page indicated by an underline/colour, not a full highlight box | All pages | Orientation without visual noise |
| **Copy-to-clipboard on email** (`st.code` with copy icon, or a styled button) | Contact/Home | Small utility touch, still formal |
| **Subtle entrance fade for section content on load** (CSS `@keyframes` opacity 0→1, ≤300ms, no movement/slide) | All pages | Feels considered without feeling flashy |
| **Consistent icon set** (e.g., Lucide/Feather-style outline icons, single colour) for contact links and section headers | All pages | Adds polish without adding colour or clutter |
| **Print-friendly / PDF-safe CSS** (`@media print`) hiding nav and buttons | All pages | Lets a recruiter print or save a page cleanly |

Explicitly excluded (fails the formal-first rule): particle backgrounds, animated gradients, cursor-follow effects, auto-scrolling carousels, confetti/celebration animations, emoji as UI icons, multi-colour tag categories, typewriter text effects.

---

## 5. Agent Workflow

Execute in order; verify visually after each step (run the app, check the affected page).

### Step 1 — Establish the design tokens
1. Write `.streamlit/config.toml` (Section 3.1).
2. Create `assets/style.css` with CSS custom properties for every colour/spacing value in Section 2, so no hex code is hardcoded elsewhere.
3. Confirm the base theme applies (background, text colour, accent colour visible on default widgets).

### Step 2 — Build reusable style components
4. Create `assets/components.py` with the helper functions in Section 3.3.
5. Write the card, tag-row, and section-header CSS classes in `style.css` and confirm each helper renders correctly on a blank test page.
6. Delete the test page once confirmed.

### Step 3 — Apply to Home
7. Style the profile header block using `section_header` and consistent spacing.
8. Style the contact row as icon + text pairs using the shared icon set (Section 4).
9. Style skill-category chips using `tag_row`.

### Step 4 — Apply to Projects
10. Wrap each project in the `card` component.
11. Add the domain pill filter (Section 4) and wire it to the existing `domain` field filter logic from the content workflow.
12. Add `st.tabs` inside each card for Overview / Tech / Links if a card's content is long enough to warrant it; otherwise keep it flat.
13. Style tool tags with `tag_row`.

### Step 5 — Apply to Skills
14. Group and style skill chips by category header, using consistent card or section spacing — no progress bars, no star ratings.

### Step 6 — Apply to Education & Certifications
15. Style the education timeline as a simple vertical list with consistent spacing, not a heavy graphic timeline component.
16. Use `st.expander` for grouping certifications/achievements/volunteering if the page gets long; keep everything visible if it doesn't.

### Step 7 — Apply to Contact
17. Style as a short, icon-led list. Add the copy-to-clipboard email touch (Section 4).

### Step 8 — Motion pass
18. Add the single entrance-fade CSS keyframe (Section 4) and apply it to top-level section containers only — not to every individual element (avoids a distracting cascade of fades).
19. Confirm no layout shift occurs during the fade (opacity-only animation).

### Step 9 — Consistency and QA pass
20. Check spacing multiples (8px base unit) are respected across every page.
21. Check the accent colour is not overused — audit each page for accent-colour element count.
22. Check contrast: body text on white/surface-alt, white text on navy, accent-on-white for links — verify each meets at least 4.5:1 for body-sized text.
23. Test hover/focus states with keyboard navigation (Tab key) — every interactive element needs a visible focus outline, not just a mouse hover state.
24. Test the print stylesheet on the Projects and Home pages.
25. View at 3 widths (mobile ~375px, tablet ~768px, desktop ~1280px) and confirm cards, nav and text wrap without breaking.

### Step 10 — Final review
26. Screenshot every page and compare against Section 1's ground rules checklist before calling styling complete.

---

## 6. Fields/Decisions the Agent Should Confirm, Not Assume

- Exact accent colour if teal (#0E7C86) isn't preferred — keep it to one accent either way.
- Icon set choice (Lucide vs Feather vs Streamlit's built-in Material icons via `:material/...:` syntax).
- Whether the entrance-fade motion is wanted at all, or whether to skip animation entirely for maximum formality.
