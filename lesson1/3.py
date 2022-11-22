x = int(input('Введите значение по оси x '))
y = int(input('Введите значение по оси y '))

if x > 0 and y > 0: {
        print (x, y, '-> 1')
    }
elif x < 0 and y > 0: {
        print (x, y, '-> 2')
    }
elif x < 0 and y < 0: {
        print (x, y, '-> 3')
}   
else: {
        print (x, y, '-> 4')
}
