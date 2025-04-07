import streamlit as st

def display_proj_type(project):
    st.divider()

    st.markdown(f":blue-badge[Project Type]")
    st.write(", ".join(project.project_type))
