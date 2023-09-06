# BOJ 9242 폭탄 해체
# https://www.acmicpc.net/problem/9242

from sys import stdin

def solution(code):

    def mapping(decode):
        for key, value in decodeList.items():
            if decode == key:
                return value
        return False

    decodeList = {
        '001020012102220323041424': '0',
        '2021222324': '1', 
        '0010202102122203041424': '2', 
        '0010202102122223041424': '3', 
        '002001210212222324': '4', 
        '0010200102122223041424': '5', 
        '001020010212220323041424': '6', 
        '00102021222324': '7', 
        '00102001210212220323041424': '8', 
        '001020012102122223041424': '9'
    }

    codeList = ''
    for i in range(0, len(code[0]), 4):
        # decode
        decode = ''
        for y in range(5):
            for x in range(i, i+3):
                try:
                    if code[y][x] == '*':
                        decode += str(x-i)+str(y)
                except:
                    return 'BOOM!!  '
        
        mappingCode = mapping(decode)
        if not mappingCode:
            return 'BOOM!!'
        codeList += mappingCode
    return 'BEER!!' if not int(codeList)%6 else 'BOOM!!'

code = list(stdin.readline()[:-1] for _ in range(5))

res = solution(code)
print(res)