import pytest

from joseph.adapters.zip_reader import ZipReader
from joseph.common.constant import *
import os.path


def test_zip_get_people_list():
    zip_reader = ZipReader(ZIP_PATH)
    people_list = zip_reader.get_people_list()
    assert len(people_list) == 15


def test_get_people_list_from_csv():
    zip_reader = ZipReader(ZIP_PATH)
    people_list = zip_reader.get_people_list_from_csv(os.path.basename(CSV_PATH))
    assert len(people_list) == 8


def test_get_people_list_from_txt():
    zip_reader = ZipReader(ZIP_PATH)
    people_list = zip_reader.get_people_list_from_txt(os.path.basename(TXT_PATH))
    assert len(people_list) == 7


if __name__ == "__main__":
    pytest.main(["test_zip_reader.py"])
