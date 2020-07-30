from joseph.common.constant import *
from joseph.domain.people import People
from joseph.interface.interface import Interface
import pytest


def test_get_people_from_txt():
    interface = Interface()
    people_list = interface.get_people_from_file(TXT_PATH)
    assert len(people_list) == 7


def test_get_people_from_csv():
    interface = Interface()
    people_list = interface.get_people_from_file(CSV_PATH)
    assert len(people_list) == 8


def test_get_last_people():
    interface = Interface()
    People.cls_number = 0
    interface.get_people_from_file(CSV_PATH)
    last_people = interface.get_last_people(CONTAINER_JOSEPH, 3, 4)
    assert last_people.number == 3


if __name__ == "__main__":
    pytest.main(["test_interface.py"])