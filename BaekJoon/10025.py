# BOJ 10025 게으른 백곰
# https://www.acmicpc.net/problem/10025

from sys import stdin

def solution(N, K, ice):

    length = max([ice[i][1] for i in range(N)])
    graph = [0] * (length + 1)

    for g, x in ice:
        graph[x] = g
    
    score = sum(graph[:2*K+1])
    answer = score
    for i in range(K, length-K):
        score = score - graph[i-K] + graph[i+K+1]
        answer = max(answer, score)

    return answer

N, K, = map(int,stdin.readline().split())
ice = list(list(map(int,stdin.readline().split())) for _ in range(N))

res = solution(N, K, ice)
print(res)