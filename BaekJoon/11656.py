# 접미사 배열

from sys import stdin

S = stdin.readline()

length = len(S)
result=[]

for i in range(0,length-1):
  result.append(S[i:-1])

result.sort()
for r in result:
  print(r)