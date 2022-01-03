# 알파벳 찾기

from sys import stdin

S = stdin.readline().rstrip()

dic = {}
count=0

for i in range(97,123):
  dic[chr(i)] = -1
for s in S:
  if dic[s] == -1:
    dic[s]=count
  count+=1
  
result = dic.values()
print(*result)