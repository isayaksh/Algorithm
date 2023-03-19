# BOJ 12738 가장 긴 증가하는 부분 수열 3
# https://www.acmicpc.net/problem/12738

from sys import stdin
from _bisect import bisect_left

def soluton(N, A):
    result = [A[0]]
    for a in A:
        if result[-1] < a: result.append(a)
        else: result[bisect_left(result, a)] = a     
    return len(result)
        
N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

result = soluton(N, A)
print(result)