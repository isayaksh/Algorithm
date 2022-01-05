# 1499 수리공 항승 <실버 3>
from sys import stdin
N, L = map(int,stdin.readline().split())
lst = list(map(int,stdin.readline().split()))
lst.sort()
tape = 0 # 테이프의 현재 길이
result = 0 # 테이프 사용 갯수
for l in lst:
  if tape < l:
    tape = l - 0.5 + L
    result +=1
print(result)