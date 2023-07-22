# BOJ 21314 민겸 수
# https://www.acmicpc.net/problem/21314

from sys import stdin
from re import findall

def solution(mkNumber):

    def converToMaxValue(mkNumber):
        value = ''
        for mkn in findall('M*K|M', mkNumber):
            N = len(mkn) - 1
            if N == 0:
                value += str(5) if mkn == 'K' else str(1)
            else:
                value += str(5*10**N)
        return value
    
    def convertToMinValue(mkNumber):
        value = ''
        for mkn in findall('K|M+', mkNumber):
            N = len(mkn) - 1
            value += str(5) if mkn == 'K' else str(10**N)
        return value
    
    return converToMaxValue(mkNumber), convertToMinValue(mkNumber)

mkNumber = stdin.readline().strip()

maxValue, minValue = solution(mkNumber)
print(maxValue)
print(minValue)