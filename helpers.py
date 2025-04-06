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


import streamlit as st

import streamlit as st


def display_streamlit(project: "Project"):
    st.divider()

    # Title of the project
    st.title(project.name)
    st.text(project.description)

    # Display project URL as a link with a nice button style
    st.markdown(f"### [Project Link]({project.url})", unsafe_allow_html=True)

    # Display categories in a neat list, separated by commas
    st.subheader("Categories")
    st.write(", ".join(project.category))

    # Display logo in a smaller, neat style
    st.subheader("Logo")
    st.image(project.logo_url, width=200)

    # Display screenshots in a horizontal layout
    st.subheader("Screenshots")
    cols = st.columns(len(project.screenshots_urls))  # Create columns for each screenshot
    for i, screenshot_url in enumerate(project.screenshots_urls):
        with cols[i]:
            st.image(screenshot_url, width=300)

    # Display videos as clickable items with a clean design
    st.subheader("Videos")
    for video_url in project.videos_urls:
        st.markdown(f"### [Watch Video]({video_url})", unsafe_allow_html=True)
        st.video(video_url)




