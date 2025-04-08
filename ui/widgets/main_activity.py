from ui.widgets.proj_widg.proj_widget import display_proj_capsule
from .proj_widg import show_footer
from data.project import Project
from ui.helpers import json_files, load_files
import streamlit as st
from config import GITHUB_URL, LINKEDIN_URL


class StreamlitUi:
    def __init__(self, dir_with_jsons):
        self.files = json_files(dir_with_jsons)


    def set_design(self):
        st.set_page_config(
            page_title="The lab",
            page_icon="https://static.thenounproject.com/png/1876208-200.png",
            initial_sidebar_state="expanded",
        )

        st.subheader("The Projects of Armen-Jean Andreasian")


    def run(self):
        self.set_design()
        for content in load_files(self.files):
            proj = Project(**content)
            with st.container():
                # Optional: wrap your custom capsule in a div for styling
                st.markdown('<div class="project-capsule">', unsafe_allow_html=True)
                display_proj_capsule(proj)
                st.markdown('</div>', unsafe_allow_html=True)


        # Footer with clickable logos
        show_footer(linked_in_url=LINKEDIN_URL, github_url=GITHUB_URL)