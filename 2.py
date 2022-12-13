import re
#Функция переводит строку в обратную польскую нотацию
def turnIntoPostfix(s):
    prec = {} #Приоритеты операторов
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    operator_stack = [] #стэк операторов
    postfix = [] #результирующий стэк
    count_operators = 0 #кол-во бинарных операторов
    count_operands = 0 #кол-во операндов

    for x in s:
        if x == '(':
            operator_stack.append(x)
        elif x.isdigit():
            postfix.append(int(x))
            count_operands += 1
        elif x == ')':
            if operator_stack.count('(') == 0: #Проверка на ошибку в строке по типу ")2+4=", "(5*3))="
                return None
            topX = operator_stack.pop()
            if(topX == '-' and count_operators == count_operands): #Проверка на унарный минус в строке
                '''
                Кол-во бинарных операторов не превышает количество операндов, поэтому, если их значение равно и в стэке
                операторов присутствует конструкция "(-", минус является унарным
                '''
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

    if operator_stack.count('(') > 0 or count_operators >= count_operands: #Проверка на ошибки по типу "((2+3)=", "2++3="
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
        if x == 0: #Проверка на деление на 0
            return None
        return y/x

def delN(s):
    while(s.count('') != 0):
        s.remove('')
    return s

#Функция для вычисления результата выражения
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
s = delN(re.split('([+|\-|*|/|)|(|=])', infix))[:-1]
k = turnIntoPostfix(s)
if k:
    print(calcPostfix(k))
else:
    print('Ошибка')

