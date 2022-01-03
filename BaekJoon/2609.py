# 최대 공약수와 최소 공배수

from sys import stdin
A, B = map(int,stdin.readline().split())
C = A * B
while B:
  A, B = B, A%B
print(A) # 최대 공약수
print(C//A) # 최소 공배수