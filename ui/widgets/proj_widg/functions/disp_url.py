import streamlit as st

def display_url(project):
    if project.urls:
        st.divider()
        st.markdown(f":blue-badge[Links]", unsafe_allow_html=True)

        for source_name, url in project.urls.items():
            st.markdown(f":red-badge[{source_name}]: [URL]({url})", unsafe_allow_html=True)
