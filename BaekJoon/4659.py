# BOJ 4659 비밀번호 발음하기
# https://www.acmicpc.net/problem/4659

from sys import stdin

def solution(password):

    vowel = {'a', 'e', 'i', 'o', 'u'}
    
    condition1 = True if password[-1] in vowel or password[-2] in vowel else False

    for i in range(len(password)-2):
        # 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
        if password[i] in vowel:
            condition1 = True
        
        # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
        if (password[i] in vowel) == (password[i+1] in vowel) == (password[i+2] in vowel):
            return False
        
        # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        if password[i] == password[i+1] == password[i+2]:
            return False
        if password[i] == password[i+1]:
            word = password[i] + password[i+1]
            if word != 'ee' and word != 'oo':
                return False
        if password[i+1] == password[i+2]:
            word = password[i+1] + password[i+2]
            if word != 'ee' and word != 'oo':
                return False

    return condition1

while True:
    password = stdin.readline().strip()
    if password == 'end':
        break
    res = solution(password)
    print(f'<{password}>' + (' is ' if res else ' is not ') + 'acceptable.')