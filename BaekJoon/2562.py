# BOJ 2562 최댓값
# https://www.acmicpc.net/problem/2562

from sys import stdin

def solution(numbers):
    answer = [-1, -1]
    for i in range(9):
        if answer[0] < numbers[i]:
            answer = [numbers[i], i+1]
    return answer 

numbers = list(int(stdin.readline()) for _ in range(9))

value, idx = solution(numbers)
print(value)
print(idx)