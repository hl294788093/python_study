from joseph.interface.interface import Interface
import pytest


def test_interface_get_people_from_file():
    interface = Interface()
    people_list = interface.get_people_from_file("../../data/people.txt")
    assert len(people_list) == 10


def test_interface_get_last_people():
    interface = Interface()
    interface.get_people_from_file("../../data/people.csv")
    assert interface.get_last_people(3, 0).number == 4


if __name__ == "__main__":
    test_interface_get_people_from_file()
    test_interface_get_last_people()