# алгоритм Бойера-Мура (Бойера-Мура-Хорспула)

def alphabet_init(pattern): # Формирование таблицы сдвигов 
    alph = list(set(pattern))
    res = {}

    for letter in alph:
        for i in range(len(pattern) - 1): # Последний символ паттерна не рассматривается т.к. это чревато зацикливанием
            if letter == pattern[i]:
                res[letter] = len(pattern) - 1 - i
    
    return res

def BMHfunc(pattern, text):
    shift_table = alphabet_init(pattern)
    res = []
    M = len(pattern)
    i = 0

    while i <= len(text) - M:
        k = 0

        for j in range(M - 1, -1, -1): # Сравниваем справа налево, хотя в БМХ (в отличие от БМ) это не принципиально
            if pattern[j] != text[i + j]:
                k = 1
                break

        if not k:
            res.append(f'{text[i:i+M]}, {i}, {i+M-1}')
        
        last_symbol = text[i + M - 1] # Последний символ "над" паттерном
        if last_symbol in shift_table:
            i += shift_table[last_symbol] 
        else:
            i += M

    return res

print(BMHfunc('indeed', 'a friend in need is indeed'))
print(BMHfunc('ips', 'Lorem ipsum dolor sit amet, Lorem ipsum dolor sit amet'))