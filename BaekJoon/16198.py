# BOJ 16198 에너지 모으기
# https://www.acmicpc.net/problem/16198

from sys import stdin

answer = 0
def dfs(W, energy):
    if len(W) == 2:
        global answer
        answer = max(answer, energy)
        return
    for i in range(1, len(W)-1):
        dfs(W[:i]+W[i+1:], energy + W[i-1] * W[i+1])

N = int(stdin.readline())
W = list(map(int,stdin.readline().split()))

dfs(W, 0)
print(answer)