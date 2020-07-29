from joseph.domain.reader import Reader


def test_reader_init():
    reader = Reader("data/people.txt")
    assert reader.ext is None


if __name__ == "__main__":
    test_reader_init()