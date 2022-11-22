
#Рассчет для 2D - пространства

'''from math import sqrt

coordinate_аx = int(input('Введите значение оси x первой точки: '))
coordinate_аy = int(input('Введите значение оси y первой точки: '))
coordinate_bx = int(input('Введите значение оси x второй точки: '))
coordinate_by = int(input('Введите значение оси y второй точки: '))

distance_2D = float(sqrt(((coordinate_аx - coordinate_bx)**2) + ((coordinate_аy - coordinate_by)**2)))

print(f'A {coordinate_аx, coordinate_аy},B {coordinate_bx, coordinate_by} -> {round(distance_2D, 3)}') # оставила 3 цыфры, так как при 2 - округление идет не всегда корректно (пример: вместо 5, 09 - 5.1)'''

#Рассчет для 3D - пространства

from math import sqrt

coordinate_аx = int(input('Введите значение оси x первой точки: '))
coordinate_аy = int(input('Введите значение оси y первой точки: '))
coordinate_bx = int(input('Введите значение оси x второй точки: '))
coordinate_by = int(input('Введите значение оси y второй точки: '))
coordinate_zx = int(input('Введите значение оси x тертьей точки: '))
coordinate_zy = int(input('Введите значение оси y тертьей точки: '))

distance_3D = float(sqrt(((coordinate_аx - coordinate_bx)**2) + ((coordinate_аy - coordinate_by)**2) + ((coordinate_zx - coordinate_zy)**2)))

print(f'A {coordinate_аx, coordinate_аy},B {coordinate_bx, coordinate_by},C {coordinate_zx, coordinate_zy} -> {round(distance_3D, 3)}') 
