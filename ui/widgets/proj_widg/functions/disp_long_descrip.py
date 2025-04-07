import streamlit as st

def display_long_description(project):
    if project.description_long:
        st.divider()

        st.markdown(f":blue-badge[Extended Description]")
        st.write(project.description_long)
    else:
        pass