from sys import stdin
S = int(stdin.readline())
if S == 1:
  print(1)
else:
  num = 1
  sum = 0
  while sum < S:
    num+=1
    sum+=num
  print(num-1)