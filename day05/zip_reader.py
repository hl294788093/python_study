import zipfile
import json
from day04.people import People


class ZipReader(object):
    """
    zip文件读取类，包含功能：
    1.查看压缩包有哪些文件
    2.解压压缩包到自定文件
    3.直接读取文件里面csv内容返回people_list
    4.直接读取文件里面txt内容返回people_list
    """

    def __init__(self, file_path):
        self._file_path = file_path

    def get_zip_list(self):
        with zipfile.ZipFile(self._file_path, 'r') as zp:
            file_list = zp.namelist()
            print(file_list)

    def extract_zip(self, extract_path):
        with zipfile.ZipFile(self._file_path, 'r') as zp:
            file_list = zp.namelist()
            for file in file_list:
                zp.extract(file, extract_path)

    def get_people_list_from_csv(self, csv_name):
        people_list = []
        with zipfile.ZipFile(self._file_path, 'r') as zp:
            info = zp.read(csv_name).decode("UTF-8").split("\n")
            for str_people in info:
                str_list = str_people.split(",")
                people = People(str_list[0].replace("\"", ""), int(str_list[1]), int(str_list[2]), int(str_list[3]))
                people_list.append(people)
        return people_list

    def get_people_list_from_txt(self, txt_name):
        people_list = []
        with zipfile.ZipFile(self._file_path, 'r') as zp:
            info = zp.read(txt_name).decode("UTF-8").split("\n")
            for str_people in info:
                people = json.loads(str_people, object_hook=lambda x: People(x['name'], x['number'], x['age'], x['sex']))
                people_list.append(people)
        return people_list


def test_zip_txt():
    zip_reader = ZipReader("file/people.zip")
    people_list = zip_reader.get_people_list_from_txt("people.txt")
    print(people_list)


def test_zip_csv():
    zip_reader = ZipReader("file/people.zip")
    people_list = zip_reader.get_people_list_from_csv("people.csv")
    # print(people_list)


if __name__ == "__main__":
    # test_zip_txt()
    test_zip_csv()
