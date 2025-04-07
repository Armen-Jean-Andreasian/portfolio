import streamlit as st

def display_short_description(project):
    st.divider()
    st.markdown(f":blue-badge[Description]")
    st.write(project.description_short)