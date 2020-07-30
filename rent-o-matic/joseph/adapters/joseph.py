from typing import List

from joseph.common.constant import *
from joseph.domain.people import People


class Joseph(object):

    def __init__(self):
        self._people_list: List[People] = []

    def append(self, people: People or List[People]) -> None:
        """添加people"""
        if isinstance(people, list):
            self._people_list.extend(people)
        else:
            self._people_list.append(people)

    def pop(self, index: int) -> None:
        """根据索引删除people"""
        self._people_list.pop(index)

    def get_joseph_length(self) -> int:
        """获取约瑟夫环长度"""
        return len(self._people_list)

    def get_last_people(self, step: int, start_number: int) -> People:
        """获取约瑟夫环最后剩下的人"""
        if start_number + step < 0:
            raise IndexError(STEP_ADD_START_UNDER_ZERO_ERROR)
        if step <= 0:
            raise IndexError(STEP_UNDER_ZERO_ERROR)
        if step > len(self._people_list):
            raise IndexError(STEP_OVER_LENGTH_ERROR)
        if start_number > len(self._people_list):
            raise IndexError(START_OVER_LENGTH_ERROR)

        people_list_duplicate = self._people_list.copy()
        while len(people_list_duplicate) > 1:
            for i in range(1, step):
                if start_number >= len(people_list_duplicate) - 1:
                    start_number = 0
                else:
                    start_number += 1
            people_list_duplicate.pop(start_number)
        return people_list_duplicate[0]

    def __iter__(self):
        self._iter = 0
        return self

    def __next__(self):
        if self._iter < len(self._people_list):
            people = self._people_list[self._iter]
            self._iter += 1
            return people
        else:
            raise StopIteration()
