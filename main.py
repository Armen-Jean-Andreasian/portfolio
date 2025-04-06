import streamlit as st
from helpers import json_files, load_files, display_streamlit
from projects.project import Project

files = json_files()

print(files)

for content in load_files(files):
    proj = Project(**content)
    display_streamlit(proj)
