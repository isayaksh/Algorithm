# BOJ 2143 두 배열의 합
# https://www.acmicpc.net/problem/2143

from sys import stdin
from collections import defaultdict

def solution(T, n, A, m, B):
    answer = 0
    dictA, dictB = defaultdict(int), defaultdict(int)
    dictA[A[0]] += 1
    dictB[B[0]] += 1

    for i in range(1, n):
        A[i] += A[i-1]
        dictA[A[i]] += 1
        for j in range(i):
            dictA[A[i] - A[j]] += 1
    for i in range(1, m):
        B[i] += B[i-1]
        dictB[B[i]] += 1
        for j in range(i):
            dictB[B[i] - B[j]] += 1
    
    keyA, keyB = dictA.keys(), set(dictB.keys())
    for key in keyA:
        if T-key in keyB:
            answer += dictA[key] * dictB[T-key]
    
    return answer

T = int(stdin.readline())
n = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
m = int(stdin.readline())
B = list(map(int,stdin.readline().split()))

result = solution(T, n, A, m, B)
print(result)