from sys import stdin
import heapq
N = int(stdin.readline())
lst = []
result = 0
for _ in range(N):
  heapq.heappush(lst,int(stdin.readline()))

while len(lst) > 1:
  tmp = (heapq.heappop(lst) + heapq.heappop(lst))
  heapq.heappush(lst,tmp)
  result += tmp
print(result)