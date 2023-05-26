# BOJ 2469 사다리 타기
# https://www.acmicpc.net/problem/2469

from sys import stdin

def solution(k, n, target, ladder):
    answer = ['*' for _ in range(k-1)]
    participant = list(chr(i) for i in range(65, 65+k))

    # up > down
    for row in range(n):
        if ladder[row][0] == '?': break
        for col in range(k-1):
            if ladder[row][col] == '-':
                participant[col], participant[col+1] = participant[col+1], participant[col]

    # down > up
    for row in range(n-1, 0, -1):
        if ladder[row][0] == '?': break
        for col in range(k-1):
            if ladder[row][col] == '-':
                target[col], target[col+1] = target[col+1], target[col]

    # check
    for col in range(k-1):
        if participant[col] != target[col]:
            if participant[col+1] == target[col]:
                participant[col], participant[col+1] = participant[col+1], participant[col]
                answer[col] = '-'
            else:
                return 'x'*(k-1)

    return ''.join(answer)

# input
k = int(stdin.readline())
n = int(stdin.readline())
target = list(stdin.readline().strip())
ladder = list(list(stdin.readline().strip()) for _ in range(n))
participant = list(chr(i) for i in range(65, 65+k))

# result 
res = solution(k, n, target, ladder)
print(res)