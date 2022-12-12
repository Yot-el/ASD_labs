x = int(input())

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



