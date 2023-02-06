# BOJ 1107 리모컨
# https://www.acmicpc.net/problem/1107

from sys import stdin
from itertools import product

def solution(target, button):
    
    answer = abs(target - 100)

    # 중복 순열을 통한 숫자 버튼을 이용해 이동할 수 있는 모든 경우
    cases = set()
    for i in range(1,7):
        cases = cases.union(set(int("".join(case)) for case in product(button, repeat=i)))
    
    # 최소 이동 횟수 갱신
    for case in cases:
        move = len(str(case)) + abs(target - case)
        if answer > move: answer = move

    return answer

# input
target = int(stdin.readline())
M = int(stdin.readline())
if M != 0: button = list(set([str(i) for i in range(10)]) - set(stdin.readline().strip().split()))
else: button = list(str(i) for i in range(10))

# response
response = solution(target, button)
print(response)