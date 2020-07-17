class People(object):

    def __init__(self, name, number, age=0, sex=0):
        """初始化的值判断应该在外部还是内部"""
        self.name = name
        self._age = age
        self._sex = sex
        self.number = number

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError("error: age must be int")

    @property
    def sex(self):
        if self._sex == 0:
            return "boy"
        else:
            return "girl"

    @sex.setter
    def sex(self, value):
        if value == 0 or value == 1:
            self._sex = value
        else:
            raise ValueError("error: sex must be 0(boy) or 1(girl)")

    def __repr__(self):
        return "people's name:%s, age:%d, sex:%s, number:%d" % (
            self.name, self._age, self.sex, self.number)


def test_people_age():
    people = People("A", 0, 12, 1)
    people.age = "23"


def test_people_sex():
    people = People("A", 1, 22, 1)
    people.sex = 0
    assert people.sex == "boy"
    people.sex = 1
    assert people.sex == "girl"


def test_people_sex2():
    people = People("A", 1, 22, 1)
    people.sex = 3


if __name__ == "__main__":
    try:
        test_people_age()
        test_people_sex()
        test_people_sex2()
    except ValueError as ve:
        print(ve)
