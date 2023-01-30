# BOJ 2252 줄 세우기
# https://www.acmicpc.net/problem/2252

from sys import stdin
from collections import defaultdict, deque

def solution(N, AB):
    answer = []

    graph = defaultdict(list) # 정점 연결 정보
    degree = [0 for i in range(N+1)] # 정점 진입 차수

    for A, B in AB:
        degree[B] += 1 # 정점 진입 차수 갱신
        graph[A].append(B) # 정점 연결 정보 갱신

    # 진입 차수가 0인 정점으로 구성된 우선순위 큐 생성
    queue = deque()
    for i in range(1,N+1):
        if degree[i] == 0:
            queue.append(i)
    
    # 위상 정렬
    while queue:
        node = queue.popleft()
        answer.append(node) 
        # 현재 정점(node)에 연결된 모든 정점(nextNode)
        for nextNode in graph[node]:
            # 연결된 정점(nextNode)의 진입차수 -1
            degree[nextNode] -= 1
            # 진입 차수가 0인 즉, 현재 자신보다 큰 학생이 없는 경우
            if degree[nextNode] == 0:
                # queue에 추가
                queue.append(nextNode)

    return answer

N, M = map(int,stdin.readline().split())
AB = [list(map(int,stdin.readline().split())) for _ in range(M)]

result = solution(N, AB)
print(*result)