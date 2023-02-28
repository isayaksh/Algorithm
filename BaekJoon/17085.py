# BOJ 17085 십자가 2개 놓기
# https://www.acmicpc.net/problem/17085

from sys import stdin

def solution(N, M, graph):

    answer = 0
    crosses = []

    def check(cross):
        for x, y in cross:
            if x < 0 or x >= M or y < 0 or y >= N or graph[y][x] != '#':
                return False
        return True

    def getCorssSize(x, y):
        size = 0
        while check([(x + dx*size, y + dy*size) for dx, dy in ((1,0), (0,1), (-1,0), (0,-1))]):
            size += 1
        return size
    
    def chceckDuplicate(c1, c2):
        board = [[0] * M for _ in range(N)]
        x1, y1, s1 = c1
        x2, y2, s2 = c2
        
        for s in range(s1+1):
            board[y1+s][x1] = 1
            board[y1-s][x1] = 1
            board[y1][x1+s] = 1
            board[y1][x1-s] = 1
        for s in range(s2+1):
            if board[y2+s][x2] == 1 or board[y2-s][x2] == 1 or board[y2][x2+s] == 1 or board[y2][x2-s] == 1:
                return False
        return True

    for y in range(N):
        for x in range(M):
            if graph[y][x] == '#':
                size = getCorssSize(x, y)
                for i in range(size):
                    crosses.append((x, y, i))
    
    n = len(crosses)

    for i in range(n-1):
        for j in range(i+1, n):
            tmp = (1+4*crosses[i][2]) * (1+4*crosses[j][2])
            if answer < tmp and chceckDuplicate(crosses[i], crosses[j]):
                answer = tmp
    return answer

N, M = map(int,stdin.readline().split())
graph = list(list(stdin.readline().strip()) for _ in range(N))

result = solution(N, M, graph)
print(result)