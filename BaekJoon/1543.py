# 1543 문서 검색 <실버 4>
from sys import stdin
document = stdin.readline().rstrip()
word = stdin.readline().rstrip()
wl = len(word)
result = 0
while True:
  idx = document.find(word)
  if idx == -1:
    break
  document = document[idx+wl:]
  result +=1
print(result)