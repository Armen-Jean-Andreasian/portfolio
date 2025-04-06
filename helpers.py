from typing import TYPE_CHECKING
import streamlit as st

if TYPE_CHECKING:
    from projects.project import Project


def json_files() -> list[str]:
    """Returns a list of json file full-paths"""
    import os
    folder = os.path.join('projects', 'jsons')
    files = tuple(os.walk(folder))[0][2]
    return [os.path.join(folder, file) for file in files]


def load_files(files: list[str]):
    import json
    for file in files:
        with open(file, mode='r', encoding='utf-8') as jf:
            content: dict = json.load(jf)
            yield content


def display_streamlit(project: "Project"):
    st.divider()

    # Title of the project
    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <img src="{project.logo_url}" width="50" style="margin-right: 10px;" />
            <h1 style="margin: 0;">{project.name}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Project Type
    st.markdown(f":blue-badge[Project type]: {project.project_type}")

    # Description
    st.markdown(f":blue-badge[Description]: {project.description}")

    # Project link
    st.markdown(f":blue-badge[Project link]: [URL]({project.url})", unsafe_allow_html=True)

    # Category
    st.markdown(f":blue-badge[Category]: " + ", ".join(project.category))

    # Display screenshots in a horizontal layout
    st.subheader("Screenshots")
    cols = st.columns(2)

    for i, screenshot_url in enumerate(project.screenshots_urls):
        with cols[i % 2]:  # Alternate between col[0] and col[1]
            st.image(screenshot_url, use_container_width=True)  # or set width=300

    # Display videos as clickable items with a clean design
    st.subheader("Videos")
    for video_url in project.videos_urls:
        st.video(video_url)
