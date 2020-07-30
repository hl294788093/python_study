from typing import List

from joseph.adapters.joseph import Joseph
from joseph.common.constant import CONTAINER_JOSEPH
from joseph.domain.people import People


class ContainerUseCase(object):

    """
    机制层：
    选取对应的方法，获得最后一个人员
    """

    @classmethod
    def pick_people_in_order(cls, people_list: List[People], container: str, step: int, start: int) -> People:
        """选取对应的方法，获得最后一个人员"""
        last_people = None
        if container == CONTAINER_JOSEPH:
            joseph = Joseph()
            joseph.append(people_list)
            last_people = joseph.get_last_people(step, start)
        return last_people

