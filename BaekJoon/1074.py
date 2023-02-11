# BOJ 1074 Z
# https://www.acmicpc.net/problem/1074

from sys import stdin

def solution(N, y, x):
    answer = 0
    quaterBoxSize = 2**((N-1)*2) # N에 해당하는 1/4 박스크기
    halfLength = 2**(N-1) # N에 해당하는 박스 1/2 길이
    while N > 0:
        answer += ( quaterBoxSize * 2 * (y // halfLength) + quaterBoxSize * (x // halfLength) )
        N, y, x = N - 1, y % halfLength, x % halfLength
        quaterBoxSize //= 4
        halfLength //= 2
    return answer

# request
N, y, x = map(int,stdin.readline().split())

# response
response = solution(N, y, x)
print(response)