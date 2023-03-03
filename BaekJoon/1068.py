# BOJ 1068 트리
# https://www.acmicpc.net/problem/1068

from sys import stdin
from collections import defaultdict

def solution(N, nodes, deleteNode):

    answer = 0

    # 트리 생성
    tree = defaultdict(list)
    for s, e in enumerate(nodes):
        if s == deleteNode:
            continue
        tree[e].append(s)
    
    # 최상위 부모 없는 경우
    if not tree[-1]:
        return 0

    stack = [-1]
    while stack:
        node = stack.pop()
        # 리프 노드
        if not tree[node]:
            answer += 1
            continue
        # 자식 노드 이동
        for nextNode in tree[node]:
            stack.append(nextNode)
    return answer

N = int(stdin.readline())
nodes = list(map(int,stdin.readline().split()))
deleteNode = int(stdin.readline())

res = solution(N, nodes, deleteNode)
print(res)