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


def joseph_ring(people_list, step, start_number):
    while len(people_list) > 1:
        for i in range(1, step):
            if start_number == len(people_list) - 1:
                start_number = 0
            else:
                start_number += 1
        people_list.pop(start_number)
    return people_list


if __name__ == "__main__":
    john = People("john", "22", "boy")
    jim = People("jim", "23", "boy")
    amy = People("amy", "21", "girl")
    jack = People("jack", "20", "boy")
    petty = People("petty", "22", "girl")
    kobe = People("kobe", "24", "boy")
    james = People("james", "25", "boy")
    curry = People("curry", "20", "boy")
    jordan = People("jordan", "21", "boy")
    smith = People("smith", "22", "girl")
    peoples = [john, jim, amy, jack, petty, kobe, james, curry, jordan, smith]
    last_people = joseph_ring(peoples, 3, 0)
    print(f"最后一个人名字:{last_people[0].name}, 年龄:{last_people[0].age}, 性别:{last_people[0].sex}")
