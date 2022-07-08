# 11478 서로 다른 부분 문자열의 개수 < 실버 3 >
from sys import stdin
def getSubString(S):
    N = len(S)
    subString = set() # 중복 제거를 위한 집합 자료구조 사용
    for i in range(N):
        for j in range(i,N):
            subString.add(''.join(S[i:j+1])) # 슬라이스를 통해 모든 경우의 문자열 원소 집합에 추가
    return subString

S = list(stdin.readline().strip())
print(len(getSubString(S)))