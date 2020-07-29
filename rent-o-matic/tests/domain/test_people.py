from joseph.domain.people import People


def test_people_init():
    people = People("jack", 3, 21, 0)
    assert people.name == "jack"
    assert people.age == 21
    assert people.sex == "boy"
    assert people.number == 3


if __name__ == "__main__":
    test_people_init()
