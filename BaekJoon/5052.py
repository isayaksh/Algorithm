# 5052 전화번호 목록 < 골드 5 >
from sys import stdin
# 한 번호가 다른 번호의 접두어인지 확인하는 함수
def check():
    for i in range(n-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            return 'NO'
    return 'YES'
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    numbers = sorted([stdin.readline().rstrip() for _ in range(n)]) # 번호 문자열을 사전순으로 정렬
    print(check())