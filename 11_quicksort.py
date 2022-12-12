def quickSort(_arr, i, j):
    if i < j:
        s = partition(_arr, i, j)
        quickSort(_arr, i, s-1)
        quickSort(_arr, s + 1, j)

def partition(_arr, l, r):
    pivot = _arr[r] #опорный элемент
    i = l - 1
    for j in range(l, r):
        if _arr[j] <= pivot:
            i = i + 1
            (_arr[i], _arr[j]) = (_arr[j], _arr[i])
    (_arr[i + 1], _arr[r]) = (_arr[r], _arr[i + 1])
    return i + 1

_arr = list(map(int, input().split()))
quickSort(_arr, 0, len(_arr)-1)
print(_arr)