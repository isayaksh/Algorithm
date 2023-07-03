# BOJ 15779 Zigzag
# https://www.acmicpc.net/problem/15779

from sys import stdin

def solution(N, A):
    answer = [2] * N
    for i in range(2, N):
        # 단조증가 수열이거나, 단조감소 수열인 경우
        if (A[i-2] <= A[i-1] <= A[i]) or (A[i-2] >= A[i-1] >= A[i]): continue
        # 지그재그 수열인 경우
        answer[i] = answer[i-1] + 1
    return max(answer)

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

res = solution(N, A)
print(res)