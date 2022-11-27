from random import randint as rnd
import random

size = int(input('Введите размер списка: '))

rnd_list = []

for i in range(size):
    rnd_list.append(rnd(0,100))


print(rnd_list)
print(sorted(rnd_list))

