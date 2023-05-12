# BOJ 2661 좋은수열
# https://www.acmicpc.net/problem/2661

from sys import stdin

def dfs(sequence):
    if N == len(sequence):
        print(sequence)
        exit()
    for i in range(1, 4):
        if checkSymmetry(sequence+str(i)):
            dfs(sequence+str(i))
    
def checkSymmetry(sequence):
    for i in range(1, len(sequence)//2+1):
        if sequence[-2*i:-i] == sequence[-i:]:
            return False
    return True

N = int(stdin.readline())
dfs('1')