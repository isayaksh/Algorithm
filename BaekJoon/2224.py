# BOJ 2224 명제 증명
# https://www.acmicpc.net/problem/2224

from sys import stdin
from collections import defaultdict

def solution(N, initPropositions):
    
    answer = set()
    newPropositions = defaultdict(set)

    for antecedent, arrow, consequent in initPropositions:
        newPropositions[antecedent].add(consequent)
    
    def dfs(antecedent, consequent):
        if consequent not in newPropositions: return
        for con in newPropositions[consequent]:
            if (antecedent, con) not in answer and antecedent != con:
                answer.add((antecedent, con))
                dfs(antecedent, con)
    
    for antecedent in newPropositions:
        dfs(antecedent, antecedent)

    print(len(answer))
    for pro, con in sorted(answer):
        print(f'{pro} => {con}')

N = int(stdin.readline())
initPropositions = list(stdin.readline().split() for _ in range(N))

solution(N, initPropositions)