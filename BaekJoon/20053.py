# BOJ 20053 최소, 최대 2
# https://www.acmicpc.net/problem/20053

from sys import stdin

def solution(N, number):
    return min(number), max(number)

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    number = list(map(int,stdin.readline().split()))
    minNumber, maxNumber = solution(N, number)
    print(minNumber, maxNumber)