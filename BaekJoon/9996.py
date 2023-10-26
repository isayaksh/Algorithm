# BOJ 9996 한국이 그리울 땐 서버에 접속하지
# https://www.acmicpc.net/problem/9996

from sys import stdin

def solution(N, pattern, fileNameList):
    prefix, suffix = pattern.split('*')
    length = len(pattern) - 1
    return ["DA" if (len(fileName) >= length and fileName.startswith(prefix) and fileName.endswith(suffix)) else "NE" for fileName in fileNameList]

# input
N = int(stdin.readline())
pattern = stdin.readline().strip()
fileNameList = list(stdin.readline().strip() for _ in range(N))

# result
result = solution(N, pattern, fileNameList)
print('\n'.join(result))