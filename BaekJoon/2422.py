# BOJ 2422 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# https://www.acmicpc.net/problem/2422

from sys import stdin

def solution(N, M, mismatch):
    answer = 0

    impossible = [[False] * (N+1) for _ in range(N+1)]

    for ic1, ic2 in mismatch:
        ic1, ic2 = min(ic1,ic2), max(ic1, ic2)
        impossible[ic1][ic2] = True


    for i in range(1, N-1):
        for j in range(i+1, N):
            for k in range(j+1, N+1):
                if impossible[i][j] or impossible[i][k] or impossible[j][k]:
                    continue
                answer += 1
    
    return answer

    
N, M = map(int,stdin.readline().split())
mismatch = list(list(map(int,stdin.readline().split())) for _ in range(M))

res = solution(N, M, mismatch)
print(res)