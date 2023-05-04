# алгоритм Рабина

def hash(string): # Сумма ASCII
    summ = 0
    for i in range(len(string)):
        summ += ord(string[i])
    
    return summ

def hashUpdate(prev_hash, start, end):
    new_hash = prev_hash - ord(start) + ord(end)
    return new_hash

def rabinFunc(pattern, text):
    M = len(pattern)
    res = []

    hash_pattern = hash(pattern)
    hash_text = hash(text[0:len(pattern)])

    for i in range(0, len(text)-M + 1):

        if hash_pattern == hash_text:
            k = 0
            for j in range(M):
                if pattern[j] != text[i + j]: # Символы на одинаковых позициях не совпали
                    k = 1
                    break
            if not k:
                res.append(f'{text[i:i+j+1]}, {i}, {i+j}') # Добавляем совпадение в массив
        
        if i + M < len(text): # У Тенебекова в коде этого не было, но если пробегать i от 0 до len(text)-M без доб-я 1, то последние
            # M символов у меня не обрабатываются, т.е. в text последний us будет проигнорирован (если pattern = 'us' например)
            # Если пробегать i от 0 до len(text)-M+1, то приходится добавлять эту проверку, я не знаю как по-другому
            hash_text = hashUpdate(hash_text, text[i], text[i + M])

    if res:
        return res
    
    return -1 # Нет совпадений


print(rabinFunc('indeed', 'a friend in need is indeed'))
print(rabinFunc('ips', 'Lorem ipsum dolor sit amet, Lorem ipsum dolor sit amet'))
print(rabinFunc('spi', 'Lorem ipsum dolor sit amet, Lorem ipsum dolor sit amet'))
print(rabinFunc('jj', 'a friend in need is indeed'))