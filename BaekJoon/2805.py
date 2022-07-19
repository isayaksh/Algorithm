# 2805 나무 자르기 < 실버 2 >
from sys import stdin

def binSearch(start,end):
    while start <= end:
        mid = (start + end) // 2 # 중앙값
        m = 0 # 자른 나무의 합
        for tree in trees:
            if tree <= mid: break
            m += tree - mid
        if m >= M: start = mid + 1
        else: end = mid - 1
    return end

N, M = map(int,stdin.readline().split())
trees = list(map(int,stdin.readline().split()))
trees.sort(reverse=True) # 내림차순으로 정렬
print(binSearch(0, max(trees)))