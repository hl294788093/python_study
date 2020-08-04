from typing import List
from joseph.domain.people import People


class Reader(object):
    ext = None

    def __init__(self, file_path: str):
        self._file_path = file_path

    def get_people_list(self) -> List[People]:
        raise NotImplementedError
