from typing import List
from joseph.domain.reader import Reader
from joseph.domain.people import People
import json


class TxtReader(Reader):
    ext = "txt"

    def get_people_list(self) -> List[People]:
        people_list = []
        with open(self._file_path, "r") as fp:
            for str_people in fp:
                people = json.loads(str_people,
                                    object_hook=lambda x: People(x['name'], x['number'], x['age'], x['sex']))
                people_list.append(people)
        return people_list

    def __iter__(self):
        with open(self._file_path, "r") as fp:
            line = fp.readline()
            while line:
                yield line
                line = fp.readline()