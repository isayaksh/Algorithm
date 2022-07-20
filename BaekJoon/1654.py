# 1654 랜선 자르기 < 실버 2 >
from sys import stdin

def binarySearch(N, lans):
    start, end = 1, max(lans) # 시작점, 끝점
    while start <= end:
        cnt = 0 # 나누어진 랜선의 개수
        mid = (start + end) // 2 # 중앙점
        for lan in lans: cnt += lan//mid # 나누어진 랜선의 개수 합
        if cnt >= N: start = mid + 1
        else: end = mid - 1
    return end

K, N = map(int,stdin.readline().split())
lans = list(int(stdin.readline()) for _ in range(K))
print(binarySearch(N,lans))