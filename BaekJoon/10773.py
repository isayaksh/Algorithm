# 10773 제로 <실버 4>
from sys import stdin
K = int(stdin.readline())
lst = []
for _ in range(K):
  num = int(stdin.readline())
  if num:
    lst.append(num)
  else:
    lst.pop()
print(sum(lst))