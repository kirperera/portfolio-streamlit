import streamlit as st
from data.content import Profile, SKILLS
from assets.components import section_header, tag_row

def render():
    profile = Profile()
    
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title(profile.name)
    st.subheader(profile.title)
    st.write(profile.summary)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Contact row
    cols = st.columns(5)
    with cols[0]:
        st.markdown(f"📧 [Email](mailto:{profile.email})")
    with cols[1]:
        st.markdown(f"🐙 [GitHub](https://github.com/{profile.github})")
    with cols[2]:
        st.markdown(f"💼 [LinkedIn]({profile.linkedin})")
    with cols[3]:
        st.markdown(f"📍 {profile.location}")
    with cols[4]:
        st.markdown(f"📱 {profile.phone}")
        
    section_header("Skills Overview")
    tag_row(list(SKILLS.keys()))
    
render()
