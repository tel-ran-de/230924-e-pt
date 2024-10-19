# Тема: Цикл while. Операторы break, continue, else.

# Упражнение 1: Поиск числа
#
# Напишите программу, которая запрашивает у пользователя числа, пока он не введет число совпадающее
# с переменной num (num = любое число от 0 до 100).  Если введенное число меньше num, программа должна
# выводить сообщение "Слишком маленькое число" и продолжать запрашивать числа. Если число больше num,
# программа должна вывести сообщение "Вы ввели большее число" и продолжать запрашивать числа.
# Если пользователь угадал, то программа должна вывести "Вы угадали число" и завершиться.
print('Task # 1')
guess_num = 63
while True:
    check_num = int(input('Введите число от 0 до 100: '))
    if check_num > guess_num:
        print("Вы ввели большее число")
    elif check_num < guess_num:
        print("Слишком маленькое число")
    else:
        print("Вы угадали число")
        break
print('Task # 2')
# Упражнение 2: Проверка пароля
#
# Напишите программу, которая будет запрашивать у пользователя пароль до тех пор, пока не будет введен
# правильный пароль "python123", либо пока не закончатся попытки. Если введенный пароль содержит пробелы,
# программа должна выводить сообщение "Пароль не должен содержать пробелов" и продолжать запрашивать пароль.
# Если введен правильный пароль, программа должна выводить сообщение "Доступ разрешен" и завершаться.
# Если после трех неправильных попыток пароль не введен правильно, программа должна выводить сообщение
# "Превышено количество попыток" и завершаться.

password = "python123"
attempt_num = 3
attempt = 0
while True:
    user_input = input('Введите пароль: ')
    attempt += 1
    if ' ' in user_input:
        print("Пароль не должен содержать пробелов")
    if user_input == password:
        print("Доступ разрешен")
        break
    if attempt == attempt_num:
        break
    print(f'{attempt_num - attempt} attempt(s) remain!')

print('Task # 3')
# Упражнение 3: Работа со списком покупок
#
# Напишите программу, которая будет запрашивать у пользователя элементы для списка покупок до тех пор,
# пока не будет введено слово "стоп", либо пока количество покупок не станет больше 6. Если введенное
# слово уже есть в списке, программа должна выводить сообщение "Этот элемент уже в списке" и продолжать
# запрашивать новые элементы. Если введено слово "стоп", программа должна выводить сообщение
# "Формирование списка завершено" и завершаться. Если количество покупок ставится больше 6,
# то программа должна вывести: “Превышен лимит покупок.” и завершиться.
# Перед завершением программа должна выводить итоговый список покупок и общее количество элементов в нем.

articles_list = []
article_num = 6
stop_word = 'стоп'
counter = 0
while True:
    if len(articles_list) > 0:
        print('список покупок')
        for index, item in enumerate(articles_list, 1):
            print(f'{index}. {item}')
    article = input('Внесите планируемую покупку в список: ')
    if article == 'стоп':
        print("Формирование списка завершено")
        print('список покупок')
        for index, item in enumerate(articles_list, 1):
            print(f'{index}. {item}')
        break
    elif article in articles_list:
        print('Эта покупка уже в списке!')
        continue
    if counter == article_num:
        print('Превышен лимит покупок.')
        print('список покупок')
        for index, item in enumerate(articles_list, 1):
            print(f'{index}. {item}')
        break
    articles_list.append(article)
    counter += 1

# Тема: Цикл for

# Упражнение 1: Подсчет гласных в строке
#
# Напишите программу, которая принимает строку от пользователя и подсчитывать количество гласных букв (a, e, i, o, u)
# в этой строке.Используйте цикл for и условие if.
print('Тема: Цикл for Task # 1')
check_string = 'aeiou'
counter = 0
word = input('введите слово: ')
for letter in word:
    if letter in check_string:
        counter += 1
print(f'в слове {word} всего {counter} гласных букв')

print('Тема: Цикл for Task # 2')
# Упражнение 2: Генерация и вывод последовательности чисел
#
# Напишите программу, которая генерит и выводит последовательность чисел от 1 до 20,
# но выводит "Fizz" вместо чисел, кратных 3, "Buzz" вместо чисел, кратных 5, и "FizzBuzz"
# вместо чисел, кратных как 3, так и 5. Используйте цикл for и функцию range.
for number in range(1, 21):
    if number % 3 == 0:
        if number % 5 == 0:
         print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


