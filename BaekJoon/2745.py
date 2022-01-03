# 진법 변환

from sys import stdin

N,B = stdin.readline().split()
B = int(B)

result = 0
count = 1

for k in N[::-1]:
  if k.isdigit():
    k = int(k)
  else:
    k = ord(k)-55
  result+=k*count
  count*=B
print(result)