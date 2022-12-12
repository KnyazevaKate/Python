my_list = []


def mult_my_list(my_list):

    l = len(my_list) // 2 + 1 if len(my_list) % 2 != 0 else len(my_list) // 2

    new_my_list = [my_list[i] * my_list[len(my_list) - i - 1] for i in range(l)]

    print(new_my_list)


mult_my_list(my_list)

my_list = list(map(int, input('Введите числа: ').split()))

mult_my_list(my_list)