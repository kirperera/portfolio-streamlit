import streamlit as st
from data.content import EDUCATION, CERTIFICATIONS, ACHIEVEMENTS, VOLUNTEERING
from assets.components import section_header

def render():
    section_header("Education & Certifications")
    
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    # Education
    for edu in EDUCATION:
        with st.container(border=True):
            st.markdown(f"**{edu.degree}**")
            st.markdown(f"{edu.institution} | {edu.period}")
            
    # Certifications
    st.markdown("### Certifications")
    with st.expander("View all certifications"):
        for cert in CERTIFICATIONS:
            status_str = f" ({cert.status})" if cert.status else ""
            issuer_str = f" - {cert.issuer}" if cert.issuer else ""
            st.markdown(f"- **{cert.title}**{issuer_str}{status_str}")
            
    # Achievements
    st.markdown("### Achievements")
    with st.expander("View all achievements"):
        for ach in ACHIEVEMENTS:
            st.markdown(f"- **{ach.title}**: {ach.detail}")
            
    # Volunteering
    st.markdown("### Volunteering")
    with st.expander("View volunteering experience"):
        for vol in VOLUNTEERING:
            st.markdown(f"- **{vol.role}** at {vol.org} ({vol.period})")
            
    st.markdown('</div>', unsafe_allow_html=True)

render()
