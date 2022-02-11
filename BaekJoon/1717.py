# 1717 집합의 표현 <골드 4>
from sys import stdin

def FindParent(num):
  while S[num][1]:
    num = S[num][1]
  return num

def Union(a,b):
  a = FindParent(a)
  b = FindParent(b)
  if a > b:
    S[b][1] = a
  elif a < b:
    S[a][1] = b

n, m = map(int,stdin.readline().split())
S = []
for i in range(n+1):
  S.append([i,None])

for _ in range(m):
  o, a, b = map(int,stdin.readline().split())
  if o: # 찾기
    if FindParent(a) == FindParent(b):
      print("YES")
    else:
      print("NO")
  else: # 합
    Union(a,b)