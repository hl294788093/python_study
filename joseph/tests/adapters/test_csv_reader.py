import pytest

from joseph.adapters.csv_reader import CsvReader
from joseph.common.constant import *


def test_get_people_list():
    csv_reader = CsvReader(CSV_PATH)
    people_list = csv_reader.get_people_list()
    assert len(people_list) == 8


if __name__ == "__main__":
    pytest.main(["test_csv_reader.py"])