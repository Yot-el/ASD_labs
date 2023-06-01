# Найти подмножество множества, сумма элементов которого равняется 0.

def findSubset(m):
    for i in range(len(m)):
        m_subset = [m[i]] # Подмножество
        s = m[i]          # Сумма элементов подмножества

        for j in range(i+1, len(m)):
            if abs(s + m[j]) < abs(s):
                s += m[j]
                m_subset.append(m[j])

                if s == 0:
                    return m_subset

def myFunc(e):
    return abs(e)


m = [3, 6, -4, 2, -2]
m = [4, 5, -9, 7, -3, -4, 5, -2]
#m = [2, 1, -3]
m = [-1, -2, 3]
m.sort(reverse = True, key = myFunc)
print(m)
print(f'subset is {findSubset(m)}')

