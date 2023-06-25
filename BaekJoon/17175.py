# BOJ 17175 피보나치는 지겨웡~
# https://www.acmicpc.net/problem/17175

from sys import stdin

def countFibonacci(n):
    countFibonacciList = [1, 1, 3] + [0] * (n-2)
    for i in range(3, n+1):
        countFibonacciList[i] = (countFibonacciList[i-1] + countFibonacciList[i-2] + 1) % 1000000007
    return countFibonacciList

n = int(stdin.readline())
countFibonacciList = countFibonacci(n)
print(countFibonacciList[n])