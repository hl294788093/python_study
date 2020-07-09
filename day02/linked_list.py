class Node(object):
    """链表节点"""

    def __init__(self, data, pnext=None):
        self.data = data
        self.next = pnext

    def __repr__(self):
        return str(self.data)


class LinkedList(object):
    """链表类"""

    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def append(self, data_or_node):
        """添加节点"""
        item = None
        if isinstance(data_or_node, Node):
            item = data_or_node
        else:
            item = Node(data_or_node)

        # 先判断头节点是否为空
        if self.head is None:
            self.head = item
            self.length += 1
        else:
            head_node = self.head
            while head_node.next is not None:
                head_node = head_node.next
            head_node.next = item
            self.length += 1

    def delete(self, index):
        """删除一个节点"""
        if self.is_empty():
            print("error:linked list is empty!")
            return

        if index < 0 or index >= self.length:
            print("error:index out of bounds!")

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        i = 0
        head_node = self.head
        prev_node = self.head
        while head_node.next is not None and i < index:
            prev_node = head_node
            head_node = head_node.next
            i += 1

        if i == index:
            prev_node.next = head_node.next
            self.length -= 1

    def get_item(self, index):
        """查找一个节点的索引"""
        if self.is_empty() or index < 0 or index >= self.length:
            print("error:index out of bounds")
            return
        i = 0
        node = self.head
        while node.next and i < index:
            node = node.next
            i += 1
        return node.data

    def __repr__(self):
        if self.is_empty():
            return "error:linked list is empty!"
        node = self.head
        node_list = ''
        while node:
            node_list += str(node.data) + ' '
            node = node.next
        return node_list

    def __len__(self):
        return self.length


def get_last_number(n, k):
    """有n个人，依次报数到k的离开，最后返回剩下的人的编号"""
    people_list = LinkedList()
    count = 0  # 计数器
    total_number = 0  # 报数到第几号
    for i in range(1, n + 1):
        people_list.append(i)
    # while len(people_list) != 1:
    #     count += 1
    #     total_number += 1
    #     if total_number == len(people_list) - 1:
    #         total_number = 0
    #     if count == k:
    #         people_list.delete(total_number)
    #         count = 0
    #         total_number -= 1
    while len(people_list) > 1:
        for j in range(1, k):
            if total_number == len(people_list) - 1:
                total_number = 0
            else:
                total_number += 1
        people_list.delete(total_number)
        # if total_number == len(people_list) - 1:
        #     total_number = 0
    return people_list

# (1,2,3,4,5)
# (1,2,4,5)
# (2,4,5)
# (2,4)
# (4)


def test(n, k):
    ans = 0
    i = 0
    for i in range(1, n+1):
        ans = (ans + k) % i
    return ans + 1


a = get_last_number(10, 3)
print(f"结果为{a}")
b = test(8, 4)
print(f"正确结果为{b}")