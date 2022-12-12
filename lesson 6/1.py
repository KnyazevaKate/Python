import math

number = (input('Введите вещественное число: '))


print(sum(map(int, filter(str.isdigit, number))))