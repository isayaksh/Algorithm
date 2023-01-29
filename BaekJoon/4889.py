# BOJ 4889 안정적인 문자열
# https://www.acmicpc.net/problem/4889

from sys import stdin

def solution(string):
    answer = 0

    stack = []
    for s in string:
        if s == '{':
            stack.append(s)
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s)
    
    for i in range(0, len(stack), 2):
        if stack[i] != '{': answer += 1
        if stack[i+1] != '}': answer += 1

    return answer 

num = 1
while True:
    string = stdin.readline().strip()
    if '-' in string:
        break
    res = solution(string)
    print(f"{num}. {res}")
    num+=1