# BOJ 2559 수열
# https://www.acmicpc.net/problem/2559

from sys import stdin, maxsize

def solution(N, K, temperatures):
    answer = -maxsize
    total = sum(temperatures[:K])
    # 구간합
    for i in range(K, N+1):
        total = total - temperatures[i-K] + temperatures[i]
        answer = max(answer, total)
    return answer

# input
N, K = map(int,stdin.readline().split())
temperatures = [0] + list(map(int,stdin.readline().split()))

# result
result = solution(N, K, temperatures)
print(result)