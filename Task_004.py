# Задайте число N и создайте список, заполненный числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

with open("file.txt") as file: # выгрузка значений из файла.
    x = int(file.readline())
    y = int(file.readline())
    z = int(file.readline())

n = int(input('Введите N: '))
line_n = range(-n, n+1)        # заполнение строки по параметрам
for i in line_n:
    print(i, end=', ')
print(f'\n{x}, {y}, {z}')
print(f'{line_n[x]*line_n[y]*line_n[z]}')
