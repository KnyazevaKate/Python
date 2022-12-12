my_list = list(map(float, input('Введите вещественные числа: ').split()))

new_my_list = [round(i % 1,2) for i in my_list if i % 1 != 0]

print(max(new_my_list) - min(new_my_list))