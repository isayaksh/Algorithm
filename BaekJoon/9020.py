# BOJ 9020 골드바흐의 추측
# https://www.acmicpc.net/problem/9020

from sys import stdin

def solution(n):
    a, b = n//2, n//2+n%2
    while not (a in primeNumber and b in primeNumber):
        a, b = a-1, b+1
    return a, b

number = [True] * 10001
for i in range(2, 101):
    if number[i]:
        for j in range(i*2, 10001, i):
            number[j] = False
primeNumber = set([i for i in range(2, 10001) if number[i]])

# input
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    # result
    print(*solution(n))