import zipfile


class ZipReader(object):
    """
    zip文件读取类，包含功能：
    1.查看压缩包有哪些文件
    2.解压压缩包到自定文件
    """

    def __init__(self, file_path):
        self._file_path = file_path

    def get_zip_list(self):
        with zipfile.ZipFile(self._file_path, 'r') as zip:
            file_list = zip.namelist()
            print(file_list)

    def extract_zip(self, extract_path):
        with zipfile.ZipFile(self._file_path, 'r') as zip:
            file_list = zip.namelist()
            for file in file_list:
                zip.extract(file, extract_path)


def test_zip():
    zip_reader = ZipReader("file/people.zip")
    zip_reader.get_zip_list()
    zip_reader.extract_zip("zip")


if __name__ == "__main__":
    test_zip()
