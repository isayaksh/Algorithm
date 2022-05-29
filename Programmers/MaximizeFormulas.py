import re
from collections import deque
def solution(expression):
    answer = 0
    operatorOrder = [["+","-","*"],["+","*","-"],["*","-","+"],["*","+","-"],["-","+","*"],["-","*","+"]]
    expression = re.findall("[0-9]+|[+*-]",expression)
    for operators in operatorOrder:
        tmp1 = deque(expression)
        for operator in operators:
            tmp2 = deque()
            while tmp1:
                word = tmp1.popleft()
                if word == operator:
                    if word == '+': result = int(tmp2.pop()) + int(tmp1.popleft())
                    if word == '-': result = int(tmp2.pop()) - int(tmp1.popleft())
                    if word == '*': result = int(tmp2.pop()) * int(tmp1.popleft())
                    tmp2.append(result)
                else:
                    tmp2.append(word)
            tmp1 = tmp2
        if answer < abs(tmp1[0]): answer = abs(tmp1[0])
    return answer