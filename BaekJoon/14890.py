# BOJ 14890 경사로
# https://www.acmicpc.net/problem/14890

from sys import stdin
from collections import deque

def solution(N, L, graph):
    answer = 0

    def possible(road):
        visited = [False] * N
        for i in range(1, N):
            # 평지 or 경사로 건설
            if road[i] == road[i-1] or visited[i]:
                continue
            # 절벽
            if abs(road[i] - road[i-1]) > 1:
                return 0
            # 왼쪽 설치
            if road[i] == road[i-1] + 1:
                # 설치 공간 부족
                if i - L < 0:
                    return 0
                for j in range(i-L, i):
                    if road[j] != road[i] - 1 or visited[j]:
                        return 0
                    visited[j] = True
            # 오른쪽 설치
            if road[i] == road[i-1] - 1:
                # 설치 공간 부족
                if i + L > N:
                    return 0
                for j in range(i, i+L):
                    if road[i-1] != road[j] + 1:
                        return 0
                    visited[j] = True
        return 1
            
    for i in range(N):
        answer += possible(graph[i])
        answer += possible([graph[j][i] for j in range(N)])

    return answer

# input
N, L = map(int,stdin.readline().split())
graph = [list(map(int,stdin.readline().split())) for _ in range(N)]

# response
response = solution(N, L, graph)
print(response)