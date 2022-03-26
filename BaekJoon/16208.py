# 16208 귀찮음 < 실버 5 >
from sys import stdin
n = int(stdin.readline())
A = sorted(list(map(int,stdin.readline().split()))) # 파이프 길이 오름차순 정렬
total = sum(A) # 파이프의 총 길이
result = 0
for a in A:
  total -= a # 얻어야 하는 파이프 길이만큼 잘라낸 길이 
  result += a * total
print(result)