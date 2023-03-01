# BOJ 16235 나무 재테크
# https://www.acmicpc.net/problem/16235

from sys import stdin
from collections import deque

def solution(N, M, K, compost, treeInfo):

    answer = 0

    area = [[5] * (N) for _ in range(N)]
    trees = [[deque() for _ in range(N)] for _ in range(N)]

    for x, y, z in treeInfo:
        trees[x-1][y-1].append(z)

    for _ in range(K):  

        # spring & summer
        for y in range(N):
            for x in range(N):
                if trees[y][x]:
                    comp = 0
                    tree = trees[y][x]
                    newTree = deque()
                    while tree:
                        z = tree.popleft()
                        if z <= area[y][x]:
                            area[y][x] -= z
                            newTree.append(z+1)
                        else:
                            comp += z//2
                    trees[y][x] = newTree
                    area[y][x] += comp
        
        # autumn & winter
        for y in range(N):
            for x in range(N):
                if trees[y][x]:
                    for t in trees[y][x]:
                        if t%5==0:
                            for dx, dy in ((-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)):
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < N and 0 <= ny < N:
                                    trees[ny][nx].appendleft(1)
                area[y][x] += compost[y][x]

    for y in range(N):
        for x in range(N):
            answer += len(trees[y][x])
    
    return answer
    

N, M, K = map(int,stdin.readline().split()) # size, tree, year
compost = [list(map(int,stdin.readline().split())) for _ in range(N)]
treeInfo = [list(map(int,stdin.readline().split()))for _ in range(M)]

result = solution(N, M, K, compost, treeInfo)
print(result)