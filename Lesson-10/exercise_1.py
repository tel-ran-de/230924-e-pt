# Тема: Цикл while. Операторы break, continue, else.
#
# Упражнение 1: Поиск числа
#
# Напишите программу, которая запрашивает у пользователя числа, пока он не введет число совпадающее
# с переменной num (num = любое число от 0 до 100).  Если введенное число меньше num, программа должна
# выводить сообщение "Слишком маленькое число" и продолжать запрашивать числа. Если число больше num,
# программа должна вывести сообщение "Вы ввели большее число" и продолжать запрашивать числа.
# Если пользователь угадал, то программа должна вывести "Вы угадали число" и завершиться.

# num = 0
# while num != 10:
#     num = int(input("Введите любое число от 0 до 100: "))
#     if num > 10:
#         print('Вы ввели слишком большое число')
#     elif num < 10:
#         print('Вы ввели слишком маленькое число')
# else:
#     print('Вы угадали!')

# num = int(input())
# while 0 <= num <= 100:
#     print("Вы угадали число")
#     break
# if num > 100:
#     print("Вы ввели большее число")
# if num < 0:
#     print("Вы ввели меньшее число")



# Упражнение 2: Работа со списком покупок
#
# Напишите программу, которая будет запрашивать у пользователя элементы для списка покупок до тех пор,
# пока не будет введено слово "стоп", либо пока количество покупок не станет больше 6. Если введенное
# слово уже есть в списке, программа должна выводить сообщение "Этот элемент уже в списке" и продолжать
# запрашивать новые элементы. Если введено слово "стоп", программа должна выводить сообщение
# "Формирование списка завершено" и завершаться. Если количество покупок ставится больше 6,
# то программа должна вывести: “Превышен лимит покупок.” и завершиться.
# Перед завершением программа должна выводить итоговый список покупок и общее количество элементов в нем.