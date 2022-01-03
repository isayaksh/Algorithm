#오등큰수
from sys import stdin

N=int(stdin.readline())
A=list(map(int,stdin.readline().split()))

dic={}
result=[-1 for _ in range(N)]
stack=[0]

# 각 수열의 등장 횟수 count
for i in A:
  if i in dic:
    dic[i]+=1
  else:
    dic[i]=1

# 오등큰수 구하기
for i in range(1, N):
  while stack and dic[A[stack[-1]]] < dic[A[i]]:
    result[stack.pop()] = A[i]
  stack.append(i)

print(*result)