# BOJ 17406 배열 돌리기 4
# https://www.acmicpc.net/problem/17406

from sys import stdin, maxsize
from itertools import permutations
from copy import deepcopy

def solution(N, M, K, graph, turn):
    answer = maxsize

    # 회전
    def turnning(x, y, s):
        tmp = newGraph[y-s][x-s]
        for dy in range(y-s, y+s):
            newGraph[dy][x-s] = newGraph[dy+1][x-s]
        for dx in range(x-s, x+s):
            newGraph[y+s][dx] = newGraph[y+s][dx+1]
        for dy in range(y+s, y-s, -1):
            newGraph[dy][x+s] = newGraph[dy-1][x+s]
        for dx in range(x+s, x-s, -1):
            newGraph[y-s][dx] = newGraph[y-s][dx-1]
        newGraph[y-s][x-s+1] = tmp
        if s != 1:
            turnning(x, y, s-1)
    # 회전 연산
    for case in permutations(turn, K):
        newGraph = deepcopy(graph)
        for y, x, s in case:
            turnning(x-1, y-1, s)
        answer = min(answer, min(map(sum, newGraph)))
    return answer

N, M, K = map(int,stdin.readline().split())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))
turn = list(list(map(int,stdin.readline().split())) for _ in range(K))

result = solution(N, M, K, graph, turn)
print(result)