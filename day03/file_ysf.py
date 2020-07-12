import io
import json


class People(object):
    def __init__(self, name, age, sex):
        self._name = name
        self._age = age
        self._sex = sex

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def sex(self):
        return self._sex


def get_people_from_txt():
    f = open("/Users/huangliang/Documents/python/PythonProject/python_study/day03/people.txt", "r+")
    people = f.readline()
    f.close()
    return people


def dict2people(d):
    return People(d['name'], d['age'], d['sex'])


people = get_people_from_txt()
print(json.loads(people, object_hook=dict2people))
