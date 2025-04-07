from typing import TYPE_CHECKING
import streamlit as st

from ui.widgets.proj_widg.functions import display_title_n_logo
from ui.widgets.proj_widg.functions import display_short_description

if TYPE_CHECKING:
    from data.project import Project


def display_proj_capsule(project: "Project"):
    st.divider()

    # Title of the project
    display_title_n_logo(project)

    # Short Description
    display_short_description(project)

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
