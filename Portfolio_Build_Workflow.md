# Portfolio Website — Build Workflow (Streamlit / Python)

Content source: `cv_1_2.pdf` (Iman Perera). No content outside the CV is invented. Placeholders are marked `[FILL: ...]` only where the CV is missing something the layout needs.

---

## 1. Stack

| Layer | Choice |
|---|---|
| Framework | Streamlit (`st.Page` / `st.navigation`, current multipage API) |
| Language | Python 3.11+ |
| Data viz | Plotly (skills/timeline charts) |
| Maps | `pydeck` or `folium` + `streamlit-folium` (for the flood-zone GIS project) |
| Styling | Streamlit theme via `.streamlit/config.toml` + one `assets/style.css` injected with `st.markdown(..., unsafe_allow_html=True)` |
| Content | Structured Python dataclasses in `data/content.py` — single source of truth, not hardcoded in page files |
| Deployment | Streamlit Community Cloud (same as existing site) |

No JS framework, no separate frontend build step — everything renders through Streamlit.

---

## 2. File Structure

```
portfolio/
├── streamlit_app.py            # entrypoint: st.navigation router + global CSS/theme
├── requirements.txt
├── .streamlit/
│   └── config.toml             # theme colors, fonts
├── assets/
│   ├── style.css
│   └── profile.jpg             # [FILL: headshot file]
├── data/
│   └── content.py              # ALL CV content lives here as typed structures
└── pages_content/
    ├── home.py
    ├── projects.py
    ├── skills.py
    ├── education.py
    └── contact.py
```

Each file in `pages_content/` exposes one function, e.g. `def render():`, called by the `st.Page` callable in `streamlit_app.py`. This keeps content (`data/content.py`) separate from layout (`pages_content/*.py`), so updating the CV later means editing one file.

---

## 3. Content Model (`data/content.py`)

Populate directly from the CV — do not add sections the CV doesn't have (no testimonials, no availability banner, no soft "call to action" copy).

