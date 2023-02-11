# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств


import random
n = int(input('Введите число N ')) 
x = int(input('Введите число Х ')) 


def Result(n,x):
    list_1 = []
    list_2 = []
    
    for i in range(-n,n):
        list_1.append(random.randint(1, n+1))
        # print(list_1)

    for i in range(-x,x):
        list_2.append(random.randint(1, x+1))
        # print(list_2)

    my_set_1= set(list_1)
    my_set_2= set(list_2)
    
    my_set_3 = my_set_1.union(my_set_2)
    
    return sorted(my_set_3)

print(f'Отсортированное множество {Result(n,x)}')







