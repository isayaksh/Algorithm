# 알파벳 개수

from sys import stdin

S = stdin.readline().rstrip()

dic = {}

for i in range(97,123):
  dic[chr(i)] = 0
for s in S:
  dic[s]+=1
result = dic.values()
print(*result)