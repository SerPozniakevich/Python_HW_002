#Задайте список из n чисел последовательности (1+ (1/n))^n 
# и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55

a = int(input('Введите N: '))
sum_sequ = 0
for i in range(a):
    i += 1
    sum_sequ += (1 + (1 / i)) ** i
print(f'Для N = {a}: сумма = {round(sum_sequ, 2)}')