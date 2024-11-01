# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.

def sum_all(*args):
    return sum(args)

result = sum_all(1, 3, 55, 558, 666, 13)
print(result)