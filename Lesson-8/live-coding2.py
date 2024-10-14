# Продемонстрируйте и объясните работу:
# - Вложенных условий
# - Конструкции if-elif-else
# - Тернарного условного оператора
# print('Вложенное условие')
# a = int(input('Введите число: '))
# if a > 0:
#     if a % 2 == 0:
#         print('число положительное чётное')
#     else:
#         print('число положительное нечётное')
# else:
#     if a % 2 == 0:
#         print('число отрицательное чётное')
#     else:
#         print('число отрицательное нечётное')
# print()

# print('Конструкция if-elif-else')
# score = float(input())
# if score > 100:
#     print('Таких высоких оценок не бывает!')
# elif score >= 80:
#     print(5)
# elif score >= 60:
#     print(4)
# elif score >= 40:
#     print(3)
# elif score >= 20:
#     print(2)
# elif score >= 0:
#     print(1)
# else:
#     print('Вы ввели неверную оценку!!!')

print('тернарный оператор')
number = int(input('Введите целое число: '))
# # if number >= 0:
# #     result = 'Неотрицательное'
# # else:
# #     result = 'Отрицательное'
result = 'Неотрицательное' if number >= 0 else 'Отрицательное'
# result = 'Положительное' if number > 0 else ('Отрицательное' if number < 0 else 'Ноль')
print(result)

# print('Неотрицательное' if int(input('Введите целое число: ')) >= 0 else 'Отрицательное')
