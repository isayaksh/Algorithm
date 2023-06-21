# BOJ 1487 물건 팔기
# https://www.acmicpc.net/problem/1487

from sys import stdin

def solution(N, buyers):
    answer = 0
    totalPrice = 0
    for payment in sorted(set([buyer[0] for buyer in buyers])):
        tmpPrice = 0
        for pm, df in buyers:
            if pm >= payment and payment > df:
                tmpPrice += (payment - df)
        if totalPrice < tmpPrice:
            answer, totalPrice = payment, tmpPrice
    return answer

N = int(stdin.readline())
buyers = list(tuple(map(int,stdin.readline().split())) for _ in range(N))

res = solution(N, buyers)
print(res)