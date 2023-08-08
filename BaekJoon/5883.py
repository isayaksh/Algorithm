# BOJ 5883 아이폰 9S
# https://www.acmicpc.net/problem/5883

from sys import stdin

def solution(N, battery):
    def longestLength(newLine):
        lengthList = []
        for i in range(1, len(newLine)):
            if newLine[i-1] != newLine[i]:
                lengthList.append(1) 
            else:
                lengthList[-1] += 1
        return max(lengthList)

    answer = 0

    battery_set = set(battery)
    for ex in battery_set:
        newLine = [-100] + [b for b in battery if b != ex]
        length = longestLength(newLine)
        answer = max(answer, length)
        
    return answer
        
N = int(stdin.readline())
battery = list(int(stdin.readline()) for _ in range(N))

res = solution(N, battery)
print(res)