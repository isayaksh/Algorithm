# BOJ 18870 좌표 압축
# https://www.acmicpc.net/problem/18870

from sys import stdin

def solution(N, X):
    sortedX = list(sorted(set(X)))
    newX = {sortedX[i] : i for i in range(len(sortedX))}
    return [newX[x] for x in X]

N = int(stdin.readline())
X = list(map(int,stdin.readline().split()))

result = solution(N, X)
print(*result)