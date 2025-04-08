import streamlit as st


def display_installation(project):
    if project.installation:
        st.divider()

        st.caption(f"### Installation")
        st.markdown(project.installation)
