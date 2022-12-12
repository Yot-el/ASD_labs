import re
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
        else:
            tr = Node(_tree[-4], CheckifNode(_tree[-2]), CheckifNode(_tree[-1]))
            del _tree[len(_tree)-4:len(_tree)]
            _tree.append(tr)

    return _tree[0]

def pre_order(node):
    if node:
        print(node.data, end=' ')
        pre_order(node.left)
        pre_order(node.right)

def in_order(node):
    if node:
        in_order(node.left)
        print(node.data, end=' ')
        in_order(node.right)

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

def minValueNode(node):
    current = node
    if(current):
        while(current.left):
            current = current.left
    return current

def delNode(key, node):
    if (not node):
        return node
    if (key < node.data):
        node.left = delNode(key, node.left)
    elif (key > node.data):
        node.right = delNode(key, node.right)
    else:
        # Если у узла нет дочерних узлов - заменяем на None
        # Если есть 1 дочерний узел - заменяем на него   
        if (not node.left):
            temp = node.right
            return temp
        elif (not node.right):
            temp = node.left
            return temp

        # Если есть 2 дочерних узла - ищем минимальный элемент в правой ветке, перестраивая ее
        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = delNode(temp.data, node.right)

    return node

print('\n17 лаба')
insertNode(int(input('Узел для добавления: ')), tree)
pre_order(tree)

tree = delNode(int(input('\nУзел для удаления: ')), tree)
pre_order(tree)
