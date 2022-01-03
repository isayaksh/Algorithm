from sys import stdin
sum = 0
N = int(stdin.readline())
N = 1000 - N
if N//500 :
  sum += N//500
  N -= (N//500)*500
if N//100:
  sum += N//100
  N -= (N//100)*100
if N//50:
  sum += N//50
  N -= (N//50)*50
if N//10:
  sum += N//10
  N -= (N//10)*10
if N//5:
  sum += N//5
  N -= (N//5)*5
sum += N
print(sum)
