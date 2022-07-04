# 10819 차이를 최대로
from itertools import permutations
from sys import stdin
def sub(number):
    answer = 0
    for i in range(N-1):
        answer += abs(number[i] - number[i+1])
    return answer
M = 0
N = int(stdin.readline()) # 정수의 개수
numbers = map(int,stdin.readline().split()) # N개의 정수로 이루어진 배열
for number in permutations(numbers,N): # 순열을 통한 모든 조합
    M = max(M,sub(number))
print(M)