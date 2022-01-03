from sys import stdin

N,K = map(int,stdin.readline().split())

start = 0
result = []

li = list(range(1,N+1))

for i in range(N):
  start+=(K-1)
  if start >= len(li):
    start%=len(li)
  result.append(str(li.pop(start)))
  
# 리스트를 문자열로 일정하게 합쳐주는 join 함수
print("<",", ".join(result),">",sep='')