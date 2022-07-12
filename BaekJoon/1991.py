# 1991 트리 순회 < 실버 1 >
from sys import stdin

def Preorder(word): # 전위 순회
    if word != '.':
        left, right = D[word]
        print(word,end='')
        Preorder(left)
        Preorder(right)

def Inorder(word): # 중위 순회
    if word != '.':
        left, right = D[word]
        Inorder(left)
        print(word,end='')
        Inorder(right)

def Postorder(word): # 후위 순회
    if word != '.':
        left, right = D[word]
        Postorder(left)
        Postorder(right)
        print(word,end='')

D = {}
N = int(stdin.readline())
for _ in range(N):
    Node = list(stdin.readline().strip().split())
    D[Node[0]] = Node[1:]
Preorder('A')
print()
Inorder('A')
print()
Postorder('A')