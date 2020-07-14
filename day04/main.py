from day04.joseph import Joseph
from day04.people import People
import json


def get_joseph_from_txt(file_location, joseph):
    """从文件读取json字符串转换为people对象追加到joseph对象列表"""
    str_people_list = open(file_location, "r")
    for str_people in str_people_list:
        people = json.loads(str_people, object_hook=json_to_people)
        joseph.append(people)
    str_people_list.close()
    return joseph


def json_to_people(d):
    """将json字符串转为people对象"""
    return People(d['name'], d['age'], d['sex'], d['number'])


def test_joseph_iter():
    """测试约瑟夫环迭代功能"""
    joseph = Joseph()
    file_location = "people.txt"
    get_joseph_from_txt(file_location, joseph)
    for i in joseph:
        print(i)


def test_joseph():
    """测试约瑟夫环方法"""
    joseph = Joseph()
    file_location = "people.txt"
    get_joseph_from_txt(file_location, joseph)
    last_people = joseph.get_last_people(3, 0)
    print(last_people)
    assert(last_people.number == 4)


if __name__ == "__main__":
    # 测试约瑟夫环迭代功能
    # test_joseph_iter()
    # 测试约瑟夫环方法
    # test_joseph()
    joseph = Joseph()
    file_location = "people.txt"
    get_joseph_from_txt(file_location, joseph)  # 从文件读取并添加约瑟夫环成员
    length = joseph.get_joseph_length()
    print("约瑟夫环初始化后长度为:%d" % length)
    step = 3
    start_number = 0
    try:
        last_people = joseph.get_last_people(step, start_number)
        print(last_people)
    except ValueError as ve:
        print(ve)
    except IndexError as ie:
        print(ie)


