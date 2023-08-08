# BOJ 2302 극장 좌석
# https://www.acmicpc.net/problem/2302

from sys import stdin

def solution(N, M, fixSeat):
    answer = 1

    dp = [1, 1, 2] + [0] * 38
    for i in range(3, 41): dp[i] = dp[i-1] + dp[i-2]
    
    if fixSeat[-1] != N:
        fixSeat += [N+1]
        M+=1
    
    for i in range(M):
        answer *= dp[fixSeat[i+1] - fixSeat[i] - 1]
    
    return answer

N = int(stdin.readline())
M = int(stdin.readline())
fixSeat = [0] + list(int(stdin.readline()) for _ in range(M))

res = solution(N, M, fixSeat)
print(res)