# 21758 꿀 따기 < 골드 5 >
from sys import stdin

def solution(N, arr):

    answer = 0
    total = sum(arr)
    
    # case1 : B B H
    value = 2 * (total - (arr[0] + arr[1]))
    answer = max(answer, value)
    for i in range(2,N):
        value += (arr[i-1] - arr[i]*2)
        answer = max(answer, value)

    # case2 : H B B
    value = 2 * (total - (arr[-1] + arr[-2]))
    answer = max(answer, value)
    for i in range(N-2, 1, -1):
        value += (arr[i] - arr[i-1]*2)
        answer = max(answer, value)

    # case3 : B H B
    value = arr[1] + total - (arr[0] + arr[-1])
    answer = max(answer, value)
    for i in range(2, N-2):
        value += (arr[i] - arr[i-1])
        answer = max(answer, value)

    return answer

# input
N = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))

# result
result = solution(N, arr)
print(result)