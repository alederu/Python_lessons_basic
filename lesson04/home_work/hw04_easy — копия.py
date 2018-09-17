# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

original_list = [1, 2, 4, 0]
new_list = list(map(lambda x:x**2, original_list[:]))

print('list_1:', original_list)
print('list_2:', new_list)

# с генератором
newest_list = [el**2 for el in original_list[:]]

print('list_1:', original_list)
print('list_2:', newest_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list_1 = ['Апельсин', 'Мандарин', 'Яблоко', 'Киви', 'Лимон']
fruit_list_2 = ['Манго', 'Грейпфрут', 'Апельсин', 'Банан', 'Лимон', 'Киви']
result_list = [i for i in fruit_list_1 if i in fruit_list_2]
print(result_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

from random import randint

int_list = [randint(-100, 100) for j in range(0, 10)]
conditioned_list = [i for i in int_list if i >= 0 and i%4 and not i%3]
print(int_list)
print(conditioned_list)
