# 19496 큰 수  만들기 < 플래티넘 5 >
from sys import stdin
N = int(stdin.readline())
numbers = list(stdin.readline().split())
result = ''
for i in range(N):
    length = len(numbers[i])
    numbers[i] = [numbers[i] * (10//length) + numbers[i][:10%length], length]
numbers.sort(reverse=True)
for i in range(N):
    result += numbers[i][0][:numbers[i][1]]
print((result))