print('project Управление библиотекой')
# Проект 1: Управление библиотекой
#
# Описание:
# Разработайте программу для управления библиотекой. Программа должна позволять добавлять книги в библиотеку,
# удалять книги, искать книги по автору и выводить список всех книг с их авторами и статусами (в наличии или выдана).
#
# Требования: Реализуйте работу всех пунктов меню.
#
library = [["Война и мир", "Толстой", "в наличии"],
           ["Преступление и наказание", "Достоевский", "выдана"],
           ["Мастер и Маргарита", "Булгаков", "в наличии"]]
status =["выдана", "в наличии"]
#
while True:
    print("\nМеню")
    print("1. Показать список всех книг")
    print("2. Добавить книгу")
    print("3. Удалить книгу")
    print("4. Поменять статус книги")
    print("5. Показать книги определенного автора")
    print("6. Показать книги с определенным статусом")
    print("0. если хотите покинуть программу")
    choice = int(input("Выберите действие, введя его номер: "))

    if choice == 1:
        print('список книг')
        print(60 * '-')
        print(f'| id |{4 * " "}author{4 * " "}|{11 * " "}title{10 * " "}|   Status  |')
        print(60 * '-')
        for index, book in enumerate(library, 1):
            print(f'|{(3 - len(str(index)))*' '}{index} |'
                  f'{(13 - len(book[1]))*' '}{book[1]} |'
                  f'{(25 - len(book[0]))*' '}{book[0]} |'
                  f'{(10 - len(book[2]))*' '}{book[2]} |')
            print(60 * '-')
    elif choice == 2:
        add_title = input('введите название книги: ')
        add_author = input('введите автора книги: ')
        library.append([add_title, add_author, 'в наличии'])
        print(f'книга с названием {add_title} автор {add_author} добавлена в библиотеку!')
    elif choice == 3:
        delete_title = input('введите название книги для удаления: ')
        delete_author = input('введите автора книги для удаления: ')
        for index, book in enumerate(library):
             if book[0].lower() == delete_title.lower() and book[1].lower() == delete_author.lower():
                library.pop(index)
                print(f'книга с названием {delete_title} автор {delete_author} удалена из библиотеки!')
                break
        else:
            print(f'книга с названием {delete_title} автор {delete_author} не найдена библиотеке!')
    elif choice == 4:
        update_title = input('введите название книги для изменения статуса: ')
        update_author = input('введите автора книги для изменения статуса: ')
        for book in library:
            if book[0].lower() == update_title.lower() and book[1].lower() == update_author.lower():
                print(f'книга с названием {update_title} автор {update_author} имеет статус {book[2]}')
                action = int(input('Если хотите изменить статус книги введите 1, если статус не меняется введите 0: '))
                if action == 1:
                    for item in status:
                        if item != book[2]:
                            book[2] = item
                            print(f'книга с названием {update_title} '
                                  f'автор {update_author} имеет новый статус {book[2]}!')
                            break
                else:
                    print(f'книга с названием {update_title} '
                          f'автор {update_author} имеет прежний статус {book[2]}!')
                break
        else:
            print(f'книга с названием {update_title} автор {update_author} не найдена библиотеке!')
    elif choice == 5:
        author_list = []
        author = input('Введите имя автора: ')
        for book in library:
            if book[1].lower() == author.lower():
                author_list.append(book)
        if len(author_list) == 0:
            print('Книг заданного автора нет в библиотеке')
        else:
            print('список книг')
            print(60 * '-')
            print(f'| id |{4 * " "}author{4 * " "}|{11 * " "}title{10 * " "}|   Status  |')
            print(60 * '-')
            for index, book in enumerate(author_list, 1):
                print(f'|{(3 - len(str(index))) * ' '}{index} |'
                      f'{(13 - len(book[1])) * ' '}{book[1]} |'
                      f'{(25 - len(book[0])) * ' '}{book[0]} |'
                      f'{(10 - len(book[2])) * ' '}{book[2]} |')
                print(60 * '-')
    elif choice == 6:
        status_list = []
        index = int(input(f'Для поиска книг со статусом "выдана" введите 0 \n'
                       f'Для поиска книг со статусом "в наличии" введите 1: '))

        for book in library:
            if book[2] == status[index]:
                status_list.append(book)
        if len(status_list) == 0:
            print(f'Книг со статусом {status[index]} нет в библиотеке')
        else:
            print('список книг')
            print(60 * '-')
            print(f'| id |{4 * " "}author{4 * " "}|{11 * " "}title{10 * " "}|   Status  |')
            print(60 * '-')
            for index, book in enumerate(status_list, 1):
                print(f'|{(3 - len(str(index))) * ' '}{index} |'
                      f'{(13 - len(book[1])) * ' '}{book[1]} |'
                      f'{(25 - len(book[0])) * ' '}{book[0]} |'
                      f'{(10 - len(book[2])) * ' '}{book[2]} |')
                print(60 * '-')
    elif choice == 0:
        print('Вы покинули программу')
        break
    else: print('Вы сделали неправильный выбор! Выберите номер действия согласно меню.')


