# BOJ 1780 종이의 개수
# https://www.acmicpc.net/problem/1780

from sys import stdin

def solution(N, graph):
    answer = {-1: 0, 0: 0, 1: 0}

    # 종이가 모두 같은 수로 구성되어 있는가?
    def check(x, y, N):
        std = graph[y][x]
        for ny in range(y,y+N):
            for nx in range(x,x+N):
                if std != graph[ny][nx]:
                    return False
        return True

    # 분할 정복
    def divideConquer(x, y, N):
        if check(x, y, N):
            answer[graph[y][x]] += 1
            return
        # 같은 크기의 종이 9개로 분할
        N//=3
        for dy in range(3):
            for dx in range(3):
                divideConquer(x+N*dx, y+N*dy, N)

    divideConquer(0, 0, N)

    return answer.values()

N = int(stdin.readline())
graph = [list(map(int,stdin.readline().split())) for _ in range(N)]

result = solution(N, graph)
for res in result:
    print(res)