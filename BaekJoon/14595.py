# BOJ 14595 동방 프로젝트 (Large)
# https://www.acmicpc.net/problem/14595

from sys import stdin

def solution(N, M, pair):
    pair.sort()
    answer = 1
    if not M: return N
    line = 1
    for x, y in pair:
        if line < x:
            answer += (x-line)
        line = max(line, y)
    return answer + (N-line)

N = int(stdin.readline())
M = int(stdin.readline())
pair = list(list(map(int,stdin.readline().split())) for _ in range(M))

res = solution(N, M, pair)
print(res)