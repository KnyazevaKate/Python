#Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
#Пример:
#45 -> 101101
#3 -> 11
#2 -> 10

calc = ''
number = int(input('Введите число: '))
while number != 0:
    calc = str(number % 2) + calc
    number //= 2
print(calc)