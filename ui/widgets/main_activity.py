from ui.widgets.proj_widg.proj_widget import display_proj_capsule
from data.project import Project
from ui.helpers import json_files, load_files

class StreamlitUi:
    def __init__(self, dir_with_jsons):
        self.files = json_files(dir_with_jsons)

    def run(self):
        for content in load_files(self.files):
            proj = Project(**content)
            display_proj_capsule(proj)
