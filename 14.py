#Хеш-таблица со списками
class HashTable:
    def __init__(self, size=10):
        self.capacity = self.getPrime(size) #размер хеш-таблицы
        self.table = [[] for i in range(self.capacity)]
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

    def hashFunction(self, key):
        return key % self.capacity

    '''Алгоритм вставки: вычисляется ключ с помощью хеш-функции, 
    значение вставляется в список, лежащий под полученным ключом'''
    def insertItem(self, key, data):
        i = self.hashFunction(key)
        if (i not in self.keys):
            self.keys.append(i)
        self.table[i].append(data)

    '''Алгоритм поиска: вычисляем ключ с помощью хеш-функции,
    ищем нужное значение в списке, лежащем под полученным ключом'''
    def searchItem(self, data):
        res = 0
        key_val = 0
        for i in data:
            key_val += ord(i)
        key = self.hashFunction(key_val)
        for j in self.table[key]:
            if j == data:
                res += 1
        return res
    
    def displayHash(self):
        for key in self.keys:
            print(f'{key}: ', end='')
            for obj in self.table[key]:
                print(obj, end=' ')
            print()


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
    

