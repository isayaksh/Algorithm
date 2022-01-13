# 11509 풍선 맞추기 <골드 5>
from sys import stdin
N = int(stdin.readline())
H = list(map(int,stdin.readline().split()))
A = [0 for _ in range(N+1)]
for h in H:
  # 현재 층에 화살이 있는 경우
  if A[h]:
    A[h] -= 1
  A[h-1] += 1
print(sum(A))