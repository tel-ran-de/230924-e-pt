a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = ("Введите знак операции: +, -, *, / ")
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    print(a/b)
else:
    print("Ввод не может быть обработан")
