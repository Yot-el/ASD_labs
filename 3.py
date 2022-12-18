x = int(input())
'''
3^a + 5^b + 7^c = i, i = [1, x]
a <= log3(x)
b <= log5(x)
c <= log7(x)
В алгоритме поиска сначала ищутся все степени 7, значения которых не больше x, и заносятся в массив
Потом находятся числа, имеющие в себе как множитель 5, так и 7, потом то же самое со множителем 3.
'''
_arr = []
ta, tb, tc = 1, 1, 1

while (ta <= x):
    tb = ta
    while (tb <= x):
        tc = tb
        while (tc <= x):
            _arr.append(tc)
            tc *= 7
        tb *= 5
    ta *= 3

_arr.sort()
for x in _arr:
    print(x)



