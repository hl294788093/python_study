class People(object):

    def __init__(self, name, age, sex, number):
        self.name = name
        self._age = age
        self._sex = sex
        self.number = number

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value

    def __repr__(self):
        return "people's name:%s, age:%s, sex:%s, number:%d" % (self.name, self._age, self._sex, self.number)
