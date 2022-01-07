# 11508 2+1 세일 <실버 4>
from sys import stdin
N = int(stdin.readline())
C = []
result = 0
for _ in range(N):
  C.append(int(stdin.readline()))
C.sort()
while len(C) > 2:
  result += C.pop() + C.pop()
  C.pop()
result += sum(C)
print(result)