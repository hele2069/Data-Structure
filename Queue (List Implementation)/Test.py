import Queue

x = Queue.Queue()
print(x.size())
print(x.peek())

for i in range(0, 10):
    x.enqueue(i)

print(x.size())
print(x.peek())
print(x.traverse())

x.dequeue()
x.dequeue()
x.enqueue(999)

print(x.size())
print(x.peek())
print(x.traverse())