print('project Управление библиотекой')
# Проект 2: Анализ посещаемости на сайте
#
# Разработайте программу для анализа посещаемости на сайте. Программа должна позволять вводить количество посещений
# за каждый день недели, определять дни с наибольшей и наименьшей посещаемостью, рассчитывать среднюю посещаемость
# за неделю и выводить дни с посещаемостью выше среднего.
#
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
visits = []
while True:
    average_attendance = 0
    max_attendance = -1
    min_attendance = 10000000000
    print("\nМеню")
    print("1. Ввести количество посещений за каждый день недели")
    print("2. Определить дни с наибольшей посещаемостью")
    print("3. Определить дни с наименьшей посещаемостью")
    print("4. Рассчитать среднюю посещаемость за неделю")
    print("5. Выввести дни с посещаемостью выше среднего")
    print("6. Выввести таблицу посещений")
    print("0. Покинуть программу")
    choice = int(input("Выберите действие, введя его номер: "))
    if choice == 1:
        for id, day in enumerate(days, 1):
            attendance = int(input(f'Введите количество посещений в/во {day}: '))
            visits.append([day, attendance])
            print(34 * '-')
            print(f'| id |{2 * " "}день недели{2 * " "}| посещения |')
            print(34 * '-')
            print(f'|{(3 - len(str(id))) * ' '}{id} |'
                  f'{(14 - len(day)) * ' '}{day} |'
                  f'{(10 - len(str(attendance))) * ' '}{attendance} |')
            print(34 * '-')
    elif choice == 2:
        for day in visits:
            if max_attendance < day[1]:
                max_attendance = day[1]
                mindex = visits.index(day)

        print(f'Наибольшая посещаемость {max_attendance} была в {visits[mindex][0]}')
    elif choice == 3:
        for day in visits:
            if min_attendance > day[1]:
                min_attendance = day[1]
                mindex = visits.index(day)
        print(f'Наименьшая посещаемость {min_attendance} была в {visits[mindex][0]}')
    elif choice in [4, 5]:
        average_attendance = round(sum([day[1] for day in visits])/len(visits), 0)
        print(f'Средняя посещаемость за неделю составляет {average_attendance}')
        if choice == 5:
            visits_list = []
            print('Список дней с посещаемостью выше средней')
            print(29 * '-')
            print(f'|{2 * " "}день недели{2 * " "}| посещения |')
            print(29 * '-')
            for day in visits:
                if day[1] > average_attendance:
                    visits_list.append(day)
                    print(f'|{(14 - len(day[0])) * ' '}{day[0]} |'
                          f'{(10 - len(str(day[1]))) * ' '}{day[1]} |')
                    print(29 * '-')
    elif choice == 0:
        print('Вы покинули программу')
        break
    elif choice == 6:
        print(34 * '-')
        print(f'| id |{2 * " "}день недели{2 * " "}| посещения |')
        print(34 * '-')
        for id, day in enumerate(visits, 1):
            print(f'|{(3 - len(str(id))) * ' '}{id} |'
                  f'{(14 - len(day[0])) * ' '}{day[0]} |'
                  f'{(10 - len(str(day[1]))) * ' '}{day[1]} |')
            print(34 * '-')
    else:
        print('Вы сделали неправильный выбор! Выберите номер действия согласно меню.')

