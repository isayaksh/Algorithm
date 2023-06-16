# BOJ 9421 소수상근수
# https://www.acmicpc.net/problem/9421

from sys import stdin
from math import sqrt

def getPrimeNumber(number):
    primeNumbers = [True] * (number+1)
    for num in range(2, int(sqrt(number)) + 1):
        if primeNumbers[num]:
            for i in range(num*2, number+1, num):
                primeNumbers[i] = False
    return [i for i in range(2, number+1) if primeNumbers[i]]

def checkSGNumber(number):
    used = set()
    while True:
        if number == 1:
            return True
        newNumber = 0
        for num in map(int,list(str(number))):
            newNumber += num**2
        if newNumber in used:
            break
        used.add(newNumber)
        number = newNumber
    return False

def solution(n):
    # 소수 구하기
    primeNumbers = getPrimeNumber(n)
    # 상근수 구하기
    for primeNumber in primeNumbers:
        if checkSGNumber(primeNumber):
            print(primeNumber)

n = int(stdin.readline())
solution(n)