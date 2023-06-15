# BOJ 15810 풍선 공장
# https://www.acmicpc.net/problem/15810

from sys import stdin, maxsize

def solution(N, M, A):
    start, end = 0, maxsize
    while start < end:
        time = (start + end)//2
        totalM = sum(time//a for a in A)
        if totalM < M:
            start = time+1
        else:
            end = time
    return end

N, M = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))

res = solution(N, M, A)
print(res)