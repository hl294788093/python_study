from day04.joseph import Joseph
from day05.txt_reader import TxtReader


def test_txt():
    txt_reader = TxtReader("file/people.txt")
    joseph = Joseph()
    people_list = txt_reader.get_people_list()
    joseph.append(people_list)
    print(joseph.get_last_people(3, 0))
    print(joseph.get_joseph_length())
    for i in joseph:
        print(i)


if __name__ == "__main__":
    test_txt()
