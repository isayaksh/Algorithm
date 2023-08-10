# BOJ 21275 폰 호석만
# https://www.acmicpc.net/problem/21275

from sys import stdin

def solution(A, B):

    def calculation(n, formula):
        return sum([formula[i] * n**(len(formula)-i-1) for i in range(len(formula))])

    answer = []
    
    dictionary = dict()
    # 0 ~ 9
    for i in range(10): dictionary[str(i)] = i
    # a ~ z
    for i in range(97, 123): dictionary[chr(i)] = i - 87

    formulaA = [dictionary[a] for a in A]
    formulaB = [dictionary[b] for b in B]
    
    for a in range(max(formulaA)+1, 37):
        for b in range(max(formulaB)+1, 37):
            calcA, calcB = calculation(a, formulaA), calculation(b, formulaB)
            if calcA == calcB and a != b:
                answer.append([calcA, a, b])
    return answer

A, B = stdin.readline().split()

res = solution(A, B)
N = len(res)
if N == 0:
    print("Impossible")
if N == 1:
    print(' '.join(map(str, res[0])))
if N > 1:
    print("Multiple")