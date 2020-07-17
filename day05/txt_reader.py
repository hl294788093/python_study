from day04.people import People
import json


class TxtReader(object):
    """
    txt文件读取类，提供接口功能：
    1.根据txt文件获取people对象列表
    2.查看文件内容
    3.迭代一行行查看文件内容
    """

    def __init__(self, file_path=""):
        """根据文件路径初始化"""
        if file_path.endswith("txt"):
            self._file_path = file_path
        else:
            raise ValueError("error: file must be *.txt")

    def get_people_list(self):
        """根据文件获取people的列表"""
        people_list = []
        with open(self._file_path, "r") as fp:
            for str_people in fp:
                people = json.loads(str_people, object_hook=lambda x: People(x['name'], x['number'], x['age'], x['sex']))
                people_list.append(people)
        return people_list

    def get_txt_info(self):
        """查看文件内容"""
        with open(self._file_path) as fp:
            txt_info = fp.readlines()
        return txt_info

    def __iter__(self):
        with open(self._file_path, "r") as fp:
            line = fp.readline()
            while line:
                yield line
                line = fp.readline()


def test_txt_get_people():
    txt_reader = TxtReader("file/people.txt")
    people_list = txt_reader.get_people_list()
    print(people_list)


def test_txt_get_info():
    txt_reader = TxtReader("file/people.txt")
    print(txt_reader.get_txt_info())


def test_txt_iter():
    txt_reader = TxtReader("file/people.txt")
    for line in txt_reader:
        print(line)


if __name__ == "__main__":
    test_txt_get_people()
    test_txt_get_info()
    test_txt_iter()
