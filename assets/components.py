import streamlit as st

def section_header(title: str, subtitle: str = ""):
    html = f"""
    <div class="section-header fade-in">
        <h2>{title}</h2>
        {f'<p>{subtitle}</p>' if subtitle else ''}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def card(content_html: str):
    html = f"""
    <div class="custom-card fade-in">
        {content_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def tag_row(tags: list[str]):
    html = ""
    for tag in tags:
        html += f'<span class="tag-chip">{tag}</span>'
    st.markdown(html, unsafe_allow_html=True)

def metric_row(items: list[tuple[str, str]]):
    cols = st.columns(len(items))
    for col, (label, value) in zip(cols, items):
        col.metric(label=label, value=value)
