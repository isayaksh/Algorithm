# BOJ 2615 오목
# https://www.acmicpc.net/problem/2615
from sys import stdin

def solution(graph):

    def checkOmok(x, y, dx, dy):
        # 1~5번 바둑알 일치 확인
        for i in range(1, 5):
            nx, ny = x + dx*i, y +dy*i
            if nx < 0 or nx >= 19 or ny < 0 or ny >= 19 or graph[y][x] != graph[ny][nx]:
                return False
            
        # 0번 바둑알 불일치 확인
        nx, ny = x - dx, y - dy
        if 0 <= nx < 19 and 0 <= ny < 19 and graph[y][x] == graph[ny][nx]:
            return False
        
        # 6번 바둑알 불일치 확인
        nx, ny = x + 5*dx, y + 5*dy
        if 0 <= nx < 19 and 0 <= ny < 19 and graph[y][x] == graph[ny][nx]:
            return False
        
        return True

    for y in range(19):
        for x in range(19):
            if graph[y][x] != 0:
                for dx, dy in ((1, -1), (1, 0), (1, 1), (0, 1)):
                    if checkOmok(x, y, dx, dy):
                        print(graph[y][x])
                        print(y+1, x+1)
                        exit()
    print(0)    

graph = list(list(map(int,stdin.readline().split())) for _ in range(19))
solution(graph)