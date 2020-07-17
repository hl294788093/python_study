from day04.joseph import Joseph
from day05.txt_reader import TxtReader
from day05.csv_reader import CsvReader
from day05.zip_reader import ZipReader


def test_txt_from_zip():
    zip_reader = ZipReader("file/people.zip")
    zip_reader.extract_zip("zip")
    txt_reader = TxtReader("zip/people.txt")
    joseph = Joseph()
    people_list = txt_reader.get_people_list()
    joseph.append(people_list)
    step = 3
    start_number = 0
    last_people = joseph.get_last_people(step, start_number)
    assert last_people.number == 4


def test_csv_from_zip():
    zip_reader = ZipReader("file/people.zip")
    zip_reader.extract_zip("zip")
    csv_reader = CsvReader("zip/people.csv")
    joseph = Joseph()
    people_list = csv_reader.get_people_list()
    joseph.append(people_list)
    step = -3
    start_number = 0
    last_people = joseph.get_last_people(step, start_number)
    assert last_people.number == 4


def test_csv_with_wrong_file():
    zip_reader = ZipReader("file/people.zip")
    zip_reader.extract_zip("zip")
    csv_reader = CsvReader("zip/people.txt")
    joseph = Joseph()
    people_list = csv_reader.get_people_list()
    joseph.append(people_list)
    step = 3
    start_number = 0
    last_people = joseph.get_last_people(step, start_number)
    assert last_people.number == 4


if __name__ == "__main__":
    try:
        # test_txt_from_zip()
        # test_csv_from_zip()
        test_csv_with_wrong_file()
    except ValueError as ve:
        print(ve)
    except IndexError as ie:
        print(ie)
