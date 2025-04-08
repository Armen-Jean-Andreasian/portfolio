import streamlit as st


def display_proj_type(project):
    st.divider()

    st.caption(f"### Project Type")
    st.markdown(' '.join(":violet-badge[:material/star: {tag}]".format(tag=i) for i in project.project_type))

