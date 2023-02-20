# BOJ 1963 소수 경로
# https://www.acmicpc.net/problem/1963

from sys import stdin
from collections import deque

def getPrimeNumber():
    # 소수 집합
    primeNumber = set([i for i in range(2, 10000)])
    # 에라토스테네스의 체
    for number in range(2, 10000):
        if number in primeNumber:
            for i in range(2*number, 10000, number):
                primeNumber.discard(i)
    # 1000 미만의 비밀번호 제외
    return primeNumber & set([i for i in range(1000, 10000)])

def solution(A, B):
    queue = deque([(A, 0)])
    visited = set()
    while queue:
        a, cnt = queue.popleft()
        # A → B 도달
        if a == B: return cnt
        # 전수 조사
        strA = str(a)
        for i in range(4):
            for j in range(0, 10):
                # 1000 미만의 비밀번호 생성 불가
                if i == 0 and j == 0: continue 
                convertA = int(strA[:i] + str(j) + strA[i+1:])
                # convertA가 소수이면서 변경된 적 없는 수 일 경우
                if convertA in primeNumber and convertA not in visited:
                    visited.add(convertA)
                    queue.append((convertA, cnt+1))
    return "Impossible"

primeNumber = getPrimeNumber()

T = int(stdin.readline())
for _ in range(T):
    A, B = map(int,stdin.readline().split())
    result = solution(A, B)
    print(result)