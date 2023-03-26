# BOJ 5635 생일
# https://www.acmicpc.net/problem/5635

from sys import stdin

def solution(data):
    result = []
    for name, day, month, year in data:
        result.append((name, int(year) * 365 + int(month) * 30 + int(day)))
    result.sort(key=lambda x : x[1])
    return result[-1][0], result[0][0]

n = int(stdin.readline())
data = list(list(stdin.readline().strip().split()) for _ in range(n))

r1, r2 = solution(data)
print(r1)
print(r2)