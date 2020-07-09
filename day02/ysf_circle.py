def get_last_number(number, k):
    """
    输入number个人，每报数到第k个人，就退出，返回最后留下的人的编号
    实现思路：
    1.初始化一个列表用来存放编号。
    2.用一个计数器变量来记录报数循环，用一个变量来保存总报数数
    3.用一个循环来执行游戏，当人数为1时结束。
        3.1 定义出局人员索引，用报数总数除以列表总人数取模，当报数到k次时，将对应人员编号置为0表示出局
        3.2 执行报数，当索引的值为0，即到已出局人数时跳过，不报数。
        3.3 当报数到第k次时，将对应人员编号置为0，剩余人数减1，报数器置为0
        3.4 报数总数加1
    4.循环结束后，过滤人员列表为0的编号，最后剩下的即为留下人的编号
    """
    length = number  # 保存人数
    people_list = []
    for i in range(number):
        people_list.append(i + 1)

    total_number = 0  # 报数总数
    count = 0  # 报数器

    while number > 1:
        index = total_number % length  # 出局人员索引
        if people_list[index] != 0:
            count += 1
        if count == k:
            people_list[index] = 0
            number -= 1
            count = 0
        total_number += 1

    last_people = list(filter(lambda x: x > 0, people_list))[0]  # 最后剩下的人的编号
    return last_people


print(get_last_number(5, 3))