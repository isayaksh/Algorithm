# 1302 베스트 셀러 <실버 4>
from sys import stdin

N = int(stdin.readline())

D = {}
count = 0

for _ in range(N):
  book = stdin.readline().rstrip()
  if book in D:
    D[book] += 1
  else:
    D[book] = 1
  if count < D[book]:
    count = D[book]
    result = book
  elif count == D[book]:
    result = min(result,book)
print(result)