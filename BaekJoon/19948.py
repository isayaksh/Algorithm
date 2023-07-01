# BOJ 19948 음유시인 영재
# https://www.acmicpc.net/problem/19948

from sys import stdin


def solution(line, space, count):
    # 사용 가능한 키보드 횟수 초기화
    counter = {chr(i+65) : count[i] for i in range(26)}
    counter[' '] = space
    
    beforeWord = '' # 이전에 사용한 알파벳

    for word in line:
        upperWord = word.upper()
        # 같은 문자가 연속으로 나오거나 빈칸이 연속으로 나오는 경우
        if word == beforeWord: continue
        # 키보드의 수명이 다 한 경우
        if counter[upperWord] == 0: return -1

        counter[upperWord] -= 1
        beforeWord = word

    # 첫 글자를 대문자로 바꾼 뒤 순서대로 이어서 만든 제목
    title = ''.join([word[0].upper() for word in line.split()])

    for word in title:
        # 키보드의 수명이 다 한 경우
        if counter[word] == 0: return -1
        counter[word] -= 1
    
    return title


line = stdin.readline().strip()
space = int(stdin.readline())
count = list(map(int,stdin.readline().split()))

res = solution(line, space, count)
print(res)