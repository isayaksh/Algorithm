# BOJ 1992 쿼드트리
# https://www.acmicpc.net/problem/1992

from sys import stdin

def solution(N, graph):

    def check(x, y, n):
        for dy in range(y, y+n):
            for dx in range(x, x+n):
                if graph[y][x] != graph[dy][dx]:
                    return False
        return True

    def dfs(x, y, N):
        result = ''
        if check(x, y, N):
            return graph[y][x]
        for dy in (y, y+N//2):
            for dx in (x, x+N//2):
                result+=(dfs(dx, dy, N//2))
        return '('+result+')'
    
    return dfs(0, 0, N)

N = int(stdin.readline())
graph = [list(stdin.readline().strip()) for _ in range(N)]

result = solution(N, graph)
print(result)