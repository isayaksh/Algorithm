# BOJ 15685 드래곤 커브
# https://www.acmicpc.net/problem/15685

from sys import stdin

direct = [(1,0), (0,-1), (-1,0), (0,1)]

def dragonCurve(x, y, d, g):
    order = [d]
    for i in range(g):
        newOrder = list(reversed(order))
        for i in range(len(newOrder)):
            newOrder[i] = (newOrder[i] + 1) % 4
        order.extend(newOrder)
    graph[y][x] = '#'
    for o in order:
        x, y = x + direct[o][0], y + direct[o][1]
        graph[y][x] = '#'   

answer = 0
graph = [['.'] * 101 for _ in range(101)]

N = int(stdin.readline())
for _ in range(N):
    x, y, d, g = map(int,stdin.readline().split())
    dragonCurve(x, y, d, g)

for y in range(100):
    for x in range(100):
        if graph[y][x] == '#' and graph[y+1][x] == '#' and graph[y][x+1] == '#' and graph[y+1][x+1] == '#':
            answer += 1

print(answer)