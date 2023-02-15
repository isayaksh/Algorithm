# BOJ 14889 스타트와 링크
# https://www.acmicpc.net/problem/14889

from sys import stdin, maxsize
from itertools import combinations

def solution(N, graph):
    answer = maxsize
    # start팀, link팀 나누기
    for team in combinations(range(N), N//2):
        stat = 0
        # start팀 능력치
        for a, b in combinations(team, 2):
            stat += graph[a][b] + graph[b][a]
        # link팀 능력치
        for a, b in combinations(set(range(N)) - set(team), 2):
            stat -= graph[a][b] + graph[b][a]
        # 팀의 능력치의 차이
        answer = min(answer, abs(stat))
    return answer

N = int(stdin.readline())
graph = [list(map(int,stdin.readline().split())) for _ in range(N)]

result = solution(N, graph)
print(result)