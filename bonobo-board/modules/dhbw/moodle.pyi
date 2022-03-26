from typing import ClassVar
from bs4.element import Tag

from .util import ImporterSession, MoodleCourseDict, MoodleModuleDict


def add_to_module_dict(name: str, url: str) -> MoodleModuleDict: ...


def get_bbb_instance_name(tag_a: Tag) -> str: ...


class MoodleImporter(ImporterSession):
    url: ClassVar[str]
    logout_url: str

    def __init__(self) -> None: ...

    def login(self, username: str, password: str) -> None: ...

    def find_all_bbb_rooms(self, course_dict: MoodleCourseDict) -> MoodleCourseDict: ...

    def scrape(self) -> None: ...

    def logout(self) -> None: ...
