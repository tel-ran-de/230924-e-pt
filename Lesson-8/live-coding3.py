# Логические операторы: and, or, not
is_raining = bool(input('Введите\n1, если дождь или\n0 если не дождь: '))
temperature = float(input('Введите температуру: '))

if is_raining or temperature < 18:
    print('Не выходи из комнаты')
else:
    print('Пора гулять!')

# x = int(input('Введите число: '))
# if x > 0 and x % 2 == 0:
#     print('Число положительное и чётное')
# else:
#     print('Не подошло под условия')

# y = int(input('Введите число: '))
# if not y % 11 == 0:
#     print('Число не делится на 11 без остатка')
# else:
#     print(y / 11)

# or
# False or False = False
# False or True = True
# True or False = True
# True or True = True

# and
# False and False = False
# False and True = False
# True and False = False
# True and True = True

# not
# not False = True
# not True = False
