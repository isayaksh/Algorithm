# 19539 사과나무 <실버1>
from sys import stdin
N = int(stdin.readline())
H = list(map(int,stdin.readline().split()))
two = 0
one = 0
for h in H:
  one += h%2
  two += h//2
if not (two-one)%3 and two >= one:
  print("YES")
else:
  print("NO")