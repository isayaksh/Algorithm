# BOJ 2160 그림 비교
# https://www.acmicpc.net/problem/2160

from sys import stdin, maxsize

def solution(N, draws):
    answer = [0, 0]
    minCount = maxsize

    def countDiffCells(i, j):
        return sum(1 for c in range(35) if draws[i][c] != draws[j][c])
    
    minCount, answer = min((countDiffCells(i, j), [i+1, j+1]) for i in range(N-1) for j in range(i+1, N))

    return answer

N = int(stdin.readline())
draws = list(''.join(stdin.readline().strip() for _ in range(5)) for _ in range(N))

i, j = solution(N, draws)
print(i, j)