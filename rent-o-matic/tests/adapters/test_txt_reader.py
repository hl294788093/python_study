from joseph.adapters.txt_reader import TxtReader


def test_get_people_list():
    txt_reader = TxtReader("../../data/people.txt")
    assert len(txt_reader.get_people_list()) == 10


if __name__ == "__main__":
    test_get_people_list()