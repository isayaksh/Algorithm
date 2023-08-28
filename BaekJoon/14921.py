# BOJ 14921 용액 합성하기
# https://www.acmicpc.net/problem/14921

from sys import stdin, maxsize

def solution(N, A):
    answer = maxsize

    # sort 
    A.sort()

    # two point search
    start, end = 0, N-1
    while start < end:
        value = A[start] + A[end]
        if value < 0:
            start += 1
        if value > 0:
            end -= 1
        if value == 0:
            return 0
        if abs(value) < abs(answer):
            answer = value

    return answer

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

res = solution(N, A)
print(res)