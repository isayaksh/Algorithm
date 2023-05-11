# BOJ 1806 부분합
# https://www.acmicpc.net/problem/1806

from sys import stdin, maxsize

def solution(N, S, numbers):
    answer = maxsize

    # 누적합
    for i in range(1, N+1):
        numbers[i] += numbers[i-1]
    
    # 투 포인터
    start, end = 0, 1
    while end < N+1:
        num = numbers[end] - numbers[start]
        if num < S:
            end += 1
        else:
            answer = min(answer, end - start)
            start += 1

    return answer if answer != maxsize else 0

# input
N, S = map(int,stdin.readline().split())
numbers = [0] + list(map(int,stdin.readline().split()))

# result
res = solution(N, S, numbers)
print(res)