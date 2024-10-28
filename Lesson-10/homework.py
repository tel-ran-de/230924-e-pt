# Тема: Цикл while. Операторы break, continue, else.

# Упражнение 1: Поиск числа
#
# Напишите программу, которая запрашивает у пользователя числа, пока он не введет число совпадающее
# с переменной num (num = любое число от 0 до 100).  Если введенное число меньше num, программа должна
# выводить сообщение "Слишком маленькое число" и продолжать запрашивать числа. Если число больше num,
# программа должна вывести сообщение "Вы ввели большее число" и продолжать запрашивать числа.
# Если пользователь угадал, то программа должна вывести "Вы угадали число" и завершиться.

# num = 30
# while True:
#     guess = int(input('Enter any number from 0 to 100: '))
#     if guess > 30:
#         print('You have entered too big number')
#     elif guess < 30:
#         print('You have entered too small number')
#     else:
#         print('You guessed the number!')
#         break


# Упражнение 2: Проверка пароля
#
# Напишите программу, которая будет запрашивать у пользователя пароль до тех пор, пока не будет введен
# правильный пароль "python123", либо пока не закончатся попытки. Если введенный пароль содержит пробелы,
# программа должна выводить сообщение "Пароль не должен содержать пробелов" и продолжать запрашивать пароль.
# Если введен правильный пароль, программа должна выводить сообщение "Доступ разрешен" и завершаться.
# Если после трех неправильных попыток пароль не введен правильно, программа должна выводить сообщение
# "Превышено количество попыток" и завершаться.

# attempts = 0
# password = 'python123'
# while True:
#     enter = input('Password: ')
#     if attempts == 3:
#         print('You\'ve reached attempts limit')
#         break
#     elif ' ' in enter:
#         print('Wrong password. Password should not nave spaces')
#         attempts += 1
#     elif enter != password:
#         print('Wrong password')
#         attempts += 1
#     else:
#         print('You\'ve guessed password')
#         break
#





# Упражнение 3: Работа со списком покупок
#
# Напишите программу, которая будет запрашивать у пользователя элементы для списка покупок до тех пор,
# пока не будет введено слово "стоп", либо пока количество покупок не станет больше 6. Если введенное
# слово уже есть в списке, программа должна выводить сообщение "Этот элемент уже в списке" и продолжать
# запрашивать новые элементы. Если введено слово "стоп", программа должна выводить сообщение
# "Формирование списка завершено" и завершаться. Если количество покупок ставится больше 6,
# то программа должна вывести: “Превышен лимит покупок.” и завершиться.
# Перед завершением программа должна выводить итоговый список покупок и общее количество элементов в нем.
#
# list = []
# product = ''
# counter = 0
# while product != 'stop' or counter != 6:
#     product = input('Enter product name: ')
#     if product == 'stop':
#         print('List has been created')
#         print(list)
#         break
#     elif counter == 6:
#         print('Products limit reached')
#         print(list)
#         break
#     if product in list:
#         print('You already have this product')
#     else:
#         list.append(product)
#         print('Product has been added')
#         counter += 1
# else:
#     print(list)


# Тема: Цикл for

# Упражнение 1: Подсчет гласных в строке
#
# Напишите программу, которая принимает строку от пользователя и подсчитывать количество гласных букв (a, e, i, o, u)
# в этой строке.Используйте цикл for и условие if.

# vowels = list('aeiou')
# word = input('Введите слово: ')
# counter=0
# for char in word:
#     if char in vowels:
#         counter += 1
# print('Vowels amount: ', counter)




# Упражнение 2: Генерация и вывод последовательности чисел
#
# Напишите программу, которая генерит и выводит последовательность чисел от 1 до 20,
# но выводит "Fizz" вместо чисел, кратных 3, "Buzz" вместо чисел, кратных 5, и "FizzBuzz"
# вместо чисел, кратных как 3, так и 5. Используйте цикл for и функцию range.


# for digit in range(1, 21):
#     if digit % 3 == 0 and digit % 5 == 0:
#         print('FizzBuzz')
#     if digit % 3 == 0:
#         print('Fizz')
#     elif digit % 5 == 0:
#         print('Buzz')
#     else:
#         print(digit)



