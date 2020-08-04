import pytest

from joseph.adapters.txt_reader import TxtReader
from joseph.common.constant import *


def test_get_people_list():
    txt_reader = TxtReader(TXT_PATH)
    people_list = txt_reader.get_people_list()
    assert len(people_list) == 7


if __name__ == "__main__":
    pytest.main(["test_txt_reader.py"])