# BOJ 10830 행렬 제곱
# https://www.acmicpc.net/problem/10830

from sys import stdin
from collections import defaultdict

def solution(N, B, A):

    for i in range(N):
        for j in range(N):
            if A[i][j] == 1000:
                A[i][j] = 0

    dictionary = defaultdict(list)
    dictionary[1] = A

    # A행렬 * B행렬
    def matrixSquared(A, B):
        tmp = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                tmp[j][i] = sum(B[j][k] * A[k][i] for k in range(N)) % 1000
        return tmp
    
    # 분할 정복
    def divideQunquer(N):
        if not dictionary[N]:
            res = matrixSquared(divideQunquer(N//2), divideQunquer(N//2+N%2))
            dictionary[N] = res
            return res
        else:
            return dictionary[N]

    divideQunquer(B)

    return dictionary[B]

# input
N, B = map(int,stdin.readline().split())
A = [list(map(int,stdin.readline().split())) for _ in range(N)]

# result
result = solution(N, B, A)
for res in result:
    print(*res)