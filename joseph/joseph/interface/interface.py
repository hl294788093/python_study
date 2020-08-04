from typing import List


from joseph.domain.people import People
from joseph.use_cases.container_use_cases import ContainerUseCase
from joseph.use_cases.file_use_cases import FileUseCase


class Interface(object):
    """
    对外接口层，提供rest界面数据
    """

    def __init__(self):
        self._people_list: List[People] = []

    def get_people_from_file(self, file_path: str) -> List[People]:
        """1.接收界面输入文件名，初始化people列表并返回"""
        people_list = FileUseCase.pick_people_list_in_file(file_path)
        self._people_list.extend(people_list)
        return self._people_list

    def get_last_people(self, container: str, step: int, start_number: int) -> People:
        """2.输入起始点和间隔，获取约瑟夫环最后一个人"""
        last_people = ContainerUseCase.pick_people_in_order(self._people_list, container, step, start_number)
        return last_people
