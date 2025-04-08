import streamlit as st


def display_category(project):
    if project.category:
        st.divider()

        st.caption(f"### Category")
        st.markdown(' '.join(":green-badge[:material/check: {tag}]".format(tag=i) for i in project.category))

