# Тема: Цикл while. Операторы break, continue, else.
#
# Упражнение 1: Поиск числа
#
# Напишите программу, которая запрашивает у пользователя числа, пока он не введет число совпадающее
# с переменной num (num = любое число от 0 до 100).  Если введенное число меньше num, программа должна
# выводить сообщение "Слишком маленькое число" и продолжать запрашивать числа. Если число больше num,
# программа должна вывести сообщение "Вы ввели большее число" и продолжать запрашивать числа.
# Если пользователь угадал, то программа должна вывести "Вы угадали число" и за
Упражнение 2: Работа со списком покупок
#
# Напишите программу, которая будет запрашивать у пользователя элементы для списка покупок до тех пор,
# пока не будет введено слово "стоп", либо пока количество покупок не станет больше 6. Если введенное
# слово уже есть в списке, программа должна выводить сообщение "Этот элемент уже в списке" и продолжать
# запрашивать новые элементы. Если введено слово "стоп", программа должна выводить сообщение
# "Формирование списка завершено" и завершаться. Если количество покупок ставится больше 6,
# то программа должна вывести: “Превышен лимит покупок.” и завершиться.

# Перед завершением программа должна выводить итоговый список покупок и общее количество элементов в нем.


t = 4
while True :
     p = input('Введите пароль:')
     if p == 'pyton123':
       print('Доступ разрешен')
       break
     if ' ' in p :
         print('Пароль не должен содержать пробелов')
     t -= 1
     if t > 0:
       print('Осталось', t)
     else:
       print('Превышено количество попыток')
       break

# Перед завершением программа должна выводить итоговый список покупок и общее количество элементов в нем.
