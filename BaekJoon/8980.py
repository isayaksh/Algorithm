# BOJ 8980 택배
# https://www.acmicpc.net/problem/8980

from sys import stdin

def solution(N, C, M, trackingInfomations):

    answer = 0
    currentWeight = [C] * (N+1)
    trackingInfomations.sort(key=lambda x : ((x[1])))

    for start, end, weight in trackingInfomations:
        availableWeight = min(weight, min(currentWeight[start:end]))
        answer += availableWeight
        for node in range(start, end):
            currentWeight[node] -= availableWeight
    return answer

N, C = map(int,stdin.readline().split())
M = int(stdin.readline())
trackingInfomations = list(list(map(int,stdin.readline().split())) for _ in range(M))

result = solution(N, C, M, trackingInfomations)
print(result)