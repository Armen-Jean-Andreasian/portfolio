import streamlit as st


def display_usage(project):
    if project.usage:
        st.divider()

        st.caption(f"### Usage")
        st.markdown(project.usage)
