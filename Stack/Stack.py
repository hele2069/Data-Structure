# Stack (LIFO)

class Stack(object):
    def __init__(self, size=10):
        self.stack = []  # 存放元素
        self.size = size  # 栈容量极限

    def push(self, data):  # 判断栈是否溢出
        if len(self.stack) >= self.size:
            print('StackOverflowError')
            pass
        self.stack.append(data)

    def pop(self):
        if self.stack:  # list is empty = False; vice versa
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')  # 空栈不能被弹出

    def peek(self):  # 查看堆栈的最上面的元素
        if self.stack:
            return self.stack[-1]

    def is_empty(self):  # 判断栈是否为空
        return not bool(self.stack)

    def sizes(self):  # 返回栈的大小
        return len(self.stack)

    def traverse(self):  # print stack
        print(*self.stack)
