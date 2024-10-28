# Продемонстрируйте работу булевых переменных и операторов сравнения.
print('булевы переменные')
print('apple' < 'banana')
print('вода' < 'водяной')
print('водопровод' < 'водяной')
print('a' < 'а')  # латинская а и кириллическая а
print('A' < 'a')

print('apple' == 'Apple')
print('apple' != 'Apple')

is_raining = True
print(type(is_raining))
is_sunny = False
print(type(is_sunny))

a = 5
b = 10
print(a == b)  # False
print(a != b)  # True
print(a > b)  # False
print(a < b)  # True
print(a >= b)  # False
print(a <= b)  # True

x = 5
y = 5.0
print(x == y)  # True
x1 = 5  # 5.0
y1 = 5.1
print(x1 == y1)  # False
print()

# Продемонстрируйте работу условных операторов if и if-else.
print('операторы if & if-else')
a = 5
if a > 0:
    print('a больше нуля')

b = -3
if b > 0:
    print('b больше нуля')
else:
    print('b не больше нуля')

x = int(input('Введите число: '))
if x % 2 == 0:
    print('число чётное')
else:
    print('число нечётное')