```python
from dataclasses import dataclass, field

@dataclass
class Profile:
    name: str = "Iman Perera"
    title: str = "Intern – Data Science & Machine Learning"
    location: str = "Colombo, Sri Lanka"
    email: str = "kimanrandilaperera@gmail.com"
    phone: str = "+94 76 292 5854"
    linkedin: str = "[FILL: LinkedIn URL]"
    github: str = "kirperera"
    summary: str = (
        "Motivated Information Systems undergraduate with a strong focus on "
        "Data Analytics, Machine Learning, and Geographic Information Systems. "
        "Passionate about discovering actionable insights from environmental "
        "and infrastructural data to build predictive, data-driven systems. "
        "Proficient in Python, SQL, and Power BI, with hands-on experience in "
        "machine learning classification and modern frontend frameworks."
    )

@dataclass
class Education:
    degree: str
    institution: str
    period: str

EDUCATION = [
    Education("BSc (Hons) in Information Systems", "Sabaragamuwa University of Sri Lanka", "Expected 2028"),
    Education("Advanced Level (Physical Science Stream)", "Rajapaksa Central College, Weeraketiya", "2019–2022"),
]

SKILLS = {
    "Programming Languages": ["Python", "R", "C", "HTML", "CSS", "Java", "JavaScript"],
    "Frameworks & Libraries": ["Pandas", "Matplotlib", "NumPy", "PyTorch", "React.js", "Next.js", "Tailwind CSS"],
    "Tools & Technologies": ["Excel", "Tableau", "Power BI", "Jupyter Notebook", "Google Earth Engine",
                              "Jira", "Figma", "PyCharm", "WebStorm", "Notion", "PowerPoint", "Git"],
    "Databases": ["MySQL", "PostgreSQL", "PostGIS"],
    "Soft Skills": ["Critical Thinking", "Analytical Thinking & Problem-Solving",
                     "Strategic Planning", "Adaptability & Flexibility"],
}

@dataclass
class Project:
    title: str
    role: str
    period: str
    tools: list[str]
    points: list[str]
    domain: list[str]          # for filtering: analytics, ml, gis, software
    repo_url: str = ""
    demo_url: str = ""

PROJECTS = [
    Project(
        title="Lanka Geo — Flood Zone Detection System (Phase 01)",
        role="Team Lead, Backend Developer, ML Model",
        period="Feb 2026 – Aug 2026",
        tools=["Google Earth Engine", "Machine Learning", "Node.js", "Python"],
        points=[
            "Built an intelligent web application to detect and map flood zones using satellite imagery.",
            "Contributed to ML classification (Random Forest) and thresholding logic to distinguish water from land masses.",
            "Designed the system architecture and integrated the ML backend with a responsive frontend for visualization.",
        ],
        domain=["gis", "ml", "software"],
        repo_url="[FILL: repo link]",
        demo_url="[FILL: demo link]",
    ),
    Project(
        title="Unt — Automated Market Intelligence Dashboard",
        role="Developer",
        period="Aug 2026 – Present",
        tools=["Python", "Pandas", "scikit-learn", "PostgreSQL", "Power BI"],
        points=[
            "Built an automated Python ETL pipeline to ingest daily Colombo Stock Exchange equity data and Central Bank macroeconomic indicators into a normalized PostgreSQL database.",
            "Built a time-series forecasting engine in Python to model 30-day stock price trends against macroeconomic variables.",
        ],
        domain=["analytics", "ml"],
        repo_url="[FILL: repo link]",
        demo_url="[FILL: demo link]",
    ),
]

@dataclass
class Achievement:
    title: str
    detail: str

ACHIEVEMENTS = [
    Achievement("Innovate with Ballerina 2025", "Coding challenge organized by IEEE Student Branch, University of Moratuwa and WSO2."),
    Achievement("SLIOT Challenge 2026", "IoT challenge organized by University of Moratuwa and SLT Mobitel."),
]

@dataclass
class Certification:
    title: str
    issuer: str
    status: str  # e.g. "Ongoing" or ""

CERTIFICATIONS = [
    Certification("Geographic Information Systems", "UC Davis", "Ongoing"),
    Certification("Power BI Data Analyst Professional Certificate", "Microsoft", "Ongoing"),
    Certification("Machine Learning Engineering for Production", "DeepLearning.AI", "Ongoing"),
    Certification("Programming for Everybody (Getting Started with Python)", "", ""),
    Certification("Getting Started with BigQuery GIS for Data Analysts", "", ""),
]

@dataclass
class Volunteering:
    role: str
    org: str
    period: str

VOLUNTEERING = [
    Volunteering("Technical Team Member", "WIE Day, IEEE Student Branch", "July 2026"),
    Volunteering("Team Member", "Hope 2.0 — technology education for school students", "2025–26"),
    Volunteering("Attendee", "Project Management Workshop, IEEE Young Professionals Sri Lanka", "January 2026"),
]
```

References from the CV are personal contact details for named third parties — do not publish them on the site; keep "References available on request" or omit the section entirely.

---

## 4. Page Plan

| Page | Content | Source fields |
|---|---|---|
| **Home** | Name, title, one-paragraph summary, contact row (email, phone, location, GitHub, LinkedIn), skill category chips | `Profile`, `SKILLS` keys only |
| **Projects** | Card per project: title, role, period, tools, bullet points, domain tags, repo/demo links; filter by domain | `PROJECTS` |
| **Skills** | Grouped list by category, exactly as categorized in the CV — no invented proficiency percentages | `SKILLS` |
| **Education & Certifications** | Degree timeline, certifications (with status), achievements, volunteering | `EDUCATION`, `CERTIFICATIONS`, `ACHIEVEMENTS`, `VOLUNTEERING` |
| **Contact** | Email, phone, location, GitHub, LinkedIn — plain links, no form | `Profile` |

No hero animation, no "availability" banner, no testimonials section — none of these are on the CV.

