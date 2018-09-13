# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

    a, b = 1, 1
    f_list = [a, b]

    for i in range(3, m+1):
        c = a
        a = b
        b = c + a
        i += 1
        f_list.append(b)
    return(f_list[n-1:])

m = int(input("До какого элемента вывести:"))
n = int(input("С какого элемента начать:"))
x = fibonacci(n, m)

print(x)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):

    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return(origin_list)

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def bike_reinvented(condition, input_list):
    filtered_list = list()
    for i in input_list:
        if condition(i) == True:
            filtered_list.append(i)
        else:
            continue
    return filtered_list

input_list = list([2, 10, -10, 8, 2, 0, 14])
print(input_list)

u = int(input("Введи число для фильтра по выбранному знаку:"))
condition = lambda i: i > u

print(list((bike_reinvented(condition, input_list))))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

def distance(line):
    distance_line = math.sqrt(pow(line[2] - line[0], 2) + pow(line[3] - line[1], 2))
    return distance_line


print('Нижняя левая верщина A:')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('Верхняя левая верщина B:')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print('Верхняя правая верщина C:')
x3 = float(input('x3 = '))
y3 = float(input('y3 = '))

print('Нижняя правая верщина D:')
x4 = float(input('x4 = '))
y4 = float(input('y4 = '))

line_ab = list([x1, y1, x2, y2])
line_bc = list([x2, y2, x3, y3])
line_cd = list([x3, y3, x4, y4])
line_da = list([x4, y4, x1, y1])
line_ac = list([x1, y1, x3, y3])
line_bd = list([x2, y2, x4, y4])

q = distance(line_ab)
w = distance(line_bc)
e = distance(line_cd)
r = distance(line_da)
t = distance(line_ac)
y = distance(line_bd)


print(list(map(lambda x: x ** 2, [q, w, e, r, t, y])))

if ((t + y) - (q + w + e + r) < 0.001):
    print('паралелограмм')
else:
    print('fail fish')