from day04.people import People
import csv


class CsvReader(object):
    """
    csv文件读取类，提供接口功能：
    1.根据csv文件获取people对象列表
    2.查看文件内容
    3.迭代一行行查看文件内容
    """

    def __init__(self, file_path=""):
        """根据文件路径初始化"""
        if file_path.endswith("csv"):
            self.file_path = file_path
        else:
            raise ValueError("error: file must be *.csv")

    def get_people_list(self):
        """根据文件获取people的列表"""
        people_list = []
        with open(self.file_path, "r") as fp:
            csv_reader = csv.reader(fp)
            for str_people in csv_reader:
                people = People(str_people[0], int(str_people[1]), int(str_people[2]), int(str_people[3]))
                people_list.append(people)
        return people_list

    def get_csv_info(self):
        """查看文件内容"""
        with open(self.file_path) as fp:
            csv_reader = csv.reader(fp)
            csv_info = [line for line in csv_reader]
        return csv_info

    def __iter__(self):
        with open(self.file_path, "r") as fp:
            csv_reader = csv.reader(fp)
            for csv_line in csv_reader:
                yield csv_line


if __name__ == "__main__":
    t = CsvReader("file/people.csv")
    for i in t:
        print(i)
    print(t.get_people_list())
    print(t.get_csv_info())
