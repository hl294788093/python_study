from typing import List

from joseph.domain.people import People
from joseph.adapters.csv_reader import CsvReader
from joseph.adapters.txt_reader import TxtReader
from joseph.adapters.zip_reader import ZipReader
from joseph.domain.reader import Reader

TXT_SUFFIX = ".txt"
CSV_SUFFIX = ".csv"
ZIP_SUFFIX = ".zip"


class FileUseCase(object):
    """
    机制层：
    选取对应的reader，读取文件并返回人员列表
    """

    @classmethod
    def pick_people_list_in_file(cls, file_path: str) -> List[People]:
        """根据传入的文件生成人员列表"""
        reader = FileUseCase.get_reader_by_file(file_path)
        people_list = reader.get_people_list()
        return people_list

    @classmethod
    def get_reader_by_file(cls, file_path: str) -> Reader:
        """根据文件不同，生成对应的Reader类返回"""
        if file_path.endswith(TXT_SUFFIX):
            return TxtReader(file_path)
        elif file_path.endswith(CSV_SUFFIX):
            return CsvReader(file_path)
        elif file_path.endswith(ZIP_SUFFIX):
            return ZipReader(file_path)
