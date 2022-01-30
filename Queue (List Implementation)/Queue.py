class Queue:
    def __init__(self):
        self.entries = []  # 表示队列内的参数
        self.length = 0  # 表示队列的长度

    def size(self):
        return self.length

    def enqueue(self, item):
        self.entries.append(item)  # 添加元素到队列里面
        self.length += 1  # 队列长度增加 1

    def dequeue(self):
        self.length -= 1  # 队列的长度减少 1
        self.entries = self.entries[1:]  # 队首元素为dequeued

    def peek(self):
        if self.size() == 0:
            return "Queue empty"
        else:
            return self.entries[0]  # 直接返回队列的队首元素

    def traverse(self):
        return self.entries
