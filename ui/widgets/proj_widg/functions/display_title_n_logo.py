import streamlit as st


def display_title_n_logo(project):
    if project.logo_url:
        st.markdown(
            f"""
            <div style="display: flex; align-items: center;">
                <img src="{project.logo_url}" width="50" style="margin-right: 10px;" />
                <h1 style="margin: 0;">{project.name}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(f"<h1 style='margin: 0;'>{project.name}</h1>", unsafe_allow_html=True)
