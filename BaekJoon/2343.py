# BOJ 2343 기타 레슨
# https://www.acmicpc.net/problem/2343


from sys import stdin

def solution(N, M, length):

    # 블루레이의 개수가 1개일 경우
    if M == 1:
        return sum(length)

    # 가장 긴 녹화 길이
    maxLength = max(length)
    
    # 누적 녹화 길이
    for i in range(1,N):
        length[i] += length[i-1]
    
    # 이진 탐색
    start, end = 1, sum(length)
    while start <= end:
        mid = (start + end) // 2

        # 블루레이의 길이가 가장 긴 녹화 길이보다 짧은 경우
        if mid < maxLength:
            start = mid + 1
            continue

        m, std = 1, 0
        for i in range(N):
            if length[i] - std > mid:
                std = length[i-1]
                m += 1
        if M < m:
            start = mid + 1
        else:
            end = mid - 1
    
    return start

# input
N, M = map(int,stdin.readline().split())
length = list(map(int,stdin.readline().split()))

# result
result = solution(N, M, length)
print(result)