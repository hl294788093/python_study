class Joseph(object):
    """
    约瑟夫环类,提供方法
    1.添加People成员方法
    2.删除people方法
    3.返回约瑟夫环最后剩下的人方法
    4.获取约瑟夫环长度
    5.迭代成员方法
    """

    def __init__(self):
        self._iter = 0
        self._people_list = []

    def append(self, people):
        """添加people"""
        self._people_list.append(people)

    def pop(self, index):
        """根据索引删除people"""
        self._people_list.pop(index)

    def get_joseph_length(self):
        """获取约瑟夫环长度"""
        return len(self._people_list)

    def get_last_people(self, step, start_number):
        """获取约瑟夫环最后剩下的人"""
        if start_number + step < 0:
            raise IndexError("error:起点加间隔小于0")
        if step < 0 or step < len(self._people_list):
            raise ValueError("error:间隔step小于0")
        while len(self._people_list) > 1:
            for i in range(1, step):
                if start_number >= len(self._people_list) - 1:
                    start_number = 0
                else:
                    start_number += 1
            self._people_list.pop(start_number)
        return self._people_list[0]

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter < len(self._people_list):
            people = self._people_list[self._iter]
            self._iter += 1
            return people
        else:
            self._iter = 0
            raise StopIteration()
