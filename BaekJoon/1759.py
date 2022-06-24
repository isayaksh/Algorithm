# 1759 암호 만들기 < 골드 5 >   
from itertools import combinations
from sys import stdin

# string 문자열에 존재하는 모음의 개수 반환
def check_vowel(string):
    cnt = 0
    for str in 'aeiou':
        cnt += string.count(str)
    return cnt

L, C = map(int,stdin.readline().split())
string = sorted(list(stdin.readline().split())) # 사전순으로 정렬
for s in combinations(string,L): # 생성할 수 있는 모든 조합
    String = ''.join(s)
    cnt = check_vowel(String)
    if cnt > 0 and L - cnt > 1: print(String)