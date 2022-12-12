import re
def turnIntoPostfix(s):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    operator_stack = []
    postfix = []
    count_operators = 0 #кол-во бинарных операторов
    count_operands = 0 

    for x in s:
        if x == '(':
            operator_stack.append(x)
        elif x.isdigit():
            postfix.append(int(x))
            count_operands += 1
        elif x == ')':
            if operator_stack.count('(') == 0:
                return None
            topX = operator_stack.pop()
            if(topX == '-' and count_operators == count_operands):
                postfix[-1] = -1 * postfix[-1]
                count_operators -= 1
                topX = operator_stack.pop()
            while topX != '(':
                postfix.append(topX)
                topX = operator_stack.pop()
        else:
            while (len(operator_stack) != 0 and prec[operator_stack[-1]] >= prec[x]):
                postfix.append(operator_stack.pop())
            operator_stack.append(x)
            count_operators += 1

    if operator_stack.count('(') > 0 or count_operators >= count_operands:
        return None
    
    while(len(operator_stack) != 0):
        postfix.append(operator_stack.pop())

    return postfix

def doMath(operator, x, y):
    if operator == '+':
        return x+y
    elif operator == '-':
        return y-x
    elif operator == '*':
        return x*y
    else:
        if x == 0:
            return None
        return y/x

def delN(s):
    while(s.count('') != 0):
        s.remove('')
    return s

def calcPostfix(s):
    operands_stack = []

    for x in s:
        if isinstance(x, int) or isinstance(x, float):
            operands_stack.append(x)
        else:
            t = round(doMath(x, operands_stack.pop(), operands_stack.pop()), 2)
            if t:
                operands_stack.append(t)
            else:
                return 'Ошибка'
    
    return operands_stack[-1]

infix = str(input())
print(infix)
s = delN(re.split('([+|\-|*|/|)|(|=])', infix))[:-1]
k = turnIntoPostfix(s)
if k:
    print(calcPostfix(k))
else:
    print('Ошибка')

