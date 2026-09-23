import streamlit as st
from data.content import PROJECTS
from assets.components import section_header, tag_row

def render():
    section_header("Projects", "Selected data science and software engineering work")
    
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    all_domains = set()
    for p in PROJECTS:
        for d in p.domain:
            all_domains.add(d)
            
    selected_domains = st.pills("Filter by Domain", list(all_domains), default=list(all_domains), selection_mode="multi")
    st.markdown('</div>', unsafe_allow_html=True)
    
    for project in PROJECTS:
        if not set(project.domain).intersection(selected_domains):
            continue
            
        with st.container(border=True):
            st.markdown(f"### {project.title}")
            st.markdown(f"**{project.role}** | {project.period}")
            
            tab1, tab2, tab3 = st.tabs(["Overview", "Tech", "Links"])
            
            with tab1:
                for point in project.points:
                    st.markdown(f"- {point}")
            with tab2:
                tag_row(project.tools)
            with tab3:
                cols = st.columns([1, 1, 8])
                if project.repo_url and "[FILL" not in project.repo_url:
                    with cols[0]:
                        st.link_button("Repository", project.repo_url)
                if project.demo_url and "[FILL" not in project.demo_url:
                    with cols[1]:
                        st.link_button("Live Demo", project.demo_url)

render()
