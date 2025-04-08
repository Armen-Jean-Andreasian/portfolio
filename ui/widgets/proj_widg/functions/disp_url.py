import streamlit as st


def display_url(project):
    if project.urls:
        st.divider()
        st.caption(f"### Links")

        st.markdown(" ".join(f"[:blue-badge[{source_name}]]({url})" for source_name, url in project.urls.items()))
