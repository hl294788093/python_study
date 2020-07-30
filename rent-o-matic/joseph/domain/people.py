from joseph.common.constant import *


class People(object):

    cls_number = 0

    def __init__(self, name: str, age: int = 0, sex: int = 0):
        self.name = name
        self._age = age
        self._sex = sex
        People.cls_number += 1
        self._number = People.cls_number

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError(AGE_NOT_INT_ERROR)

    @property
    def sex(self) -> str:
        if self._sex == 0:
            return SEX_0
        else:
            return SEX_1

    @sex.setter
    def sex(self, value: int) -> None:
        if value == 0 or value == 1:
            self._sex = value
        else:
            raise ValueError(SEX_ERROR)

    @property
    def number(self) -> int:
        return self._number

    def __repr__(self):
        return "people's name:%s,  age:%d,  sex:%s,  number:%d" % (
            self.name, self._age, self.sex, self._number)

    def __eq__(self, other):
        return self.name == other.name and self._age == other.age and self._sex == other.sex
