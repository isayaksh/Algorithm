# 숨바꼭질6

from sys import stdin

def GCD(A,B):
  while B!=0:
    A,B=B,A%B
  return A

N,S = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))

if N==1:
  print(abs(S-A[0]))
elif N==2:
  print(GCD(abs(S-A[0]),abs(S-A[1])))
else:
  nums = []
  for a in A:
    nums.append(abs(S-a))
  result = GCD(nums[0],nums[1])
  for i in range(2,N):
    result = GCD(result,nums[i])
  print(result)
