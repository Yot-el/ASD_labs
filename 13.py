#Хеш-таблица с наложением
class HashTable():
    def __init__(self, size=10):
        self.A = 0.618033 # модификатор для хеш-фунции
        self.N = 13
        self.capacity = self.getPrime(size) #размер хеш-таблицы
        self.table = {key:None for key in range(self.capacity)}
        self.keys = [] #список ключей

    def checkPrime(self, n):
        if (n == 1 or n == 0):
            return 0
        for i in range(2, n//2):
            if n % i == 0:
                return 0
        return 1
    
    def getPrime(self, n):
        if n % 2 == 0:
            n += 1
        while not self.checkPrime(n):
            n += 1
        return n
    
    def hashFunctionMod(self, key):
        return key % self.capacity
    
    def hashFunctionComb(self, key):
        return self.N * ((key * self.A) % 1)
    
    def hashFunctionPowered(self, key):
        return (self.hashFunctionMod(key) + self.hashFunctionComb(key)) // 1
    
    '''Алгоритм вставки проверяет ячейки массива  с помощью линейного пробирования
    до тех пор, пока не найдется свободная ячейка'''
    def insertItem(self, key, data):
        index = self.hashFunctionPowered(key)
        if (not self.table[index]):
            self.keys.append(index)
        else:
            i = 0
            while True:
                if (not self.table[index + i]):
                    index += i
                    self.keys.append(index)
                    break
                i += 1
        self.table[index] = data
    
    def displayHash(self):
        for key in self.keys:
            print(f'{key}: {self.table[key]}')

    '''Алгоритм поиска аналогичен алгоритму вставки
    Вычисляется индекс стартовой ячейки. Ячейки просматриваются до тех пор,
    пока не найден искомый ключ или пустая ячейка'''
    def searchItem(self, data):
        key_val = 0
        for i in data:
            key_val += ord(i)
        
        index = self.hashFunctionPowered(key_val)
        counter, i = 0, 0
        while True:
            if (not (self.table[index + i])):
                break
            if (self.table[index + i] == data):
                counter += 1
            i += 1
        return counter

tab = HashTable(12345)
s = input().split()

key_val = 0
for word in s:

    for symbol in word:
        key_val += ord(symbol)
    
    tab.insertItem(key_val, word)
    key_val = 0

print(tab.searchItem('hello'))
tab.displayHash()



    

