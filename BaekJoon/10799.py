#쇠막대기

from sys import stdin

bar = list(stdin.readline())

result = 0
stack = []
times = len(bar)
count=0

for i in range(times):
  if bar[i] == ')':
    count-=1
    if bar[i-1] == '(':
      result += count
    elif bar[i-1] == ')':
      result += 1
  elif bar[i] == '(':
    count+=1
print(result)