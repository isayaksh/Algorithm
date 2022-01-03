import sys

T = int(sys.stdin.readline())

for i in range(T):
    sentence = sys.stdin.readline().split()
    for s in sentence:
        print(s)
        print(s[::-1],end=' ') # 문자열을 뒤집어서 출력하는 방법