# 1939 중량제한 < 골드 4 >
from sys import stdin
from collections import deque, defaultdict

def solution(N, edges, arrival, departure):
    answer = [-1] * (N+1)
    answer[arrival] = 0
    graph = defaultdict(lambda : defaultdict(int)) # graph[시작점][도착점] = 중량

    # 두 개의 섬(s, e) 사이의 중량 제한 갱신
    for s, e, w in edges:
        weight = max(graph[s][e], w)
        graph[s][e] = weight
        graph[e][s] = weight
    
    # 시작섬(arrival)에서 다른 직접 연결된 섬의 중량 제한 갱신
    queue = deque()
    for node in graph[arrival]:
        answer[node] = graph[arrival][node]
        queue.append(node)

    # 다익스트라
    while queue:
        currentNode = queue.popleft()
        # 현재 섬(currentNode)이 도착섬(departure)일 경우
        if currentNode == departure:
            continue

        for nextNode in graph[currentNode]:
            # 다음 섬(nextNode)의 중량 제한 갱신이 가능한 경우
            if answer[nextNode] < min(answer[currentNode], graph[currentNode][nextNode]):
                answer[nextNode] = min(answer[currentNode], graph[currentNode][nextNode])
                queue.append(nextNode)
    
    return answer[departure]

# input
N, M = map(int,stdin.readline().split())
edges = [list(map(int,stdin.readline().split())) for _ in range(M)]
arrival, departure = map(int,stdin.readline().split())

# result
result = solution(N, edges, arrival, departure)
print(result)