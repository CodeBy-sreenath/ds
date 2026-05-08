from collections import deque
stack=deque()
stack.append(1)
stack.append('a')
stack.append(3.14)
print(stack)

print(stack.pop())
print(stack)