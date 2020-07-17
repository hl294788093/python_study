from day04.joseph import Joseph
from day05.txt_reader import TxtReader
from day05.csv_reader import CsvReader
from day05.zip_reader import ZipReader


def test_txt():
    # txt文件读取测试
    txt_reader = TxtReader("file/people.txt")
    joseph = Joseph()
    people_list = txt_reader.get_people_list()
    joseph.append(people_list)
    step = 3
    start_number = 0
    last_people = joseph.get_last_people(step, start_number)
    assert last_people.number == 4


def test_csv():
    # csv文件读取测试
    csv_reader = CsvReader("file/people.csv")
    joseph = Joseph()
    people_list = csv_reader.get_people_list()
    joseph.append(people_list)
    step = -3
    start_number = 0
    last_people = joseph.get_last_people(step, start_number)
    assert last_people.number == 4


def test_csv_with_wrong_file():
    # 用csv读取txt文件测试
    csv_reader = CsvReader("file/people.txt")
    joseph = Joseph()
    people_list = csv_reader.get_people_list()
    joseph.append(people_list)
    step = 3
    start_number = 0
    last_people = joseph.get_last_people(step, start_number)
    assert last_people.number == 4


def test_txt_from_zip():
    # 测试直接读取zip中的txt文件
    zip_reader = ZipReader("file/people.zip")
    joseph = Joseph()
    people_list = zip_reader.get_people_list_from_txt("people.txt")
    joseph.append(people_list)
    step = 3
    start_number = 0
    last_people = joseph.get_last_people(step, start_number)
    assert last_people.number == 4


def test_people_from_different():
    txt_reader = TxtReader("file/people.txt")
    txt_people_list = txt_reader.get_people_list()
    csv_reader = CsvReader("file/people.csv")
    csv_people_list = csv_reader.get_people_list()
    zip_reader = ZipReader("file/people.zip")
    zip_people_list = zip_reader.get_people_list_from_txt("people.txt")
    joseph = Joseph()
    joseph.append(txt_people_list)
    joseph.append(csv_people_list)
    joseph.append(zip_people_list)
    step = 4
    start_number = 13
    last_people = joseph.get_last_people(step, start_number)
    print(last_people)


if __name__ == "__main__":
    try:
        # test_txt()
        # test_csv()
        # test_csv_with_wrong_file()
        # test_txt_from_zip()
        test_people_from_different()
    except ValueError as ve:
        print(ve)
    except IndexError as ie:
        print(ie)
