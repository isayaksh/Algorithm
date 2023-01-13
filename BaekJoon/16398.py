from sys import stdin
from itertools import combinations

def solution(N, L, R, X, A):
    answer = 0
    A.sort()
    for num in range(2, N+1):
        for case in combinations(A, num):
            point = sum(case) # 문제 난이도의 합
            dif = case[-1] - case[0] # 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이
            if L <= point and point <= R and dif >= X:
                answer += 1
    
    return answer

# input
N, L, R, X = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))

# result
result = solution(N, L, R, X, A)
print(result)