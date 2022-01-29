import Stack

stack1 = Stack.Stack()

for i in range(10):
    stack1.push(i)

print(stack1.sizes())
stack1.traverse()
