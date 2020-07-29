from typing import List

from joseph.adapters.joseph import Joseph
from joseph.domain.people import People


class ContainerUseCase(object):

    @classmethod
    def pick_people_in_order(cls, people_list: List[People], container: str, step: int, start: int) -> People:
        last_people = None
        if container == "joseph":
            joseph = Joseph()
            joseph.append(people_list)
            last_people = joseph.get_last_people(step, start)
        return last_people

