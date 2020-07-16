import zipfile


class ZipReader(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def get_people_list(self):
        with zipfile.ZipFile('file/people.zip', 'r') as zzz:
            file_list = zzz.namelist()
            zzz.extract(file_list[0], "zip")

    def extract_zip(self):
        with zipfile.ZipFile('file/people.zip', 'r') as zzz:
            file_list = zzz.namelist()
            zzz.extract(file_list[0], "zip")


if __name__ == "__main__":
    z = ZipReader("file/people.zip")
    z.get_people_list()
