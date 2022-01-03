from sys import stdin
import collections

deque=collections.deque([])

N = int(stdin.readline())

for i in range(N):
  order = list(map(str,stdin.readline().split()))
  if order[0] == 'push_front':
    deque.appendleft(order[1])
  elif order[0] == 'push_back':
    deque.append(order[1])
  elif order[0] == 'pop_front':
    if deque:
      print(deque.popleft())
    else:
      print(-1)
  elif order[0] == 'pop_back':
    if deque:
      print(deque.pop())
    else:
      print(-1)
  elif order[0] == 'size':
    print(len(deque))
  elif order[0] == 'empty':
    if not deque:
      print(1)
    else:
      print(0)
  elif order[0] == 'front':
    if deque:
      print(deque[0])
    else:
      print(-1)
  elif order[0] == 'back':
    if deque:
      print(deque[-1])
    else:
      print(-1)
