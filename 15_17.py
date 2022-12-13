import re
#Класс узла дерева
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def delN(s):
    while(s.count('') != 0):
        s.remove('')
    return s

def findEmptyChild(s):
    i = s.count(',)')
    while(i != 0):
        j = s.find(',)')
        s = s[:j] + ' ' + s[j+1:]
        i -= 1
    
    i = s.count('(,')
    while (i != 0):
        j = s.find('(,')
        s = s[:j+1] + ' ' + s[j+1:]
        i -= 1
    return s

def CheckifNode(i):
    if (isinstance(i, Node)):
        return i
    else:
        if i == ' ':
            return None
        else:
            return Node(i)
'''
Дерево подается в скобочно-линейной записи (Напр. 8(2,10(,12)) )
Перед тем, как строится само дерево, оно преобразуется в список (Напр. [8, '(', 2, 10, '(', ' ', 12, ')', ')'])
Когда в списке встречается конструкция [X, '(', A, B, ')'], то эта конструкция сворачивается
в узел X с правым дочерним узлом B и левым дочерним узлом A. 
В результате в стэке останется корень дерева.
'''
def buildTree(s):
    _tree = []

    for x in s:
        if x.isdigit():
            _tree.append(int(x))
        elif x == ' ':
            _tree.append(x)
        elif x == '(':
            _tree.append(x)
        elif x == ',':
            continue
        else: # x == ')'
            tr = Node(_tree[-4], CheckifNode(_tree[-2]), CheckifNode(_tree[-1]))
            del _tree[len(_tree)-4:len(_tree)]
            _tree.append(tr)

    return _tree[0]
#Прямой обход дерева: посещение родительских узлов до дочерних
def pre_order(node):
    if node:
        print(node.data, end=' ')
        pre_order(node.left)
        pre_order(node.right)
#Центральный обход: сначала обход по левому дочернему узлу, потом вывод родительского, потом обход по правому дочернему узлу
def in_order(node):
    if node:
        in_order(node.left)
        print(node.data, end=' ')
        in_order(node.right)
#Концевой обход: сначала обход дочерних узлов, потом родительского
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end=' ')


s = findEmptyChild(str(input()))
s = delN(re.split('([)|(|,| ])', s))

tree = buildTree(s)

print('Прямой обход, 15 лаба')
pre_order(tree)

print('\nЦентрированный обход, 15 лаба')
in_order(tree)

print('\nКонцевой обход, 15 лаба')
post_order(tree)

#16 лаба
def n_pre_order(node):
    _stack = []
    _stack.append(node)
    while(_stack):
        node = _stack.pop()
        print(node.data, end=' ')
        if(node.right):
            _stack.append(node.right)
        if(node.left):
            _stack.append(node.left)

print('\nПрямой без рекурсии, 16 лаба')
n_pre_order(tree)

#17 лаба
'''Функция для добавления вершины БДП
Свойства:
Все узлы в левой ветке меньше рассматриваемого узла,
Все узлы в правой ветке больше рассматриваемого узла.
По этим свойствам проводится операция вставки нового узла:
Если новый узел Y больше рассматриваемого узла X, рассматриваем наличие у X правого дочернего узла,
если его нет - вставляем Y, если есть - производим функцию вставки Y в правое поддерево.
Аналогично с новыми узлами, меньшими X.
'''
def insertNode(key, node):
    if(key < node.data):
        if(node.left):
            insertNode(key, node.left)
        else:
            node.left = Node(key)
    elif(key > node.data):
        if(node.right):
            insertNode(key, node.right)
        else:
            node.right = Node(key)
    else:
        print('Такой узел уже существует')
        
#Функция поиска наименьшего узла для операции удаления
def minValueNode(node):
    current = node
    if(current):
        while(current.left):
            current = current.left
    return current
'''Функция удаления вершины БДП'''
def delNode(key, node):
    if (not node):
        return node
    if (key < node.data):                       #
        node.left = delNode(key, node.left)     # Ищем нужный узел
    elif (key > node.data):                     #
        node.right = delNode(key, node.right)   #
    else:
        # Если у узла нет дочерних узлов - заменяем на None
        # Если есть 1 дочерний узел - заменяем на него   
        if (not node.left):
            temp = node.right
            return temp
        elif (not node.right):
            temp = node.left
            return temp

        # Если есть 2 дочерних узла - ищем минимальный элемент в правой ветке удаляемого родительского узла
        # Этот элемент становится на место удаляемого узла
        # Ветка, в которой был этот узел ранее, перестраивается
        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = delNode(temp.data, node.right)

    return node

'''Операция поиска вершины БДП'''
def searchNode(key, node):
    if not node:
        return False
    if key > node.data:
        return (searchNode(key, node.right))
    elif key < node.data:
        return (searchNode(key, node.left))
    else:
        return True
    
print('\n17 лаба')
insertNode(int(input('Узел для добавления: ')), tree)
pre_order(tree)

tree = delNode(int(input('\nУзел для удаления: ')), tree)
pre_order(tree)

print(searchNode(int(input('\nУзел для поиска: ')), tree))
