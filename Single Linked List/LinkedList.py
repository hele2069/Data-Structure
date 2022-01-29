import ListNode


class LinkedList:
    def __init__(self):
        self.head = ListNode.Node()

    def is_empty(self):  # 判断链表是否为空
        if self.head.next is None:
            return True
        else:
            return False

    def get_length(self):  # 获取链表的长度
        temp = self.head  # 临时变量指向队列头部
        length = 0  # 计算链表的长度变量
        while temp.next is not None:
            length = length + 1
            temp = temp.next
        return length  # 返回链表的长度

    def insert(self, value):  # 链表插入数据函数
        temp = ListNode.Node(value)
        if self.is_empty():
            self.head.next = temp
        else:
            temp.next = self.head.next
            self.head.next = temp

    def print_list(self):  # 遍历链表，并将元素依次打印出来
        temp = self.head.next
        new_list = []
        while temp is not None:
            new_list.append(temp.value)
            temp = temp.next
        return new_list
