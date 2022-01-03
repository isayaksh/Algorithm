import sys
import collections

def Resolution(answer,n):
    count=0
    stack=[]
    result=[]
    for a in answer:
        while count < a:
            count+=1
            stack.append(count)
            result.append('+')
        if stack[-1]==a:
            stack.pop()
            result.append('-')
        else:
            return False
    return result
        
n = int(sys.stdin.readline())

answer = collections.deque([])

for i in range(n):
    a = int(sys.stdin.readline())
    answer.append(a)

R = Resolution(answer,n)

if not R:
    print('NO')
else:
    for i in R:
        print(i)




