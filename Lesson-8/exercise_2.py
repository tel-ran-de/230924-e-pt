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
# text = " example"
text = " exemple"
if len(text) == 0:
    print("Строка пуста")
elif text.startswith(" "):
    print("Строка начинается с пробела")
else:
    print("Строка не начинается с пробела")

# Задание 3: Определите размер скидки и выведите ее размер в консоль.
# Если покупка стоит до 10 долларов, то скидки нет, если до 50, то скидка 10%, если больше 50, то 15%.
# my_sum = 68
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
# password = "Привет"
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
# num = -10
num = -10
res = "Отрицательное" if num < 0 else "Положительное"
print(res)

# Задание 7: Проверьте, четное или нечетное число с помощью тернарного оператора.
# num = 7
num = 7
res = "Чётное" if num % 2 == 0 else "Нечётное"
print(res)

# Задание 8: Определите, является ли строка пустой или нет с помощью тернарного оператора.
# text = "Hello"
text = "Hello"
print("Строка не пуста" if len(text) > 0 else "Строка пуста")

# Задание 9: Проверьте, начинается ли строка с заглавной буквы с помощью тернарного оператора.
# city = "Berlin"
city = "Berlin"
print("Строка начинается с заглавной буквы" if city.istitle() else "Строка начинается с маленькой буквы")






