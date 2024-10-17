# Тема: Логический тип Bool. Условия if-else

# Задание 1: Проверьте, является ли число 7 положительным, и выведите сообщение "Число положительное" если да.
#
# a = 7
# if a > 0:
#      print('Число положительное')
# elif a == 0:
#      print('Ни положительное, ни отрицательное')
# else:
#      print('Число отрицательное')
# print()
#
# Задание 2: Проверьте, четное ли число 8, и выведите соответствующее сообщение: "Число четное" или "Число нечетное".
#
# x = int(input('Введите число: '))
# if x % 2 == 0:
#     print('Число чётное')
# else:
#     print('Число нечётное')
# print()
#
# Задание 3: Определите, является ли строка "Hello" пустой, и выведите соответствующее сообщение:
# "Строка пустая" или "Строка не пустая".
#
# b = input()
# if len(b) == 0:
#     print('Строка пустая')
# else:
#     print('Строка не пустая')
# print()
#
# Задание 4: Определите, является ли температура выше 30 градусов. Если да, то выведете "Очень жарко",
# если нет, то "Не очень жарко".
# temperature = 25
#
# temperature = 25
# temperature = 25
# if temperature >= 30:
#     print('Очень жарко')
# else:
    # print('Не очень жарко')
# print()
#
# Задание 5: Проверьте, начинается ли строка с заглавной буквы. Если да, то выведите длину строки.
#
# str1=input('Введите строчку: ')
# if str1[0]<='a':
#     print(len(str1))
# print()
#
# a = input()
# if a.istitle():
#     print(len(a))
# print()
#
# Задание 6: Определите, делится ли число на 5 без остатка.
# Если делится, то умножьте его на два, если нет, то поделите на прибавьте к числу 5.
# num = 20
#
# num = 20
# if num % 5 == 0:
#     print(num * 2)
# else:
#     print(num + 2)
# print()
#
# Задание 7: Определите, является ли число отрицательным, нулем или положительным.
# Выведите соответствующее сообщение: "Число положительное", "Число отрицательное", "Число равно нулю".
#
# x = int(input())
# if x == 0:
#     print('Null')
# elif x > 0:
#     print('+')
# else:
#     print('-')
# print()

# Тема: Вложенные условия и множественный выбор. Тернарный оператор

# Задание 1: Определите, принадлежит ли число 14 интервалу от 10 до 20 включительно.
# Выведите соответствующее сообщение: "Число принадлежит интервалу от 10 до 20", "Число больше 20", "Число меньше 10".
#
# num = int(input())
# if num >= 10 and num <= 20:
#     print('The number belongs to the interval from 10 to 20')
# elif num > 20:
#     print('>20')
# elif num < 10:
#     print('<10')
# print()
# num = 14
# if num < 10:
#     print('number less than 10')
# elif num > 20:
#     print("number more than 20")
# else:
#     print("The number belongs to the interval from 10 to 20")
# print()
#
# Задание 2: Проверьте, является ли строка пустой или начинается с пробела.
# Выведите соответствующее сообщение: "Строка пустая", "Строка начинается с пробела", "Строка не начинается с пробела".
# text = " example"
#
# str = input()
# if len(str) == 0:
#     print('blank string')
# elif str.startswith(" "):
#     print('string starts with space')
# else:
#     print('string doesn't starts with space')
# print()
#
# text = " example"
# if len(text) == 0:
#     print("blank string")
# else:
#     if text[0] == ' ':
#         print('string starts with space')
#     else:
#         print('string doesn't starts with space')
# print()
#
# Задание 3: Определите размер скидки и выведите ее размер в консоль.
# Если покупка стоит до 10 долларов, то скидки нет, если до 50, то скидка 10%, если больше 50, то 15%.
# my_sum = 68
#
# num = float(input())
# if num <= 10:
#     print('No discount')
# elif num > 10 and num <= 50:
#     print('discount 10%')
# elif num > 50:
#     print('discount 15%')
# print()
#
# my_sum = 68
# if my_sum < 10:
#     print("No discount")
# elif my_sum <= 50:
#     print('discount 10%')
# else:
#     print('discount 15%')
# print()
#
# Задание 4: Проверьте длину пароля и выведите соответствующее сообщение:
# до 8 символов "Короткий пароль", до 16 символов "Средний пароль", больше "Длинный пароль"
# password = "Привет"
#
# a = input()
# if len(a) <= 8:
#     print('Short password')
# elif len(a) <= 16:
#     print('Average password')
# else:
#     print('Long password')
# print()
#
# Задание 5: Проверьте, содержит ли строка символ '@'.
# Если да, то выведите сообщение "Это email", если нет, то "Введите email".
# Проверить наличие символа в строке можно так: <символ> in <строка>
#
# str = input()
# if '@' in str:
#     print('This is email')
# else:
#     print('Enter email address')
# print()
#
# Задание 6: Определите, является ли число положительным или отрицательным с помощью тернарного оператора.
# num = -10
#
# a = int(input())
# result = "Positive" if a >= 0 else "Negative"
# print(result)
# print()
#
# Задание 7: Проверьте, четное или нечетное число с помощью тернарного оператора.
# num = 7
#
# a = int(input())
# result = 'even' if a % 2 == 0 else 'odd'
# print(result)
# print()
#
# Задание 8: Определите, является ли строка пустой или нет с помощью тернарного оператора.
# text = "Hello"
#
# a = input()
# result = 'Blank' if len(a) == 0 else 'Filled'
# print(result)
# print()
#
# Задание 9: Проверьте, начинается ли строка с заглавной буквы с помощью тернарного оператора.
# city = "Berlin"
#
# a = input()
# result = 'Big letter' if a[0].istitle() else 'small'
# print(result)
# print()

# Тема: Логические операторы: and, or, not

# Мини проект: Калькулятор
# Создайте простой калькулятор, который может выполнять основные арифметические операции:
# сложение, вычитание, умножение и деление.
#
# Требования:
# Программа должна запрашивать у пользователя два числа и операцию (+, -, *, /).
# Программа должна выполнять выбранную операцию и выводить результат, например: "Результат вычисления 2 + 3 равен 5"
# В противном случае вывести сообщение: "Ввод не может быть обработан".
#
# a = float(input('Enter the first number: '))
# b = input('Enter the operation: ')
# c = float(input('Enter the second number: '))
# if b == '+':
#     print(a + c)
# elif b == '-':
#     print(a - c)
# elif b == '*':
#     print(a * c)
# elif b == '/':
#     print(a / c)
# elif c == 0:
#     print('The input could not be processed.')
# else:
#     print('The input could not be processed.')
