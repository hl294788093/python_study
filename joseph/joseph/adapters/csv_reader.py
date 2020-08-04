from typing import List

from joseph.domain.reader import Reader
from joseph.domain.people import People
import csv


class CsvReader(Reader):

    def get_people_list(self) -> List[People]:
        """读取csv文件内容，并返回人员列表功能"""
        people_list = []
        with open(self._file_path, "r") as fp:
            csv_reader = csv.reader(fp)
            for str_people in csv_reader:
                people = People(str_people[0], int(str_people[1]), int(str_people[2]))
                people_list.append(people)
        return people_list

    def __iter__(self):
        """迭代返回文件内容功能"""
        with open(self._file_path, "r") as fp:
            csv_reader = csv.reader(fp)
            for csv_line in csv_reader:
                yield csv_line
