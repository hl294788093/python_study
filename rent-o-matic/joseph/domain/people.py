class People(object):
    def __init__(self, name: str, number: int, age: int = 0, sex: int = 0):
        self.name = name
        self._age = age
        self._sex = sex
        self.number = number

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError("error: age must be int")

    @property
    def sex(self) -> str:
        if self._sex == 0:
            return "boy"
        else:
            return "girl"

    @sex.setter
    def sex(self, value: int) -> None:
        if value == 0 or value == 1:
            self._sex = value
        else:
            raise ValueError("error: sex must be 0(boy) or 1(girl)")

    def __repr__(self):
        return "people's name:%s, age:%d, sex:%s, number:%d" % (
            self.name, self._age, self.sex, self.number)

    def __eq__(self, other):
        return self.name == other.name and self._age == other.age and self._sex == other.sex
