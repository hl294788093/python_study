from typing import List

from joseph.domain.people import People
from joseph.adapters.csv_reader import CsvReader
from joseph.adapters.txt_reader import TxtReader


class FileUseCase(object):

    @classmethod
    def pick_people_list_in_file(cls, file_path: str) -> List[People]:
        people_list = []
        if file_path.endswith(".txt"):
            txt_reader = TxtReader(file_path)
            people_list = txt_reader.get_people_list()
        elif file_path.endswith(".csv"):
            csv_reader = CsvReader(file_path)
            people_list = csv_reader.get_people_list()
        return people_list
