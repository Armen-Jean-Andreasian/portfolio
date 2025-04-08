import streamlit as st


def display_long_description(project):
    if project.description_long:
        st.divider()

        st.caption(f"### Extended Description")
        st.write(project.description_long)
    else:
        pass
