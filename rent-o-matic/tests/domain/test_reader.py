import pytest

from joseph.common.constant import ZIP_PATH
from joseph.domain.reader import Reader


def test_reader_init():
    reader = Reader(ZIP_PATH)
    assert reader.ext is None


if __name__ == "__main__":
    pytest.main(["test_people.py"])