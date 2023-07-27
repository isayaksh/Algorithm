# BOJ 13305 주유소
# https://www.acmicpc.net/problem/13305

from sys import stdin

def solution(N, distances, gas_station):
    answer, min_gas_price = 0, gas_station[0]
    for i in range(1, N):
        answer += min_gas_price * distances[i-1]
        min_gas_price = min(min_gas_price, gas_station[i])
    return answer

N = int(stdin.readline())
distances = list(map(int,stdin.readline().split()))
gas_station = list(map(int,stdin.readline().split()))

res = solution(N, distances, gas_station)
print(res)