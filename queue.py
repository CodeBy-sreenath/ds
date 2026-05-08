from collections import deque
que=deque()
que.append(1)
que.append(2)
que.append(3)
print(que)
print(que.popleft())
que.popleft()
print(que)