import streamlit as st
from data.content import Profile
from assets.components import section_header

def render():
    section_header("Contact")
    
    profile = Profile()
    
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(f"📧 **Email:** [{profile.email}](mailto:{profile.email})")
        st.code(profile.email, language=None)  # Copy to clipboard utility
        st.markdown(f"📱 **Phone:** {profile.phone}")
        st.markdown(f"📍 **Location:** {profile.location}")
        st.markdown(f"🐙 **GitHub:** [github.com/{profile.github}](https://github.com/{profile.github})")
        st.markdown(f"💼 **LinkedIn:** [{profile.linkedin}]({profile.linkedin})")
    st.markdown('</div>', unsafe_allow_html=True)

render()
