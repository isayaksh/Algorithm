# 2436 공약수 < 골드 5 >
from math import sqrt
from sys import stdin
# 숫자 a, b가 서로소인지 확인하는 함수
def eo(a, b):
    MIN, MAX = min(a, b), max(a,b)
    for i in range(2,MIN+1):
        if MIN%i == 0 and MAX%i == 0:
            return True
    return False
# 최대 공약수와 최소 공배수의 값을 이용해 합이 최소가 되는 두 자연수를 반환하는 함수
def check(gcm, lcm):
    result = [gcm , lcm]
    tmpSum = 100000000
    N = lcm//gcm
    for num in range(1, int(sqrt(lcm//gcm))+1):
        tmp = N // num
        if N % num != 0 or eo(num, tmp): continue   
        ts = tmp * gcm + num * gcm
        if  ts < tmpSum:
            tmpSum = ts
            result = [num * gcm, tmp * gcm]
    return result

gcm, lcm = map(int,stdin.readline().split())
num1, num2 = check(gcm, lcm)
print(num1, num2)