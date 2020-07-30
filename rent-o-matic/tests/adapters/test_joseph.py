import pytest

from joseph.adapters.joseph import Joseph
from joseph.adapters.txt_reader import TxtReader
from joseph.common.constant import *
from joseph.domain.people import People


def test_get_last_people():
    joseph = Joseph()
    People.cls_number = 0
    txt_reader = TxtReader(TXT_PATH)
    joseph.append(txt_reader.get_people_list())
    last_people = joseph.get_last_people(3, 2)
    assert last_people.number == 3


def test_get_joseph_length():
    joseph = Joseph()
    txt_reader = TxtReader(TXT_PATH)
    joseph.append(txt_reader.get_people_list())
    assert joseph.get_joseph_length() == 7


if __name__ == "__main__":
    pytest.main(["test_joseph.py"])