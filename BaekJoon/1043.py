# BOJ 1043 거짓말
# https://www.acmicpc.net/problem/1043

from sys import stdin



def solution(N, M, know, party):
    answer = 0

    know = set(know[1:])
    party = list(set(p[1:]) for p in party)

    for _ in range(M):
        for p in party:
            if p & know:
                know = know | p
    
    for p in party:
        if not (p & know):
            answer += 1

    return answer

N, M = map(int,stdin.readline().split())
know = list(map(int,stdin.readline().split()))
party = list(list(map(int,stdin.readline().split())) for _ in range(M))

res = solution(N, M, know, party)
print(res)