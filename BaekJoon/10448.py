# BOJ 10448 유레카 이론
# https://www.acmicpc.net/problem/10448

from sys import stdin
from itertools import product

def getSumOfTriangularNumber():
    result = set()
    triangularNumbers = [n*(n+1)//2 for n in range(1,45)]
    count = 0
    for numbers in product(triangularNumbers, repeat=3):
        count += 1
        result.add(sum(numbers))
    return result

triangularNumbers = getSumOfTriangularNumber()

T = int(stdin.readline())
for _ in range(T):
    K = int(stdin.readline())
    print(1) if K in triangularNumbers else print(0)