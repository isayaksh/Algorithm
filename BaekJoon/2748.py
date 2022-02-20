# 2748 피보나치 수 2 <브론즈 1>
from sys import stdin
result = [0,1]
for i in range(2,91):
  result.append(result[i-1]+result[i-2])
n = int(stdin.readline())
print(result[n])