# 1065 한수 <실버 4>
from sys import stdin

result = [0] + [i for i in range(1,100)]
for i in range(100,1001):
  tmp = list(map(int,str(i)))
  if(tmp[0]-tmp[1] == tmp[1]-tmp[2]): # 현재의 값이 등차수열인지 확인
    result.append(result[-1]+1)
  else:
    result.append(result[-1])
N = int(stdin.readline())
print(result[N])