---

## 5. Design Tokens (`.streamlit/config.toml`)

```toml
[theme]
base = "light"
primaryColor = "#0E7C86"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F5F7FA"
textColor = "#1F2937"
font = "sans serif"
```

`assets/style.css` adds: consistent card style (border, radius, padding) for project cards, max content width (~900px, centered), and heading spacing. Inject once in `streamlit_app.py`:

```python
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
```

---

## 6. Agent Build Workflow

Execute in this order. Each step should be verified (app runs, no errors) before moving to the next.

### Step 1 — Scaffold
1. Create the file structure in Section 2.
2. Write `requirements.txt`: `streamlit`, `pandas`, `plotly`, `pydeck` (or `folium` + `streamlit-folium`).
3. Write `.streamlit/config.toml` with the tokens in Section 5.
4. Confirm `streamlit run streamlit_app.py` starts with an empty shell page.

### Step 2 — Content layer
5. Write `data/content.py` exactly as in Section 3, using only CV-sourced text. Mark any missing field `[FILL: ...]` — do not fabricate.
6. Add a short `if __name__ == "__main__":` self-check in `content.py` that prints counts (e.g., `len(PROJECTS)`, `len(SKILLS)`) to confirm the data loads without error.

### Step 3 — Router
7. In `streamlit_app.py`, define pages with `st.Page` pointing at each `pages_content/*.py` module's `render()` function, and wire them with `st.navigation`.
8. Inject `assets/style.css`.
9. Set `st.set_page_config(page_title=f"{PROFILE.name} — Portfolio", layout="centered")`.

### Step 4 — Home page
10. Render `Profile.name`, `Profile.title`, `Profile.summary`.
11. Render a contact row (email as `mailto:`, GitHub link, LinkedIn link, location, phone).
12. Render skill category names only (chips), each linking (anchor or page-switch) to the full Skills page.

### Step 5 — Projects page
13. Render each `Project` as a card: title, role + period, tool tags, bullet points, and repo/demo buttons (`st.link_button`, hidden if URL is a `[FILL: ...]` placeholder).
14. Add a domain filter using `st.pills` or `st.multiselect` over the `domain` field (`analytics`, `ml`, `gis`, `software`).
15. For the GIS project (`Lanka Geo`), add a static or placeholder map component using `pydeck`/`folium` if imagery/geojson is available; otherwise show the project card without a live map rather than fabricating data.

### Step 6 — Skills page
16. Render `SKILLS` as grouped lists (category header + tag row), in the exact category order from the CV. Do not add star ratings or percentage bars — the CV gives no basis for scoring proficiency.

### Step 7 — Education & Certifications page
17. Render `EDUCATION` as a simple two-row timeline.
18. Render `CERTIFICATIONS` with issuer and status badge ("Ongoing" where applicable).
19. Render `ACHIEVEMENTS` and `VOLUNTEERING` as compact lists.

### Step 8 — Contact page
20. Render `Profile` contact fields as plain links/text. No contact form (nothing in the CV requires one; add only if requested later).

### Step 9 — QA pass
21. Check every page renders with zero unhandled `[FILL: ...]` visible in final content (agent should flag these back to the user, not hide or invent values).
22. Confirm navigation labels match page titles, and the browser tab title is correct.
23. Run on a narrow viewport (Streamlit's default responsive layout) to confirm cards and text wrap correctly.
24. Remove unused imports/dead code; run `python -m py_compile` on all files.

### Step 10 — Deploy
25. Push to GitHub, connect to Streamlit Community Cloud (same as the existing site), set `streamlit_app.py` as the entrypoint, confirm `requirements.txt` installs cleanly.

---

## 7. Fields the Agent Must Ask For (not invent)

- LinkedIn URL
- Repository and live-demo URLs for both projects
- Headshot image, if one is wanted on Home
- Flood-zone project map data (GeoJSON/imagery), if a live map is wanted on the Projects page

Everything else required for the build is already in Section 3.
