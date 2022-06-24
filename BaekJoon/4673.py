# 4673 셀프 넘버 < 실버 5 >
from sys import stdin
def d(N):
    result = N + sum([int(i) for i in str(N)]) # 생성자 공식
    if result < 10000: return result
    else: return 0
self_number = [True for _ in range(10000)]
# 생성자가 있는 숫자 제거
for i in range(1,10000):
    self_number[d(i)] = False 
# 셀프 넘버 출력
for i in range(1,10000):
    if self_number[i]: print(i)