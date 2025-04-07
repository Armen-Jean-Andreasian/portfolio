import os.path
from dataclasses import dataclass
import json
from typing import Optional


@dataclass
class Project:
    name: str
    description_short: str
    project_type: list[str]
    category: list[str]
    screenshots_urls: Optional[list[str]] = None
    video_urls: Optional[list[str]] = None
    logo_url: Optional[str] = None
    urls: Optional[dict[str, str]] = None # {"Source Name": "URL"}
    usage: Optional[str] = None
    description_long: Optional[str] = None

    def dump_to_json_file(self, dir_to_save_jsons: str = "jsons") -> None:
        file_path = os.path.join(dir_to_save_jsons, f"{self.name}.json")

        with open(file_path, "w") as f:
            json.dump(self.__dict__, f, indent=4)
