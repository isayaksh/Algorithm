# 9576 책 나눠주기
from sys import stdin
# Union & Find 
def find(x):
    if x != books[x]:
        books[x] = find(books[x])
    return books[x]
def union(x, y):
    x = find(x)
    y = find(y)
    books[max(x,y)] = min(x,y)

T = int(stdin.readline())
for _ in range(T):
    N, M = map(int,stdin.readline().split())
    requests = []
    for _ in range(M):
        requests.append(tuple(map(int,stdin.readline().split())))
    requests.sort(reverse=True) # 신청서 내림차순으로 정렬
    books = [i for i in range(N+1)] # Union & Find를 위한 배열
    cnt = 0 # 학생 수
    for a, b in requests:
        b = find(b)
        if a > b: continue
        union(b,b-1)
        cnt += 1
    print(cnt)