# 조합 0의 개수

from sys import stdin

def F(n):
  count = 0
  while n != 0:
    n//=5
    count+=n
  return count

def T(n):
  count = 0
  while n != 0:
    n//=2
    count+=n
  return count

n, m = map(int,stdin.readline().split())

print(min(F(n) - F(m) - F(n-m), T(n) - T(m) - T(n-m) ))