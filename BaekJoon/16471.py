# 16471 작은 수 내기 < 실버 4 >
from collections import deque
from sys import stdin
N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
B = list(map(int,stdin.readline().split()))
A.sort() # 오름차순 정렬
B.sort() # 오름차순 정렬
B = deque(B)
count = 0
for i in range(N): # 작은 값 순서대로
  while B: # 모든 사장님 카드 확인
    if B.popleft() > A[i]: # 사장님 카드보다 작은 카드라면
      count += 1 # 승수 + 1
      break
if count > (N // 2): # 승수가 N // 2 보다 크면
  print("YES") 
else: # 승수가 N // 2 보다 작다면
  print("NO")