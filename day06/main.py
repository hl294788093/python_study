from day04.joseph import Joseph
from day06.reader import *


def test_txt(joseph, step, start_number):
    txt_reader = TxtReader("../day05/file/people.txt")
    people_list = txt_reader.get_people_list()
    joseph.append(people_list)
    assert joseph.get_last_people(step, start_number).number == 4


def test_csv(joseph, step, start_number):
    csv_reader = CsvReader("../day05/file/people.csv")
    people_list = csv_reader.get_people_list()
    joseph.append(people_list)
    assert joseph.get_last_people(step, start_number).number == 10


def test_zip_txt(joseph, step, start_number):
    zip_reader = ZipReader("../day05/file/people.zip/people.txt")
    people_list = zip_reader.get_people_list()
    joseph.append(people_list)
    assert joseph.get_last_people(step, start_number).number == 4


def test_zip_csv(joseph, step, start_number):
    zip_reader = ZipReader("../day05/file/people.zip/people.csv")
    people_list = zip_reader.get_people_list()
    joseph.append(people_list)
    assert joseph.get_last_people(step, start_number).number == 1


if __name__ == "__main__":
    joseph = Joseph()
    step = 3
    start_number = 0
    test_txt(joseph, step, start_number)
    test_csv(joseph, step, start_number)
    test_zip_txt(joseph, step, start_number)
    test_zip_csv(joseph, step, start_number)
    # file_path = "../day05/file/people.txt"
    # for x in Reader.__subclasses__():
    #     if file_path.endswith(x.ext):
    #         reader = x(file_path)
    #         print(reader.get_people_list())
