# 17521 Byte Coin < 실버 5 >
from sys import stdin
n, W = map(int,stdin.readline().split())
price = []
coin = 0
for _ in range(n):
  price.append(int(stdin.readline()))
price.append(0)
for i in range(n):
  W += coin*price[i]
  coin = 0
  if price[i] < price[i+1]:
    coin = W // price[i]
    W %= price[i]
print(W)