# BOJ 10825 국영수
# https://www.acmicpc.net/problem/10825

from sys import stdin

def solution(N, data):
    data.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    return [d[0] for d in data]

N = int(stdin.readline())
data = [stdin.readline().strip().split() for _ in range(N)]

response = solution(N, data)
for res in response:
    print(res)