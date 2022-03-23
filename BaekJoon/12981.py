# 12981 공 포장하기 <실버 5>
from sys import stdin
R, G, B = map(int,stdin.readline().split())
# 공의 색이 모두 다른 경우
MIN = min(R,G,B)
result = MIN
R -= MIN
G -= MIN
B -= MIN
# 같은 공이 2개 남아 있는 경우
result += R//3 + G//3 + B//3
R %= 3
G %= 3
B %= 3
# 같은 공이 2개 남아 있는 경우
if R == 2:
  result += 1
  R = 0
if G == 2:
  result += 1
  G = 0
if B == 2:
  result += 1
  B = 0
# 공이 1개 혹은 두 종류의 공이 1개씩 있는 경우
if R+G+B > 0:
  result += 1
print(result)