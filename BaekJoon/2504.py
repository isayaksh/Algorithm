# BOJ 2504 괄호의 값
# https://www.acmicpc.net/problem/2504

from sys import stdin
def solution(bracket):
    stack = []
    
    for b in bracket:
        stack.append(b)

        while True:
            # '(', ')'
            if len(stack) >= 2 and (stack[-2], stack[-1]) == ('(',')'):
                stack = stack[:-2] + ['2']
                continue
            # '[', ']'
            if len(stack) >= 2 and (stack[-2], stack[-1]) == ('[',']'):
                stack = stack[:-2] + ['3']
                continue
            # '숫자', '숫자'
            if len(stack) >= 2 and stack[-1].isdigit() and stack[-2].isdigit():
                stack = stack[:-2] + [str(int(stack[-1]) + int(stack[-2]))]
                continue
            # '(', '숫자', ')'
            if len(stack) >= 3 and stack[-3] == '(' and stack[-2].isdigit() and stack[-1] == ')':
                stack = stack[:-3] + [str(int(stack[-2]) * 2)]
                continue
            # '[', '숫자', ']'
            if len(stack) >= 3 and stack[-3] == '[' and stack[-2].isdigit() and stack[-1] == ']':
                stack = stack[:-3] + [str(int(stack[-2]) * 3)]
                continue
            break
    return int(stack[0]) if (len(stack) == 1 and stack[0].isdigit()) else 0

bracket = list(stdin.readline().strip())

result = solution(bracket)
print(result)