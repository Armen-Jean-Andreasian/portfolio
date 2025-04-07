import streamlit as st

def display_short_description(project):
    st.markdown(f":blue-badge[Short Description]: {project.description_short}")