# Проект 1: Управление библиотекой
#
# Описание:
# Разработайте программу для управления библиотекой. Программа должна позволять добавлять книги в библиотеку,
# удалять книги, искать книги по автору и выводить список всех книг с их авторами и статусами (в наличии или выдана).
#
# Требования: Реализуйте работу всех пунктов меню.
#
# Продолжите программу ниже.


# library = [["Война и мир", "Толстой", "в наличии"],
#             ["Преступление и наказание", "Достоевский", "выдана"],
#             ["Мастер и Маргарита", "Булгаков", "в наличии"]]
# while True:
#     print("\nМеню")
#     print("1. Показать список всех книг")
#     print("2. Добавить книгу")
#     print("3. Удалить книгу")
#     print("4. Поменять статус книги")
#     print("5. Показать книги определенного автора")
#     print("6. Показать книги с определенным статусом")
#     choice = input("Выберите действие, введя его номер: ")
#     if choice == '1':
#         for number, book in enumerate(library):
#             print(f'{number + 1}. {book[0]}, {book[1]}, {book[2]}')
#     elif choice == '2':
#         new_book = input('Название книги: ')
#         book_auth = input('Автор: ')
#         book_status = input('Наличие:')
#         library.append([new_book, book_auth, book_status])
#         print('Книга добавлена')
#     elif choice == '3':
#         del_book = input('Название книги, чтобы удалить: ')
#         for book in library:
#             if book[0] == del_book:
#                 library.remove(book)
#                 print(f'Книга "{del_book}" удалена')
#     elif choice == '4':
#         book_title = input('Введите книгу, чтобы изменить статус: ')
#         for book in library:
#             if book[0] == book_title:
#                 book_status = input('в наличии/выдана: ')
#                 book[2] = book_status
#                 print('Статус изменен')
#     elif choice == '5':
#         srch_auth = input('Введите автора книг: ')
#         for number, book in enumerate(library):
#             if book[1] == srch_auth:
#                 print(f'{number + 1}. {book[0]}, {book[2]}')
#     elif choice == '6':
#         srch_status = input('Введите статус книг: ')
#         for number, book in enumerate(library):
#             if book[2] == srch_status:
#                 print(f'{number + 1}. {book[0]}, {book[1]}')



# Проект 2: Анализ посещаемости на сайте
#
# Разработайте программу для анализа посещаемости на сайте. Программа должна позволять вводить количество посещений
# за каждый день недели, определять дни с наибольшей и наименьшей посещаемостью, рассчитывать среднюю посещаемость
# за неделю и выводить дни с посещаемостью выше среднего.
#

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# while True:
#     print("\nMenu")
#     print('1. Enter amount of visits: ')
#     print('2. Day with max visits: ')
#     print('3. Day with min visits: ')
#     print('4. Average attendance: ')
#     choice = input('Select action: ' )
#     if choice == '1':
#         visits = []
#         for day in days:
#             visit = int(input(f'Enter number of visits for {day}: '))
#             visits.append(visit)
#     elif choice == '2':
#         max_visits = max(visits)
#         max_day = []
#         for i, visit in enumerate(visits):
#             if visits[i] == max(visits):
#                 max_day.append(days[i])
#         print(f'Day with max visits: {max_visits} on {', '.join(max_day)}')
#     elif choice == '3':
#         min_visits = min(visits)
#         min_day = []
#         for i, visit in enumerate(visits):
#             if visits[i] == min(visits):
#                 min_day.append(days[i])
#         print(f'Day with min visits: {min_visits} on {', '.join(min_day)}')
#     elif choice == '4':
#         avrg_visits = sum(visits) / len(visits)
#         print(f'Average attendance: {avrg_visits}')
#         above_avrg_days = []
#         for i, visit in enumerate(visits):
#             if visit > avrg_visits:
#                 above_avrg_days.append(days[i])
#         print(f'Days with attendance above average: {', '.join(above_avrg_days)}')
#     else:
#         print('Invalid choice. Try again.')
#         break