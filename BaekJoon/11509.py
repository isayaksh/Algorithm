# 11509 풍선 맞추기 <골드 5>
from sys import stdin
N = int(stdin.readline())
H = list(map(int,stdin.readline().split()))
Cur = [0 for _ in range(1000001)] # 현재 화살의 위치
count = 0
for i in range(N):
  if Cur[H[i]] == 0: # 풍선의 위치에 화살이 없다면
    count += 1
  else: # 풍선의 위치에 화살이 있다면
    Cur[H[i]] -= 1
  Cur[H[i]-1] += 1 # 현재 풍선 위치 -1 에 화살 위치
print(count)