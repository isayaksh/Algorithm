# BOJ 11365 !밀비 급일
# https://www.acmicpc.net/problem/11365

from sys import stdin

while True:
    encdedString = stdin.readline().strip()
    if encdedString == "END": break
    print(''.join(list(encdedString)[::-1]))
