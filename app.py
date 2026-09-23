import streamlit as st
from data.content import Profile

# Set page config
PROFILE = Profile()
st.set_page_config(page_title=f"{PROFILE.name} — Portfolio", layout="centered")

# Inject CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Define pages
home = st.Page("pages_content/home.py", title="Home", icon="🏠")
projects = st.Page("pages_content/projects.py", title="Projects", icon="🚀")
skills = st.Page("pages_content/skills.py", title="Skills", icon="💻")
education = st.Page("pages_content/education.py", title="Education", icon="🎓")
contact = st.Page("pages_content/contact.py", title="Contact", icon="✉️")

# Router
pg = st.navigation([home, projects, skills, education, contact])
pg.run()
