# Задайте число N и создайте список, заполненный числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

#Var my

# with open("file.txt") as file: # выгрузка значений из файла.
#     x = int(file.readline())
#     y = int(file.readline())
#     z = int(file.readline())

# n = int(input('Введите N: '))
# line_n = range(-n, n + 1)        # заполнение строки по параметрам
# for i in line_n:
#     print(i, end=', ')
# print(f'\n{x}, {y}, {z}')
# print(f'{line_n[x]*line_n[y]*line_n[z]}')

# Var Albina

from unittest import result


pos = []                         # создание списка для файла
with open("file.txt") as f:      # открываем файл
    pos = f.read().split()      # read - чтение всего файла, split - разбивка данных в файле по пробелам и переводам строк 
    pos = [int(i) for i in pos] # записывание данных из файла в виде списка в симействе int (внутренним циклом for)
n = int(input('Введите целое число: '))
s = []
for i in range(-n, n + 1):
    s.append(i)
result = 1
for i in range(len(pos)):
    result *= s[pos[i]]
print(f'Исходный список: {s}.\nПозиции: {pos}.')
print(result)
