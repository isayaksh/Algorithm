# BOJ 2435 기상청 인턴 신현수
# https://www.acmicpc.net/problem/2435

from sys import stdin

def solution(N, K, temperature):
    totalTemperature = sum(temperature[:K])
    answer = totalTemperature
    for i in range(K, N):
        totalTemperature += temperature[i] - temperature[i-K]
        answer = max(answer, totalTemperature)
    return answer

N, K = map(int,stdin.readline().split())
temperature = list(map(int,stdin.readline().split()))

res = solution(N, K, temperature)
print(res)