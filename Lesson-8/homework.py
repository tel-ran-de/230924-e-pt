# Тема: Логический тип Bool. Условия if-else

# Задание 1: Проверьте, является ли число 7 положительным, и выведите сообщение "Число положительное" если да.
num = 7
if 7 > 0:
    print("Число положительное")

# Задание 2: Проверьте, четное ли число 8, и выведите соответствующее сообщение: "Число четное" или "Число нечетное".
num_2 = 8
if num_2 % 2 ==0:
    print("Число чётное")
else:
    print("Число нечётное")

# Задание 3: Определите, является ли строка "Hello" пустой, и выведите соответствующее сообщение:
# "Строка пустая" или "Строка не пустая".
str_1 = "Hello"
if len(str_1) == 0:
    print("Строка пустая")
else:
    print("Строка не пустая")

# Задание 4: Определите, является ли температура выше 30 градусов. Если да, то выведете "Очень жарко",
# если нет, то "Не очень жарко".
tem = 25
if tem > 30:
    print("Очень жарко")
else:
    print("Не очень жарко")

# Задание 5: Проверьте, начинается ли строка с заглавной буквы. Если да, то выведите длину строки.
str_2 = "Morgen"
if str_2.istitle():
    print(len(str_2))
else:
    print("Строка начинается с маленькой буквы")

# Задание 6: Определите, делится ли число на 5 без остатка.
# Если делится, то умножьте его на два, если нет, то прибавьте к числу 5.
numb = 20
if numb % 5 == 0:
    print(numb * 2)
else:
    print(numb +5)

# Задание 7: Определите, является ли число отрицательным, нулем или положительным.
# Выведите соответствующее сообщение: "Число положительное", "Число отрицательное", "Число равно нулю".
x = float(input("Введите чмсло: "))
if x > 0:
    print("Число положительное")
elif x < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# Тема: Вложенные условия и множественный выбор. Тернарный оператор

# Задание 1: Определите, принадлежит ли число 14 интервалу от 10 до 20 включительно.
# Выведите соответствующее сообщение: "Число принадлежит интервалу от 10 до 20", "Число больше 20", "Число меньше 10".
numb = 14
if 10 <= numb <= 20:
    print("Число принадлежит к интервалу от 10 до 20")
elif numb < 10:
    print("Число меньше 10")
else:
    print("Число больше 20")

# Задание 2: Проверьте, является ли строка пустой или начинается с пробела.
# Выведите соответствующее сообщение: "Строка пустая", "Строка начинается с пробела", "Строка не начинается с пробела".
text = " exemple"
if len(text) == 0:
    print("Строка пуста")
elif text.startswith(" "):
    print("Строка начинается с пробела")
else:
    print("Строка не начинается с пробела")

# Задание 3: Определите размер скидки и выведите ее размер в консоль.
# Если покупка стоит до 10 долларов, то скидки нет, если до 50, то скидка 10%, если больше 50, то 15%.
my_sum = 68
if 0 < my_sum < 10:
    print("Скидки нет")
elif 10 <= my_sum <= 50:
    print("Скидка составляет 10%: ", my_sum * 0.1)
elif my_sum > 50:
    print("Скидка составляет 15%: ", my_sum * 0.15)
else:
    print("Цена покупки должна быть больше нуля")

# Задание 4: Проверьте длину пароля и выведите соответствующее сообщение:
# до 8 символов "Короткий пароль", до 16 символов "Средний пароль", больше "Длинный пароль"
password = "Привет"
if len(password) < 8:
    print("Короткий пароль")
elif 8 <= len(password) <=16:
    print("Средний пароль")
else:
    print("Длинный пароль")

# Задание 5: Проверьте, содержит ли строка символ '@'.
# Если да, то выведите сообщение "Это email", если нет, то "Введите email".
# Проверить наличие символа в строке можно так: <символ> in <строка>
mail = input("Введите e-mail: ")
symbol = "@"
if symbol in mail:
    print("Это e-mail")
else:
    print("Введите e-mail")

# Задание 6: Определите, является ли число положительным или отрицательным с помощью тернарного оператора.
num = -10
print('ноль' if num == 0 else 'положительное' if num > 0 else 'отрицательное')

# Задание 7: Проверьте, четное или нечетное число с помощью тернарного оператора.
num = 7
print("Чётное" if num % 2 == 0 else "Нечётное")

# Задание 8: Определите, является ли строка пустой или нет с помощью тернарного оператора.
text = "Hello"
print("Строка не пуста" if len(text) > 0 else "Строка пуста")

# Задание 9: Проверьте, начинается ли строка с заглавной буквы с помощью тернарного оператора.
# city = "Berlin"
city = "Berlin"
print("Строка начинается с заглавной буквы" if city.istitle() else "Строка начинается с маленькой буквы")


# Тема: Логические операторы: and, or, not

# Мини проект: Калькулятор
# Создайте простой калькулятор, который может выполнять основные арифметические операции:
# сложение, вычитание, умножение и деление.
#
# Требования:
# Программа должна запрашивать у пользователя два числа и операцию (+, -, *, /).
# Программа должна выполнять выбранную операцию и выводить результат, например: "Результат вычисления 2 + 3 равен 5"
# В противном случае вывести сообщение: "Ввод не может быть обработан".
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
sign = input("Введите действие (+, -, *, /): ")
if sign not in ['+', '-', '*', '/']:
    print("К сожалению, операция невыполнима")
else:
    print(f'Результат вычисления {num1} {sign} {num2} равен', eval(f'{num1} {sign} {num2}'))