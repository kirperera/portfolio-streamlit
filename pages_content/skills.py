import streamlit as st
from data.content import SKILLS
from assets.components import section_header, tag_row

def render():
    section_header("Technical Skills")
    
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    for category, skills in SKILLS.items():
        with st.container(border=True):
            st.markdown(f"**{category}**")
            tag_row(skills)
    st.markdown('</div>', unsafe_allow_html=True)

render()
