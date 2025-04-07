import os.path
from dataclasses import dataclass
import json
from typing import Optional


@dataclass
class Project:
    name: str
    description_short: str
    project_type: str
    category: list[str]
    screenshots_urls: list[str]
    videos_urls: list[str]
    logo_url: Optional[str] = None
    url: Optional[str] = None
    repository_url: Optional[str] = None
    usage: Optional[str] = None
    description_long: Optional[str] = None

    def dump_to_json_file(self, dir_to_save_jsons: str = "jsons") -> None:
        file_path = os.path.join(dir_to_save_jsons, f"{self.name}.json")

        with open(file_path, "w") as f:
            json.dump(self.__dict__, f, indent=4)
