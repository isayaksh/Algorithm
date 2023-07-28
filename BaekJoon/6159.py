# BOJ 6159 Costume Party
# https://www.acmicpc.net/problem/6159

from sys import stdin

def solution(N, S, sizes):
    answer = 0
    sizes.sort()
    for i in range(N-1):
        for j in range(i+1, N):
            if sizes[i] + sizes[j] <= S: answer += 1
            else: break
    return answer

N, S = map(int,stdin.readline().split())
sizes = list(int(stdin.readline()) for _ in range(N))

res = solution(N, S, sizes)
print(res)