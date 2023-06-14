# BOJ 16508 전공책
# https://www.acmicpc.net/problem/16508

from sys import stdin, maxsize
from collections import Counter
from itertools import combinations

def solution(T, N, books):

    answer = maxsize

    def haveWords():
        for word, c in T.items():
            if not wordCounter[word] or wordCounter[word] < c:
                return False
        return True

    T = Counter(T)
    books.sort(key = lambda x : int(x[0]))

    for r in range(1, N+1):
        for cases in combinations(books, r):
            wordCounter = Counter()
            totalC = 0
            for C, W in cases:
                totalC += int(C)
                wordCounter += Counter(W)
            if haveWords():
                answer = min(answer, totalC)
    return answer if answer != maxsize else -1

T = stdin.readline().strip()
N = int(stdin.readline())
books = list(list(stdin.readline().split()) for _ in range(N))

res = solution(T, N, books)
print(res)
