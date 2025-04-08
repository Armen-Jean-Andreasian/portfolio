from typing import TYPE_CHECKING
import streamlit as st

from ui.widgets.proj_widg.functions import display_title_n_logo
from ui.widgets.proj_widg.functions import display_short_description
from ui.widgets.proj_widg.functions import display_long_description
from ui.widgets.proj_widg.functions import display_url
from ui.widgets.proj_widg.functions import display_category
from ui.widgets.proj_widg.functions import display_proj_type
from ui.widgets.proj_widg.functions import display_screenshots
from ui.widgets.proj_widg.functions import display_videos
from ui.widgets.proj_widg.functions import display_usage
from ui.widgets.proj_widg.functions import display_installation


if TYPE_CHECKING:
    from data.project import Project


def display_proj_capsule(project: "Project"):
    with st.expander(f"**{project.name}**", expanded=False):
        # Title of the project
        display_title_n_logo(project)

        # Project type
        display_proj_type(project)

        # Short Description
        display_short_description(project)

        # Display screenshots in a horizontal layout
        display_screenshots(project)

        # Display videos as clickable items with a clean design
        display_videos(project)


        # Long Description
        display_long_description(project)

        # Usage
        display_usage(project)

        # Installation
        display_installation(project)

        # Project link
        display_url(project)

        # Category
        display_category(project)


