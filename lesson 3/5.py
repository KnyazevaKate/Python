#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
#Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



def fibonacci(number):
    my_list = [1, 5]
    for i in range(2, number + 1):
        my_list.append(my_list[i-1] + my_list[i-2])
        #my_list.insert(0, -i) - с отрицательными числами не получилось
    print(my_list)
 
number = 8
fibonacci(number)      

 