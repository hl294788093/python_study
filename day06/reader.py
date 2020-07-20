from typing import List

from day04.people import People
import json
import csv
import zipfile


class Reader(object):
    ext = None

    def __init__(self, file_path):
        self._file_path = file_path

    def get_people_list(self):
        """实现查询文件返回people_list接口，多态是同一个行为具有多个不同表现形式或形态的能力."""
        raise NotImplementedError


class TxtReader(Reader):
    ext = "txt"

    def get_people_list(self):
        people_list = []
        with open(self._file_path, "r") as fp:
            for str_people in fp:
                people = json.loads(str_people,
                                    object_hook=lambda x: People(x['name'], x['number'], x['age'], x['sex']))
                people_list.append(people)
        return people_list


class CsvReader(Reader):
    ext = "csv"

    def get_people_list(self):
        people_list = []
        with open(self._file_path, "r") as fp:
            csv_reader = csv.reader(fp)
            for str_people in csv_reader:
                people = People(str_people[0], int(str_people[1]), int(str_people[2]), int(str_people[3]))
                people_list.append(people)
        return people_list


class ZipReader(Reader):
    ext = "zip"

    def get_people_list(self):
        file_name = self._file_path.split("/")[-1]
        zip_path = self._file_path.replace(("/" + file_name), "")
        people_list = []
        with zipfile.ZipFile(zip_path, 'r') as zp:
            info = zp.read(file_name).decode("UTF-8").split("\n")
            if file_name.endswith("txt"):
                for str_people in info:
                    people = json.loads(str_people,
                                        object_hook=lambda x: People(x['name'], x['number'], x['age'], x['sex']))
                    people_list.append(people)
            elif file_name.endswith("csv"):
                for str_people in info:
                    str_list = str_people.split(",")
                    people = People(str_list[0].replace("\"", ""), int(str_list[1]), int(str_list[2]), int(str_list[3]))
                    people_list.append(people)
        return people_list
