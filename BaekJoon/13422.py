# BOJ 13422 도둑
# https://www.acmicpc.net/problem/13422

from sys import stdin

def solution(N, M, K, money):
    if N == M:
        return 1 if sum(money) < K else 0

    answer = 0
    totalMoney = sum(money[:M])
    for i in range(N):
        totalMoney = totalMoney - money[i] + money[(i+M)%N]
        if totalMoney < K:
            answer += 1
    return answer

T = int(stdin.readline())
for _ in range(T):
    N, M, K = map(int,stdin.readline().split())
    money = list(map(int,stdin.readline().split()))
    res = solution(N, M, K, money)
    print(res)