# BOJ 22865 가장 먼 곳
# https://www.acmicpc.net/problem/22865

from sys import stdin, maxsize
from collections import defaultdict
from heapq import heappop, heappush

def solution(N, friendList, M, edges):

    # dijkstra using heap
    def dijkstra(startNode):
        weight = [maxsize] * (N+1)
        weight[0], weight[startNode] = 0, 0

        heap = [(0, startNode)]
        while heap:
            currentWeight, currentNode = heappop(heap)
            for nextNode, nextWeight in graph[currentNode]:
                if weight[nextNode] > currentWeight + nextWeight:
                    weight[nextNode] = currentWeight + nextWeight
                    heappush(heap, (currentWeight + nextWeight, nextNode))
        
        return weight

    # init graph
    graph = defaultdict(list)
    for D, E, L in edges:
        graph[D].append((E, L))
        graph[E].append((D, L))

    # find the length using dijkstra algorithm 
    lengthList = [dijkstra(friend) for friend in friendList]
    
    # find the minimum length
    answer, comparison = 0, 0
    for i in range(1, N+1):
        minLength = min(lengthList[0][i], lengthList[1][i], lengthList[2][i])
        if comparison < minLength:
            answer, comparison = i, minLength

    return answer
    
# input
N = int(stdin.readline())
friendList = list(map(int,stdin.readline().split()))
M = int(stdin.readline())
edges = list(list(map(int,stdin.readline().split())) for _ in range(M))

# result
result = solution(N, friendList, M, edges)
print(result)