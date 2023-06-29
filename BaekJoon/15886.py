# BOJ 15886 내 선물을 받아줘 2
# https://www.acmicpc.net/problem/15886
from sys import stdin

def solution(N, road):
    answer = 0
    visited = set()

    for i in range(N):
        stack = [i]
        tmpVisited = set()
        tmpVisited.add(i)
        while stack:
            node = stack.pop()
            if road[node] == 'E' and node < N-1 and node+1 not in tmpVisited:
                tmpVisited.add(node+1)
                stack.append(node+1)
            elif road[node] == 'W' and node > 0 and node-1 not in tmpVisited:
                tmpVisited.add(node-1)
                stack.append(node-1)

        if not visited.intersection(tmpVisited):
            answer += 1
            visited = visited.union(tmpVisited)
        
    return answer

N = int(stdin.readline())
road = stdin.readline().strip()

res = solution(N, road)
print(res)