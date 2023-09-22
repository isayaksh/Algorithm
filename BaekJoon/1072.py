# BOJ 1072 게임
# https://www.acmicpc.net/problem/1072

from sys import stdin

def solution(X, Y):
    answer = 0
    target = int(Y*100/X) + 1

    if target > 99: return -1

    # binary search
    start, end = 1, 1000000000
    while start <= end:
        mid = (start + end) // 2
        if (Y+mid)/(X+mid)*100 >= target:
            answer = mid
            end = mid-1
        else:
            start = mid+1

    return answer

X, Y = map(int,stdin.readline().split())

res = solution(X, Y)
print(res)