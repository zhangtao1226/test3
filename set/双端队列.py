from collections import deque

q = deque(range(5))

print(q)

q.append(2)

print(q)

q.appendleft(7)

print(q)

q.pop()
print(q)
q.popleft()
print(q)

q.rotate(1) #将元素右移
q.rotate(-1) #将元素左移
print(q)