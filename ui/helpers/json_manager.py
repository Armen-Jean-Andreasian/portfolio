import os
import json


def json_files(dir_with_jsons) -> list[str]:
    """Returns a list of json file full-paths"""
    files = tuple(os.walk(dir_with_jsons))[0][2]
    return [os.path.join(dir_with_jsons, file) for file in files]


def load_files(files: list[str]):
    for file in files:
        with open(file, mode='r', encoding='utf-8') as jf:
            content: dict = json.load(jf)
            yield content
