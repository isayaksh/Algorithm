# BOJ 21920 서로소 평균
# https://www.acmicpc.net/problem/21920

from sys import stdin
from math import sqrt

def solution(N, A, X):

    def checkCoprimeIntegers(a):
        for div in division:
            if a%div == 0:
                return False
        return True

    # X의 약수
    division = {X}
    for div in range(2, int(sqrt(X)) + 1):
        if X % div == 0:
            division.add(div)
            division.add(X//div)
    
    # 서로소 확인
    answer = []
    for a in A:
        if checkCoprimeIntegers(a):
            answer.append(a)

    return sum(answer)/len(answer)

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
X = int(stdin.readline())

res = solution(N, A, X)
print(res)