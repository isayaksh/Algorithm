# BOJ 2096 내려가기
# https://www.acmicpc.net/problem/2096

from sys import stdin

# input
N = int(stdin.readline())
maxGraph = [0] * 3
minGraph = [0] * 3

for y in range(N):
    maxTmp = [0] * 3
    minTmp = [0] * 3
    n = list(map(int,stdin.readline().split()))
    for x in range(3):
        if x == 0:
            maxTmp[x] = max(maxGraph[:2])
            minTmp[x] = min(minGraph[:2])
        elif x == 1:
            maxTmp[x] = max(maxGraph)
            minTmp[x] = min(minGraph)
        elif x == 2:
            maxTmp[x] = max(maxGraph[1:])
            minTmp[x] = min(minGraph[1:])
    for i in range(3):
        maxGraph[i] = n[i] + maxTmp[i]
        minGraph[i] = n[i] + minTmp[i]
print(max(maxGraph), min(minGraph))