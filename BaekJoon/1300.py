# 1300 K번째 수 < 골드 2 >
from sys import stdin

def func(N,K):
    answer = 0
    start, end = 1, N**2
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(1,N+1):
            cnt += min(N,mid//i)
        if cnt < K: start = mid + 1
        else:
            answer = mid
            end = mid - 1
    return answer

N = int(stdin.readline())
K = int(stdin.readline())
print(func(N,K))