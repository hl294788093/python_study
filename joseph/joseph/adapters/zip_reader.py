import zipfile
import json
from typing import List

from joseph.domain.people import People
from joseph.domain.reader import Reader

TXT_SUFFIX = ".txt"
CSV_SUFFIX = ".csv"
ZIP_SUFFIX = ".zip"
UTF_8 = "UTF-8"


class ZipReader(Reader):

    def get_people_list(self) -> List[People]:
        """读取zip文件内容，并返回人员列表功能"""
        people_list = []
        with zipfile.ZipFile(self._file_path, "r") as zp:
            file_list = zp.namelist()
            # 遍历zip文件内容，如果包含txt或者csv文件则读取并返回人员列表
            for file in file_list:
                if file.endswith(TXT_SUFFIX):
                    people_list.extend(self.get_people_list_from_txt(file))
                elif file.endswith(CSV_SUFFIX):
                    people_list.extend(self.get_people_list_from_csv(file))
        return people_list

    def get_people_list_from_csv(self, csv_name: str) -> List[People]:
        """从zip中直接读取csv文件内容，并返回人员列表功能"""
        people_list = []
        with zipfile.ZipFile(self._file_path, "r") as zp:
            info = zp.read(csv_name).decode(UTF_8).splitlines()
            for str_people in info:
                str_list = str_people.split(",")
                people = People(str_list[0].replace("\"", ""), int(str_list[1]), int(str_list[2]))
                people_list.append(people)
        return people_list

    def get_people_list_from_txt(self, txt_name: str) -> List[People]:
        """从zip中直接读取txt文件内容，并返回人员列表功能"""
        people_list = []
        with zipfile.ZipFile(self._file_path, "r") as zp:
            info = zp.read(txt_name).decode(UTF_8).splitlines()
            for str_people in info:
                people = json.loads(str_people, object_hook=lambda x: People(x['name'], x['age'], x['sex']))
                people_list.append(people)
        return people_list
