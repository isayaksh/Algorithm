# 12931  두 배 더하기 < 골드 4 >
from sys import stdin
N = int(stdin.readline())
B = list(map(int,stdin.readline().split()))
count = 0 # 연산 횟수
while sum(B): # 모든 B의 원소가 0이 될 때까지
  for i in range(N):
    if B[i] % 2 and B[i] > 0: # B[i]가 0보다 큰 홀수라면
      B[i]  -= 1 # 1 증가 연산
      count += 1 # 연산 횟수 + 1
  if sum(B): # 모든 B의 원소가 0이 아니라면
    # B의 모든 원소 2배 증가 연산
    for i in range(N):
      B[i]  = B[i] // 2
    count += 1 # 연산 횟수 + 1
print(count)