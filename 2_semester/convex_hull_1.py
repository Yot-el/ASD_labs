input_file = open("test_1_lab_1.txt", "r")
dots = []

while True:
    line = input_file.readline()
    if not line:
        break
    dot = list(map(int, line.split()))
    dots.append(dot)

# Сортируем координаты по x и y
def x_compare(dot):
    return dot[0]
def y_compare(dot):
    return dot[1]

dots.sort(key=y_compare)
dots.sort(key=x_compare)

# Смотрим на поворот двух векторов - AB и BC
def rotate(A,B,C):
    return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

dot_left = dots[0]
dot_right = dots[-1]
hull_up = []
hull_down = [dot_left]

#В этом цикле вектор PK - вектор нижней левой и верхней правой точек
for i in range(1, len(dots)-1):                     #Проходим по всем точкам, кроме нижней левой и верхней правой
    if rotate(dot_left, dot_right, dots[i]) > 0:    # при > 0 - поворот левый, значит точка сверху отн. вектора PK
        hull_up.append(dots[i])                     # значит мы ее запишем в hull_up.
    elif rotate(dot_left, dot_right, dots[i]) < 0:  # при < 0 - поворот правый относительно вектора PK
        hull_down.append(dots[i])                   # значит точка снизу

hull_up.append(dot_right)
hull_down.reverse()

hull_up_res = [dot_left]
hull_down_res = [dot_right]

def make_hull(hull_res, hull): # для построения выпуклой оболочки нужны правые повороты отн. вектора AB
    for i in range(len(hull)):
        while len(hull_res) >= 2 and rotate(hull_res[-2], hull_res[-1], hull[i]) > 0:
            hull_res.pop()
        hull_res.append(hull[i])
    return hull_res

hull_up_res = make_hull(hull_up_res, hull_up)
hull_down_res = make_hull(hull_down_res, hull_down)

print('Выпуклая оболочка:', hull_up_res + hull_down_res[1:-1])