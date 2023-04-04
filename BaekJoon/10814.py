# BOJ 10814 나이순 정렬
# https://www.acmicpc.net/problem/10814

from sys import stdin

def solution(N, data):
    data.sort(key=lambda x : int(x[0]))
    return data

N = int(stdin.readline())
data = list(stdin.readline().split() for _ in range(N))

newData = solution(N, data)
for age, name in newData:
    print(age, name)