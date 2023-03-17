# BOJ 11559 Puyo Puyo
# https://www.acmicpc.net/problem/11559

from sys import stdin

def solution(graph):
    answer = 0
    # 연쇄 연산
    def chain(x, y, color):
        visited[y][x] = True
        result = [(x, y)]
        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 6 and 0 <= ny < 12 and graph[ny][nx] == color and not visited[ny][nx]:
                result += chain(nx, ny, color)
        return result
    # 아래로 정렬 연산
    def fallDown(x, y):
        graph[y][x], graph[y+1][x] = graph[y+1][x], graph[y][x]
        if y + 2 < 12 and graph[y+2][x] == '.':
            fallDown(x, y+1)
    
    while True:
        visited = [[False] * 6 for _ in range(12)]
        flag = False
        # 연쇄 연산
        for y in range(12):
            for x in range(6):
                if graph[y][x] != '.' and not visited[y][x]:
                    result = chain(x, y, graph[y][x])
                    # 뿌요 4개 이상 연결 시 뿌요 제거
                    if len(result) >= 4:
                        for x, y in result:
                            graph[y][x] = '.'
                        flag = True
        # 연쇄 작용 없다면 프로그램 종료
        if not flag:
            break
        answer += 1
        # 아래로 떨어지는 연산
        for y in range(10, -1, -1):
            for x in range(6):
                if graph[y][x] != '.' and graph[y+1][x] == '.':
                    fallDown(x,y)
    return answer

# input
graph = list(list(stdin.readline().strip()) for _ in range(12))

# result
result = solution(graph)
print(result)