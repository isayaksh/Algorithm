# BOJ 9342 염색체
# https://www.acmicpc.net/problem/9342

from sys import stdin

def solution(word):
    N = len(word)

    # 문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
    if word[0] not in ('A', 'B', 'C', 'D', 'E', 'F'):
        return "Good"
    
    idx = 0 if word[0] == 'A' else 1

    # 그 다음에는 A가 하나 또는 그 이상 있어야 한다.
    while idx < N and word[idx] == 'A':
        idx+= 1
    
    # 그 다음에는 F가 하나 또는 그 이상 있어야 한다.
    while idx < N and word[idx] == 'F':
        idx+= 1

    # 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
    while idx < N and word[idx] == 'C':
        idx+= 1
    
    # 그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.
    if word[-1] not in ('A', 'B', 'C', 'D', 'E', 'F'):
        return "Good"
    
    return "Infected!" if idx == N else "Good"

for _ in range(int(stdin.readline())):
    word = stdin.readline().strip()
    res = solution(word)
    print(res)