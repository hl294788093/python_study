from joseph.adapters.joseph import Joseph
from joseph.adapters.csv_reader import CsvReader


def test_joseph():
    """测试约瑟夫环方法"""
    joseph = Joseph()
    csv_reader = CsvReader("../../data/people.csv")
    joseph.append(csv_reader.get_people_list())
    last_people = joseph.get_last_people(3, 0)
    assert last_people.number == 4


if __name__ == "__main__":
    test_joseph()