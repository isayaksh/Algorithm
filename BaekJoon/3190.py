# 3190 뱀 <골드 5>
from collections import deque
from sys import stdin

# 보드 생성
N = int(stdin.readline())
B = [[False for _ in range(N)] for _ in range(N)]
B[0][0] = True

# 사과 배치
K = int(stdin.readline())
for _ in range(K):
  X, Y = map(int, stdin.readline().split())
  B[X-1][Y-1] = "Apple"

# 방향 변환 값
L = deque()
l = int(stdin.readline())
for _ in range(l):
  X, C = stdin.readline().split()
  L.append((int(X),C))

# 뱀 이동
time = 1
direction = 0
curLocation = [0,0]
route = deque([[0,0]])
while True:
  # for b in B:
  #   print(b)
  # print()

  # 이동 방향에 따른 이동 위치 설정
  if direction == 0:
    curLocation[1] += 1
  elif direction == 1:
    curLocation[0] += 1
  elif direction == 2:
    curLocation[1] -= 1
  elif direction == 3:
    curLocation[0] -= 1

  # 뱀이 Board를 벗어났을 경우
  if curLocation[0] >= N or curLocation[0] < 0:
    break
  if curLocation[1] >= N or curLocation[1] < 0:
    break
  
  # 뱀이 자신의 몸과 부딪힐 경우
  if B[curLocation[0]][curLocation[1]] == True:
    break

  # 현재 위치에 사과의 존재 유무
  if B[curLocation[0]][curLocation[1]] != "Apple":
    tmp = route.pop()
    B[tmp[0]][tmp[1]] = False
  
  B[curLocation[0]][curLocation[1]] = True
  route.appendleft((curLocation[0],curLocation[1]))

  # 방향 전환
  if L and L[0][0] == time:
    if L[0][1] == 'L':
      direction = (direction + 3) % 4
    elif L[0][1] == 'D':
      direction = (direction + 1) % 4
    L.popleft()

  time += 1
print(time)