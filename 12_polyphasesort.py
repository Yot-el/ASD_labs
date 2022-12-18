import os

def CreateRuns(A, B, source_file, S):
    '''Объявляем массив, длина S которого равна длине отрезков; 
    На первом шаге читаются S записей и сортируются с помощью внутренней сортировки. 
    Потом поочередно получающиеся массивы записываются то в файл A, то в файл B.'''
    CurrentFile = A
    f = open(source_file, "r")
    _arr = []
    value = ''
    while True:
        data = f.read(1)
        if not data:
            if value:
                _arr.append(int(value))
            _arr.sort()
            _arr = list(map(str, _arr))
            with open(CurrentFile, "a+") as file:
                file.write(" ".join(_arr))
            break
        else:
            if (data != ' '):
                value += data
            else:
                if (S != len(_arr)):
                    _arr.append(int(value))
                    value = ''
                elif (S == len(_arr)):
                    print(_arr)
                    _arr.sort()
                    _arr = list(map(str, _arr))
                    with open(CurrentFile, "a+") as file:
                        file.write(" ".join(_arr))
                    if CurrentFile == A:
                        CurrentFile = B
                    else:
                        CurrentFile = A
                    _arr = []
                    _arr.append(int(value))
                    value = ''
    f.close()

def PolyPhaseMerge(A, B, C, D, S):
    '''На этом этапе отрезки из файла Input1 сливаются с отрезками из файла Input2, в результате отрезки
    длиной 2S, 4S и т.д. записываются в CurrentOutput файл.'''
    Size = S
    Input_1 = A
    Input_2 = B
    CurrentOutput = C

    with open(CurrentOutput, 'wb'): #Очистка CurrentOutput файла
        pass

    while((os.stat(Input_1)).st_size != 0 and (os.stat(Input_2)).st_size != 0): #Проверка на пустоту файлов с отрезками               
        f_1 = open(Input_1, "r")                                                #Если один из них пустой - в 
                                                                                #другом находится отсортированный список
        f_2 = open(Input_2, "r")
        data_1 = f_1.read(Size)
        data_2 = f_2.read(Size)
        Read_Flag = 1

        while(data_1 or data_2):
            if Read_Flag == 0:
                data_1 = f_1.read(Size)
                data_2 = f_2.read(Size)

            data_1 = data_1.split()
            data_1 = list(map(int, data_1))
            data_2 = data_2.split()
            data_2 = list(map(int, data_2))

            data = Merge(data_1, data_2)
            data = list(map(str, data))
            Read_Flag = 0

            with open(CurrentOutput, "a+") as file:
                file.write(" ".join(data) + " ")
            if (CurrentOutput == A):
                CurrentOutput = B
            elif (CurrentOutput == B):
                CurrentOutput = A
            elif (CurrentOutput == C):
                CurrentOutput = D
            else:
                CurrentOutput = C
        
        f_1.close()
        f_2.close()
        with open(Input_1, 'wb'): 
            pass
        with open(Input_2, 'wb'):
            pass
        
        Size *= 2
        if (Input_1 == A):
            Input_1 = C
            Input_2 = D
            CurrentOutput = A
        else:
            Input_1 = A
            Input_2 = B
            CurrentOutput = C

def Merge(A, B):
    A = A + B
    A.sort()
    return A

C = 'C.txt'
A = 'A.txt'
B = 'B.txt'
D = 'D.txt'
S = 20 #длина отрезка S
CreateRuns(A, B, C, S)
PolyPhaseMerge(A, B, C, D, S)
