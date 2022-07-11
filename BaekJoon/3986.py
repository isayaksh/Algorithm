# 3986 좋은 단어 < 실버 4 >
from sys import stdin
def goodWord(word):
    S = [] # 스택
    for w in word:
        if not S: S.append(w) # 스택이 비어있다면, 스택에 원소 추가
        else: # 스택이 비어있지 않다면
            if w == S[-1]: S.pop() # 현재 원소와 스택의 마지막 원소가 같다면, 스택의 마지막 원소 제거
            else: S.append(w) # 현재 원소와 스택의 마지막 원소가 다르다면, 스택에 원소 추가
    if not S: return 1 # 스택이 비어있다면 1 반환
    else: return 0 # 스택이 비어있지 않다면 0 반환
N = int(stdin.readline())
cnt = 0
for _ in range(N):
    cnt += goodWord(stdin.readline().strip())
print(cnt)