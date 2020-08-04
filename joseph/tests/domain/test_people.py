import pytest

from joseph.domain.people import People


def test_people_init():
    people = People("jack", 21, 0)
    assert people.name == "jack"
    assert people.age == 21
    assert people.sex == "boy"


if __name__ == "__main__":
    pytest.main(["test_people.py"])