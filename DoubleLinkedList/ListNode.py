class Node(object):
    # 双向链表节点
    def __init__(self, data=0):
        self.value = data
        self.next = None
        self.prev = None
