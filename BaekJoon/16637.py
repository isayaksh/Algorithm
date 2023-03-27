# BOJ 16637 괄호 추가하기
# https://www.acmicpc.net/problem/16637

from sys import stdin, maxsize

answer = -maxsize
def solution(N, formula):
    def dfs(idx, value):
        global answer
        if idx == N-1:
            answer = max(answer, value)
            return
        if idx + 2 < N:
            dfs(idx+2, eval(str(value) + formula[idx+1:idx+3]))
        if idx + 4 < N:
            dfs(idx+4, eval(str(value) + formula[idx+1] + str(eval(formula[idx+2:idx+5]))))
    
    dfs(0, int(formula[0]))

N = int(stdin.readline())
formula = stdin.readline().strip()

solution(N, formula)
print(answer)