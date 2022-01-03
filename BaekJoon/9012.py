import sys

T = int(sys.stdin.readline())

def VPS(PS):
    stack=[]
    for ps in PS:
        if ps == '(':
            stack.append(ps)
        elif ps == ')' and stack:
            if stack.pop() != '(':
                return 'NO'
        elif ps == ')' and not stack:
            return 'NO'
    if stack:
        return 'NO'
    else:
        return 'YES'

for i in range(T):
    PS = sys.stdin.readline()
    print(VPS(PS))