# BOJ 18353 병사 배치하기
# https://www.acmicpc.net/problem/18353

from sys import stdin
from bisect import bisect_left

def solution(N, soldiers):
    answer = [0]
    for i in range(N-1, -1, -1):
        soldier = soldiers[i]
        idx = bisect_left(answer, soldier)
        try:
            answer[idx] = soldier
        except:
            answer.append(soldier)

    return N - (len(answer) - 1)

N = int(stdin.readline())
soldiers = list(map(int,stdin.readline().split()))

res = solution(N, soldiers)
print(res)