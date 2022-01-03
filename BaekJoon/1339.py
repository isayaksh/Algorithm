from sys import stdin
N = int(stdin.readline())
D = dict()
I = 9
value = 0
lst = []
for _ in range(N):
  tmp = list(stdin.readline().rstrip())
  lst.append(tmp)
for l in lst:
  cnt = 1
  while l:
    tmp = l.pop()
    if tmp in D:
      D[tmp] += cnt
    else:
      D[tmp] = cnt
    cnt *= 10
result = list(D.values())
result.sort()
while result:
  value += result.pop() * I
  I -= 1
print(value)