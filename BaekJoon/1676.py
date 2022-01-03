# 팩토리얼 0의 개수

from sys import stdin

def Factorial(N):
  result = 1
  if N > 1:
    result = N * Factorial(N-1)
  return result

N = int(stdin.readline())
F = Factorial(N)

count = 0

while F%10==0:
  count+=1
  F = F//10
print(count)

# refactoring
# N = int(stdin.readline())
# print(N//5+N//25+N//125)