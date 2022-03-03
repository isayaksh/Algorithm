# 1269 대칭 차집합 < 실버 3>
from sys import stdin
N, M = map(int,stdin.readline().split())
A = set(map(int,stdin.readline().split()))
B = set(map(int,stdin.readline().split()))
result = (A | B) - (A & B)
print(len(result))