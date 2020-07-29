from typing import List

from joseph.domain.reader import Reader
from joseph.domain.people import People
import csv


class CsvReader(Reader):
    ext = "csv"

    def get_people_list(self) -> List[People]:
        people_list = []
        with open(self._file_path, "r") as fp:
            csv_reader = csv.reader(fp)
            for str_people in csv_reader:
                people = People(str_people[0], int(str_people[1]), int(str_people[2]), int(str_people[3]))
                people_list.append(people)
        return people_list

    def __iter__(self):
        with open(self._file_path, "r") as fp:
            csv_reader = csv.reader(fp)
            for csv_line in csv_reader:
                yield csv_line
