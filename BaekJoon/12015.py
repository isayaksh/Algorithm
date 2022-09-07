# 12015 가장 긴 증가하는 부분 수열 2 < 골드 2 >
from sys import stdin
from _bisect import bisect_left

def LIS(A):
    lis = [0]
    for a in A:
        if lis[-1] < a: lis.append(a)
        else: lis[bisect_left(lis,a)] = a    
    return len(lis) - 1

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

print(LIS(A))