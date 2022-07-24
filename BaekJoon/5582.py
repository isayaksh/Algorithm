# 5582 공통 부분 문자열
from sys import stdin
S1 = stdin.readline().strip()
S2 = stdin.readline().strip()

result = 0 # 최장 공통 부분 문자열 길이
N1, N2 = len(S1), len(S2)
lst = [[0 for _ in range(N1+1)] for _ in range(N2+1)]
for y in range(1,N2+1):
    for x in range(1,N1+1):
        # 현재 문자 비교
        if S1[x-1] == S2[y-1]: # 같을 경우
            lst[y][x] = lst[y-1][x-1] + 1 # 현재 문자열의 이전의 이어진 문자열 길이 + 1
            result = max(result, lst[y][x]) # 현재까지 이어진 문자열 중 가장 긴 문자열 저장
        else: # 다를 경우
            lst[y][x] = 0 # 공통 부분 문자열 길이 0으로 초기화
print(result)