from dataclasses import dataclass
import json


@dataclass
class Project:
    name: str
    description: str
    project_type: str
    url: str
    category: list[str]
    logo_url: str
    screenshots_urls: list[str]
    videos_urls: list[str]

    def dump_to_json_file(self):
        file_path = f'jsons/{self.name}.json'

        with open(file_path, 'w') as f:
            json.dump(self.__dict__, f, indent=4)



def generate_project(name: str, project_type: str, description: str, url: str, category: list[str], logo_url: str, screenshots_urls: list[str], videos_urls: list[str]):
    return Project(
        name=name,
        project_type=project_type,
        description=description,
        url=url,
        category=category,
        logo_url=logo_url,
        screenshots_urls=screenshots_urls,
        videos_urls=videos_urls
    )


if __name__ == "__main__":
    project = generate_project(
        name="DeepFocus",
        project_type="Private",
        description="Browser extension that blocks distracting websites and helps you stay focused.",
        url="https://addons.mozilla.org/en-US/firefox/addon/deepfocus/",
        category=["productivity", "webextension"],
        logo_url="https://i.ibb.co/LdwV1Kx6/icon-48.png",
        screenshots_urls=[
            "https://addons.mozilla.org/user-media/previews/full/317/317631.png?modified=1743362999",
            "https://addons.mozilla.org/user-media/previews/full/318/318029.png?modified=1743830126",
            "https://addons.mozilla.org/user-media/previews/full/317/317652.png?modified=1743363003",
            "https://addons.mozilla.org/user-media/previews/full/317/317653.png?modified=1743363003",
        ],
        videos_urls=[
            "https://www.youtube.com/watch?v=3aDUypVuAtM"
        ]
    )

    project.dump_to_json_file()