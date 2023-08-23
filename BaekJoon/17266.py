# BOJ 17266 어두운 굴다리
# https://www.acmicpc.net/problem/17266

from sys import stdin

def solution(N, M, location):
    answer = 0
    
    def possibleLightRange(lightRange):
        if location[0] > lightRange or location[-1] + lightRange < N:
            return False
        for i in range(M-1):
            if location[i+1] - location[i] > lightRange*2:
                return False
        return True

    start, end = 0, N
    while start <= end:
        mid = (start + end) // 2
        if possibleLightRange(mid):
            end = mid-1
            answer = mid
        else:
            start = mid+1

    return answer

N = int(stdin.readline())
M = int(stdin.readline())
location = list(map(int,stdin.readline().split()))

res = solution(N, M, location)
print(res)