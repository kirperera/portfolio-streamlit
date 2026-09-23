from dataclasses import dataclass, field

@dataclass
class Profile:
    name: str = "Iman Perera"
    title: str = "Data Porfessional | Machine Learning Enthusiast | GIS Analyst"
    location: str = "Colombo, Sri Lanka"
    email: str = "kimanrandilaperera@gmail.com"
    phone: str = "+94 76 292 5854"
    linkedin: str = "https://www.linkedin.com/in/imanrandilaperera/"
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

if __name__ == "__main__":
    print(f"Loaded {len(PROJECTS)} projects.")
    print(f"Loaded {len(SKILLS)} skill categories.")
