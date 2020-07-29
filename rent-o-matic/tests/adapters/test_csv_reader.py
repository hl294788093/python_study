from joseph.adapters.csv_reader import CsvReader


def test_get_people_list():
    csv_reader = CsvReader("../../data/people.csv")
    assert len(csv_reader.get_people_list()) == 10


if __name__ == "__main__":
    test_get_people_list()