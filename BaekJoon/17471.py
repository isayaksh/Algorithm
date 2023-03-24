# BOJ 17471 게리맨더링
# https://www.acmicpc.net/problem/17471

from sys import stdin, maxsize
from itertools import combinations

def solution(N, population, edges):

    answer = maxsize
    totalArea = set([i for i in range(1, N+1)])

    def check(A, B):
        visited = [True] + [False] * N
        for b in B: visited[b] = True
        visited[A[0]] = True
        stack = [A[0]]
        while stack:
            node = stack.pop()
            for nextNode in range(1, N+1):
                if graph[node][nextNode] and not visited[nextNode]:
                    visited[nextNode] = True
                    stack.append(nextNode)
        if not all(visited):
            return False
        visited = [True] + [False] * N
        for a in A: visited[a] = True
        visited[B[0]] = True
        stack = [B[0]]
        while stack:
            node = stack.pop()
            for nextNode in range(1, N+1):
                if graph[node][nextNode] and not visited[nextNode]:
                    visited[nextNode] = True
                    stack.append(nextNode)
        if not all(visited):
            return False
        return True

    # 그래프 초기화
    graph = [[False] * (N+1) for _ in range(N+1)]
    for n1 in range(1, N+1):
        for n2 in edges[n1][1:]:
            graph[n1][n2], graph[n2][n1] = True, True

    # 전수 조사
    for i in range(1, N//2+1):
        for A in combinations(range(1, N+1), i):
            B = tuple(totalArea.difference(A))
            if check(A, B):
                answer = min(answer, abs(sum([population[a] for a in A]) - sum([population[b] for b in B])))
    
    return answer

# input
N = int(stdin.readline())
population = [0] + list(map(int,stdin.readline().split()))
edges = [0] + list(list(map(int,stdin.readline().split())) for _ in range(N))

# result
result = solution(N, population, edges)
print(result) if result != maxsize else print(-1)