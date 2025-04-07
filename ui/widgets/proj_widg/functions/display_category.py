import streamlit as st

def display_category(project):
    if project.category:
        st.divider()
        st.markdown(f":blue-badge[Category]")
        st.write(", ".join(project.category))
