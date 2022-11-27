import math

number = float(input('Введите вещественное число: '))

summ = 0

while (number != 0):
    summ = summ + number % 10
    number = number // 10
   




print("Сумма цифр числа равна: ", summ)

#не получается сложение чисел с точкой (гугл тоже не особо помог(((()