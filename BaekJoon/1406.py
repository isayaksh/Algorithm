from sys import stdin
import collections

front = collections.deque(list(stdin.readline().strip()))

back=collections.deque([])

count = int(stdin.readline())

# del, insert 는 O(n)의 시간을 사용하므로
# O(1)의 시간을 사용하는 pop, append를 이용하여 해결한다.
for i in range(count):
  order = stdin.readline()
  if order[0] == 'L' and front:
    back.appendleft(front.pop())
  elif order[0] == 'D' and back:
    front.append(back.popleft())
  elif order[0] == 'B' and front:
    front.pop()
  elif order[0] == 'P':
    front.append(order[2])
result = front+back
for i in result:
  print(i,end='')
