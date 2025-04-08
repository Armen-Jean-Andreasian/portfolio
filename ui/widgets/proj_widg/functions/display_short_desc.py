import streamlit as st


def display_short_description(project):
    st.divider()
    st.caption(f"### Description")
    st.write(project.description_short)
