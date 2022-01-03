from sys import stdin
N = list(stdin.readline().rstrip())
sum = 0
if ('0' not in N):
  print(-1)
else:
  for n in N:
    sum += int(n)
  if sum%3!=0:
    print(-1)
  else:
    N.sort(reverse=True)
    print(''.join(N))