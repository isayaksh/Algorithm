from sys import stdin
N = int(stdin.readline())
k = []
w = 0
for _ in range(N):
  k.append(int(stdin.readline()))
k.sort(reverse=True)
for i in range(N):
  if k[i]*(i+1) > w:
    w = k[i]*(i+1)
print(w)