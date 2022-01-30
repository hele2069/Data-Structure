import ListNode


class DLinkedList(object):
    # 双向链表
    def __init__(self):
        self.head = ListNode.Node()
        self.tail = ListNode.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self):
        # 判断链表是否为空
        return self.get_length() == 0

    def get_length(self):
        # 返回链表的长度
        if self.head.next == self.tail and self.tail.prev == self.head:
            return 0
        else:
            temp = self.head.next
            count = 0
            while temp != self.tail:
                count += 1
                temp = temp.next
            return count

    def travel(self):
        # 遍历链表
        temp = self.head.next
        ls = []
        while temp != self.tail:
            ls.append(temp.value)
            temp = temp.next
        return ls

    def insert_head(self, item):
        # 头部插入元素
        new = ListNode.Node(item)
        if self.is_empty():
            self.head.next = new
            self.tail.prev = new
            new.prev = self.head
            new.next = self.tail
        else:
            new.next = self.head.next
            new.prev = self.head
            self.head.next.prev = new
            self.head.next = new

    def insert_tail(self, item):
        # 尾部插入元素
        new = ListNode.Node(item)
        if self.is_empty():
            self.head.next = new
            self.tail.prev = new
            new.prev = self.head
            new.next = self.tail
        else:
            new.next = self.tail
            new.prev = self.tail.prev
            self.tail.prev.next = new
            self.tail.prev = new

    def search(self, item):
        # 查找元素是否存在
        temp = self.head.next
        while temp != self.tail:
            if temp.value == item:
                return True
            else:
                temp = temp.next
        return False

    def remove(self, item):
        # 删除元素
        temp = self.head.next
        if self.is_empty():
            return "Nothing to remove"
        else:
            while temp != self.tail:
                if temp.value == item:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return "Successfully removed"
                else:
                    temp = temp.next
        return "The item is not in list"

