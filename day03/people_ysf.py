class People(object):
    def __init__(self, name, age, sex, number):
        self._name = name
        self._age = age
        self._sex = sex
        self._number = number

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def sex(self):
        return self._sex

    @property
    def number(self):
        return self._number


def joseph_ring(people_list, step, start_number):
    while len(people_list) > 1:
        for i in range(1, step):
            if start_number >= len(people_list) - 1:
                start_number = 0
            else:
                start_number += 1
        people_list.pop(start_number)
    return people_list


if __name__ == "__main__":
    john = People("john", "22", "boy", 1)
    jim = People("jim", "23", "boy", 2)
    amy = People("amy", "21", "girl", 3)
    jack = People("jack", "20", "boy", 4)
    petty = People("petty", "22", "girl", 5)
    kobe = People("kobe", "24", "boy", 6)
    james = People("james", "25", "boy", 7)
    curry = People("curry", "20", "boy", 8)
    jordan = People("jordan", "21", "boy", 9)
    smith = People("smith", "22", "girl", 10)
    peoples = [john, jim, amy, jack, petty, kobe, james, curry, jordan, smith]
    last_people = joseph_ring(peoples, 3, 5)[0]
    print(f"最后一个人名字:{last_people.name}, 年龄:{last_people.age}, 性别:{last_people.sex}, 编号:{last_people.number}")
