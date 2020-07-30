import pytest

from joseph.adapters.txt_reader import TxtReader
from joseph.common.constant import *
from joseph.domain.people import People
from joseph.use_cases.container_use_cases import ContainerUseCase


def test_pick_people_in_order():
    txt_reader = TxtReader(TXT_PATH)
    People.cls_number = 0
    people_list = txt_reader.get_people_list()
    last_people = ContainerUseCase.pick_people_in_order(people_list, CONTAINER_JOSEPH, 3, 1)
    assert last_people.number == 1


if __name__ == "__main__":
    pytest.main(["test_container_use_cases.py"])