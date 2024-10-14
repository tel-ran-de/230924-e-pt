# ДАННЫЕ И ПЕРЕМЕННЫЕ
# Продемонстрируйте работу переменных и разных типов данных. Объясните механизм работы кода.

######
# - Переменные с разным типом данных: строками, целыми и дробными числами
x = 7
y = 19
pi = 3.1415926
e = 2.7
name = 'Steven'
group_name = "230924-e-pt"

several_lines = '''тут
можно
хранить
несколько
строк'''

several_lines2 = """тут тоже
можно
хранить
текст
в
несколько
строк"""

######
# - Вывод типа данных через print(type())
# функция()
print('Hello world!')
print(x)
print(pi)
print(group_name)
print(several_lines)

# функция type() — показывает тип данных переменной
print(type(x))  # int — целое число
print(type(pi))  # float — дробное число
print(type(group_name))  # str — строка

# функция id() — показывает адрес переменной в памяти
print(id(x))
print(id(pi))
print(id(group_name))


######
# - Обращение к несуществующим переменным или объявленным ниже
# print(city)
# city = 'Tashkent'
# возникнет ошибка NameError: name 'city' is not defined

# напечатает пустую строку
print()

# - Переприсваивание, каскадное присваивание, множественное присваивание
cat_name = 'Tom'
print(cat_name)
print(id(cat_name))
cat_name = 'Scratch'
print(cat_name)
print(id(cat_name))

a = b = c = 100
# аналогично такой записи:
# a = 100
# b = 100
# c = 100
print(id(a))
print(id(b))
print(id(c))
print(a)
print(b)
print(c)

# - Наименования переменных
# нельзя называть переменные по имени встроенных функций
# print = 'принт'
# print(a)

# могут содержать в названии только маленькие буквы, цифры и знаки подчёркивания
# могут начинаться со знака подчёркивания, но не могут начинаться с цифры
cats_count = 19
username = 'Fedot'
_temp_variable = 0
password = 88888888
password2 = 88888888


# ЧИСЛА И ОПЕРАЦИИ НАД НИМИ
# Продемонстрируйте работу с числами и арифметическими операциями.
# Объясните механизм работы кода.
# - Разные типы чисел: int, float
# - Выполнение арифметических операций +, -, *, /, //, %, **
# - Сокращенная запись +=, -=, *=, /=, //=, %=, **= и т.д.
# - Применение встроенных математических функций

######
# сложение
print()
print(5 + 5)
print(5 + 1.1)
print()
# вычитание
print(2 - 1)
print(9.2 - 3)
print(9.7 - 3)
print(5.4 - 2)
print()
# умножение
print(5 * 10)
print(4 * 1.1)
print()
# деление
print(4 / 2)
print(3.2 / 1)
print(7 / 2.3)
print()
# целочисленное деление
print(7 // 2)
print(13 // 3)
print(19 // 5)
print()
# остаток от деления
print(7 % 2)
print(13 % 3)
print(19 % 5)
print()
# возведение в степень
print(2 ** 10)
print(3 ** 4)
print(11 ** 2)
print()
# присваивание
i = 10
print(i)
i = i + 1
print(i)
i += 1
print(i)
# i = i ** 2
i **= 2
print(i)

print()
# приоритет операций можно изменить с помощью скобок
value_1 = 2 + 3 * 6
value_2 = (2 + 3) * 6
print(value_1)
print(value_2)

print()
# встроенные математические функции
print(abs(2))  # 2
print(abs(-2))  # 2
print(abs(10.1))  # 10.1
print(abs(-11.2))  # 11.2

print()
# ** возведение в степень
# pow() так же возведение в степень
print(2 ** 12)
print(pow(2, 12))
# если мы хотим извлечь квадратный корень, то мы должны возвести число в степень 1/2
print(144 ** 0.5)
print(pow(144, 1/2))

print(round(1.213123))
print(round(1.523143))
print(round(-1.524231))

print(round(1.213123, 3))
print(round(1.523143, 3))
print(round(-1.524231, 3))

# ФУНКЦИИ PRINT(), INPUT()
# Продемонстрируйте работу:
# - print()
# - input()
# - sep=
# - end=
# - строки и переменные в print(), input()
#
# Объясните механизм работы кода.

# print() — выводит в консоль
print()
group_name = '230924-e-pt'
print(1, 2, 3, 'Hello', group_name, 3.14)
print(1, 2, 3, 'Hello', group_name, 3.14, sep='—')
print(1, 2, 3, 'Hello', group_name, 3.14, sep='\n')
print(1, 2, 3, 'Hello', group_name, 3.14, end='!!!')
print()
print(1, 2, 3, 'Hello', group_name, 3.14, sep='<>', end='!!!')
print()
print()


# input() — принимает данные от пользователя из консоли
# любое введённое значение input() превращает в str
name = input('Введите своё имя: ')
print(name)
print('Привет, ', name, '!')

print()
# будет ошибка, так как нельзя разделить строку
# number = input('Введите число: ')
# print(type(number))
# print(number / 2)

# функция int() приводит (или конвертирует значение в целое число)
number = int(input('Введите число: '))
print(type(number))
print(number / 2)
