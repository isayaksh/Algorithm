# 1049 기타줄 <실버 4>
from sys import stdin
N, M = map(int,stdin.readline().split())
string = 1000
strings = 1000
for _ in range(M):
  Strs, Str = map(int,stdin.readline().split())
  if strings > Strs:
    strings = Strs
  if string > Str:
    string = Str
print(min((N//6+1)*strings,(N//6)*strings+(N%6)*string,N*string))