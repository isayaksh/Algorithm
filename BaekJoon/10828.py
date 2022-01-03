import sys
# 정수를 저장할 stack
stack=[]

# 명령의 수
N = int(sys.stdin.readline())

for i in range(N):
    order = list(map(str,sys.stdin.readline().split()))
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if stack: # 스택이 비어있다면 False 스택에 원소가 있다면 True
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

