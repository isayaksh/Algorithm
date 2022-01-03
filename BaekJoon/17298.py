#오큰수
from sys import stdin

N=int(stdin.readline())
A=list(map(int,stdin.readline().split()))

stack=[0]
result=[-1 for _ in range(N)]

for i in range(1,N):
  while stack and A[stack[-1]] < A[i]:
    result[stack.pop()] = A[i]
  stack.append(i)
  
print(*result)