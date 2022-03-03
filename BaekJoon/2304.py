# 2304 창고 다각형
from collections import deque
from sys import stdin

M = [0, 0]
Array = []
sum = 0

N = int(stdin.readline())

for _ in range(N):
  tmp = list(map(int,stdin.readline().split()))
  Array.append(tmp)
  if tmp[1] > M[1]: # 가장 큰 막대 기둥 찾기
    M = tmp

Array.sort() # 기둥 위치 순으로 정렬
start = Array[0][0] # 시작 기둥 위치
middle = M[0] # 가장 큰 막대 기둥 위치
end = Array[-1][0] # 마지막 기둥 위치
Array = deque(Array)

cur = 0
for i in range(start,middle+1): # 시작 기둥 ~ 제일 큰 기둥
  if Array[0][0] == i:
    tmp = Array.popleft()
    if tmp[1] > cur:
      cur = tmp[1]
  sum += cur
  
cur = 0
for i in range(end,middle,-1): # 마지막 기둥 ~ 제일 큰 기둥
  if Array and Array[-1][0] == i:
    tmp = Array.pop()
    if tmp[1] > cur:
      cur = tmp[1]
  sum += cur
print(sum)