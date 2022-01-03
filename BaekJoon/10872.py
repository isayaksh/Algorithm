# 팩토리얼

# 함수를 이용한 재귀
def Factorial(n):
  result=1
  if n > 1:
    result = n * Factorial(n-1)
  return result


from sys import stdin

N = int(stdin.readline())
print(Factorial(N))