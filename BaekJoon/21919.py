# BOJ 21919 소수 최소 공배수
# https://www.acmicpc.net/problem/21919

from sys import stdin
from math import sqrt
from functools import reduce

def getPrimeNumberList(maxsize):
    primeNumberList = [True] * maxsize
    for i in range(2, int(sqrt(maxsize))+1):
        if primeNumberList[i]:
            for j in range(i*2, maxsize, i):
                primeNumberList[j] = False
    return primeNumberList

def solution(N, A):
    primeNumberList = getPrimeNumberList(max(A)+1)
    primeNumbers = set()
    for a in A:
        if primeNumberList[a]:
            primeNumbers.add(a)
    
    return reduce(lambda x, y: x*y, primeNumbers) if primeNumbers else -1
    
N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

res = solution(N, A)
print(res)