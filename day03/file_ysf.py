import json
from day03.people_ysf import *


def get_people_list_from_txt():
    """从文件读取json字符串转换为people对象列表"""
    str_people_list = open("/Users/huangliang/Documents/python/PythonProject/python_study/day03/people.txt", "r")
    people_list = []
    for str_people in str_people_list:
        people = json.loads(str_people, object_hook=dict_to_people)
        people_list.append(people)
    str_people_list.close()
    return people_list


def dict_to_people(d):
    """将json字符串转为people对象"""
    return People(d['name'], d['age'], d['sex'], d['number'])


# 测试代码
def test_file_read(people_list):
    assert (joseph_ring(people_list, 3, 0)[0].number == 4)


if __name__ == "__main__":
    people_list = get_people_list_from_txt()
    # test_file_read(people_list)
    last_people = joseph_ring(people_list, 3, 8)[0]
    print(f"最后一个人名字:{last_people.name}, 年龄:{last_people.age}, 性别:{last_people.sex}, 编号:{last_people.number}")




