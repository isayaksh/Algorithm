# BOJ 20444 색종이와 가위
# https://www.acmicpc.net/problem/20444

from sys import stdin

def solution(n, k):
    answer = False

    # binary search
    start, end = 0, n 
    while not answer and start <= end:
        mid = (start + end) // 2
        if (mid+1) * (n-mid+1) < k:
            start = mid+1
        if (mid+1) * (n-mid+1) > k:
            end = mid-1
        if (mid+1) * (n-mid+1) == k:
            return "YES"

    return "NO"

n, k = map(int,stdin.readline().split())

res = solution(n, k)
print(res)