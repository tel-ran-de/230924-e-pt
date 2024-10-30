# Тема: Цикл while. Операторы break, continue, else.

# Упражнение 1: Поиск числа
#
# Напишите программу, которая запрашивает у пользователя числа, пока он не введет число совпадающее
# с переменной num (num = любое число от 0 до 100).  Если введенное число меньше num, программа должна
# выводить сообщение "Слишком маленькое число" и продолжать запрашивать числа. Если число больше num,
# программа должна вывести сообщение "Вы ввели большее число" и продолжать запрашивать числа.
# Если пользователь угадал, то программа должна вывести "Вы угадали число" и завершиться.
print("===============Тема: Цикл while.Упражнение 1: Поиск числа.================================")
random_num = 44
while True:
    user_num = int(input("Введите число от 0 до 100: "))
    if user_num > random_num:
        print("Вы ввели большее число")
    elif user_num < random_num:
        print("Слишком маленькое число")
    else:
        print("Вы угадали число")
        break

# Упражнение 2: Проверка пароля
#
# Напишите программу, которая будет запрашивать у пользователя пароль до тех пор, пока не будет введен
# правильный пароль "python123", либо пока не закончатся попытки. Если введенный пароль содержит пробелы,
# программа должна выводить сообщение "Пароль не должен содержать пробелов" и продолжать запрашивать пароль.
# Если введен правильный пароль, программа должна выводить сообщение "Доступ разрешен" и завершаться.
# Если после трех неправильных попыток пароль не введен правильно, программа должна выводить сообщение
# "Превышено количество попыток" и завершаться.
print("=================Упражнение 2: Проверка пароля.===================================")
password = "password12"
probe_num = 3
probe = 0
while True:
    user_pass = input('Введите пароль: ')
    probe += 1
    if ' ' in user_pass:
        print("Пароль не должен содержать пробелов")
    if user_pass == password:
        print("Доступ разрешен")
        break
    if probe == probe_num:
        print("Превышено количество попыток")
        break
    print(f"{probe_num - probe} попыток осталось")

# Упражнение 3: Работа со списком покупок
#
# Напишите программу, которая будет запрашивать у пользователя элементы для списка покупок до тех пор,
# пока не будет введено слово "стоп", либо пока количество покупок не станет больше 6. Если введенное
# слово уже есть в списке, программа должна выводить сообщение "Этот элемент уже в списке" и продолжать
# запрашивать новые элементы. Если введено слово "стоп", программа должна выводить сообщение
# "Формирование списка завершено" и завершаться. Если количество покупок ставится больше 6,
# то программа должна вывести: “Превышен лимит покупок.” и завершиться.
# Перед завершением программа должна выводить итоговый список покупок и общее количество элементов в нем.
print("=================Упражнение 3: Работа со списком покупок.================================")
kaufen_list = []
counter = 0
while True:
    if len(kaufen_list) > 0:
        print("Список покупок:")
        for index, item in enumerate(kaufen_list, 1):
            print(f"{index}. {item}")
    spisok = input("Внесите планируемую покупку в список: ")
    if spisok == "стоп":
        print("Формирование списка завершено")
        print("Список покупок:")
        for index, item in enumerate(kaufen_list, 1):
            print(f"{index}. {item}")
        break
    elif spisok in kaufen_list:
        print("Этот элемент уже в списке")
        continue
    if counter == 6:
        print("Превышен лимит покупок.")
        print("Список покупок:")
        for index, item in enumerate(kaufen_list, 1):
            print(f"{index}. {item}")
        break
    kaufen_list.append(spisok)
    counter += 1
print("============Тема: Цикл for.Упражнение 1: Подсчет гласных в строке.=======================")
# Тема: Цикл for

# Упражнение 1: Подсчет гласных в строке
#
# Напишите программу, которая принимает строку от пользователя и подсчитывать количество гласных букв (a, e, i, o, u)
# в этой строке.Используйте цикл for и условие if.

letter = ["a", "e", "i", "o", "u"]
count = 0
sent = input("Введите слово: ")
for char in sent:
   if char in letter:
       count+=1
print(f'в слове {sent} - {count} гласных')

# Упражнение 2: Генерация и вывод последовательности чисел
#
# Напишите программу, которая генерит и выводит последовательность чисел от 1 до 20,
# но выводит "Fizz" вместо чисел, кратных 3, "Buzz" вместо чисел, кратных 5, и "FizzBuzz"
# вместо чисел, кратных как 3, так и 5. Используйте цикл for и функцию range.
print("==============Упражнение 2: Генерация и вывод последовательности чисел.==================")

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


print("========================Проект 1: Управление библиотекой.===============================")
# Проект 1: Управление библиотекой
#
# Описание:
# Разработайте программу для управления библиотекой. Программа должна позволять добавлять книги в библиотеку,
# удалять книги, искать книги по автору и выводить список всех книг с их авторами и статусами (в наличии или выдана).
#
# Требования: Реализуйте работу всех пунктов меню.
#
# library = [["Война и мир", "Толстой", "в наличии"],
#            ["Преступление и наказание", "Достоевский", "выдана"],
#            ["Мастер и Маргарита", "Булгаков", "в наличии"]]
#
# while True:
#     print("\nМеню")
#     print("1. Показать список всех книг")
#     print("2. Добавить книгу")
#     print("3. Удалить книгу")
#     print("4. Поменять статус книги")
#     print("5. Показать книги определенного автора")
#     print("6. Показать книги с определенным статусом")
#     choice = input("Выберите действие, введя его номер: ")
#
#     # Продолжите программу ниже.
library = [["Война и мир", "Толстой", "в наличии"],
           ["Преступление и наказание", "Достоевский", "выдана"],
           ["Мастер и Маргарита", "Булгаков", "в наличии"]]
status_book = ("выдана", "в наличии")
while True:
    print("\n   М  Е  Н  Ю:")
    print("------------------------------------------------------------")
    print("1. Показать список всех книг")
    print("2. Добавить книгу")
    print("3. Удалить книгу")
    print("4. Поменять статус книги")
    print("5. Показать книги определенного автора")
    print("6. Показать книги с определенным статусом")
    print("7. Завершение работы")
    print("------------------------------------------------------------")
    while True:
        try:
            choice = int(input("Выберите действие, введя его номер: "))
            print("------------------------------------------------------------")
            break
        except:
            print("Некорректный ввод! Выберите номер от 1 до 7 из меню.")
            print("---------------------------------------------------------------")
    # choice = int(input("Выберите действие, введя его номер: "))
    if choice == 1:
        print("Список книг в библиотеке: ")
        print("------------------------------------------------------------")
        print(f'|  № |{5 * " "}Автор{4 * " "}|{6 * " "}Название книги{6 * " "}|   Статус  |')
        print("------------------------------------------------------------")
        for index, book in enumerate(library, 1):
            print(f'|{(3 - len(str(index))) * ' '}{index} |'
                  f'{(13 - len(book[1])) * ' '}{book[1]} |'
                  f'{(25 - len(book[0])) * ' '}{book[0]} |'
                  f'{(10 - len(book[2])) * ' '}{book[2]} |')
            print("------------------------------------------------------------")
    elif choice == 2:
        input_book = input("Введите название книги: ")
        input_author = input("Введите автора книги: ")
        library.append([input_book, input_author, 'в наличии'])
    elif choice == 3:
        out_book = input("Удалить книгу по названию: ")
        # out_author = input("Удалить книгу автора:")
        for index, book in enumerate(library):
             if book[0].lower() == out_book.lower():
                library.pop(index)
                print(f'Книга "{out_book}" удалена из библиотеки!')
                break
        else:
            print(f'Книга "{out_book}" отсутствует')
    elif choice == 4:
        name_book = input("Введите название книги: ")
        name_author = input('Введите автора книги для изменения статуса: ')
        for book in library:
            if book[0].lower() == name_book.lower() and book[1].lower() == name_author.lower():
                print(f'книга с названием {name_book} автор {name_author} имеет статус {book[2]}')
                change_status = int(input('Чтобы изменить статус книги введите 1, если нет введите 0: '))
                if change_status == 1:
                    for item in status_book:
                        if item != book[2]:
                            book[2] = item
                            print(f'Книга с названием: "{name_book}" '
                                  f'- автор {name_author}, имеет новый статус - {book[2]}')
                            break
                else:
                    print(f'Книга с названием: "{name_book}" '
                          f'автор "{name_author}", имеет статус - {book[2]}')
                break
        else:
            print(f'Книга с названием:"{name_book}" - автор "{name_author}", не найдена в библиотеке! Проверьте корректность ввода.')
    elif choice == 5:
        authors = []
        author = input("Введите автора книги: ")
        for book in library:
            if book[1].lower() == author.lower():
                authors.append(book)
        if len(authors) == 0:
            print('Книг заданного автора нет в библиотеке')
        else:
            print("Список книг в библиотеке: ")
            print("------------------------------------------------------------")
            print(f'|  № |{5 * " "}Автор{4 * " "}|{6 * " "}Название книги{6 * " "}|   Статус  |')
            print("------------------------------------------------------------")
            for index, book in enumerate(authors, 1):
                print(f'|{(3 - len(str(index))) * ' '}{index} |'
                      f'{(13 - len(book[1])) * ' '}{book[1]} |'
                      f'{(25 - len(book[0])) * ' '}{book[0]} |'
                      f'{(10 - len(book[2])) * ' '}{book[2]} |')
                print("------------------------------------------------------------")
    elif choice == 6:
        # status_list = []
        while True:
            # index = int(input(f'Список книг со статусом "выдана" введите 0, "в наличии" введите 1: '))
            # print("---------------------------------------------------------------------------------")
            while True:
                try:
                    index = int(input(f'Список книг со статусом "выдана" введите 0, "в наличии" введите 1: '))
                    print("-----------------------------------------------")
                    break
                except:
                    print("Некорректный ввод. Введите 0 или 1.")
                    print("--------------------------------------------------")
            if index == 0:
                status_list = []
                for book in library:
                    if book[2] == status_book[index]:
                        status_list.append(book)
                print(f"Список книг со статусом - {status_book[index]}: ")
                print("------------------------------------------------------------")
                print(f'|  № |{5 * " "}Автор{4 * " "}|{6 * " "}Название книги{6 * " "}|   Статус  |')
                print("------------------------------------------------------------")
                for index, book in enumerate(status_list, 1):
                    print(f'|{(3 - len(str(index))) * ' '}{index} |'
                            f'{(13 - len(book[1])) * ' '}{book[1]} |'
                            f'{(25 - len(book[0])) * ' '}{book[0]} |'
                            f'{(10 - len(book[2])) * ' '}{book[2]} |')
                    print("------------------------------------------------------------")
                break
            elif index == 1:
                status_list = []
                for book in library:
                    if book[2] == status_book[index]:
                        status_list.append(book)
                print(f"Список книг со статусом - {status_book[index]}: ")
                print("------------------------------------------------------------")
                print(f'|  № |{5 * " "}Автор{4 * " "}|{6 * " "}Название книги{6 * " "}|   Статус  |')
                print("------------------------------------------------------------")
                for index, book in enumerate(status_list, 1):
                    print(f'|{(3 - len(str(index))) * ' '}{index} |'
                            f'{(13 - len(book[1])) * ' '}{book[1]} |'
                            f'{(25 - len(book[0])) * ' '}{book[0]} |'
                            f'{(10 - len(book[2])) * ' '}{book[2]} |')
                    print("------------------------------------------------------------")
                break
            else:
                print("Некорректный ввод. Введите 0 или 1.")
                while True:
                    try:
                        index = int(input(f'Список книг со статусом "выдана" введите 0, "в наличии" введите 1: '))
                        print("-----------------------------------------------")
                        break
                    except:
                        print("Некорректный ввод. Введите 0 или 1.")
                        print("--------------------------------------------------")

    elif choice == 7:
        print("Завершили работу с библиотекой")
        break
    else:
        print("Некорректный ввод. Выберите номер от 1 до 7 из меню.")


# Проект 2: Анализ посещаемости на сайте
#
# Разработайте программу для анализа посещаемости на сайте. Программа должна позволять вводить количество посещений
# за каждый день недели, определять дни с наибольшей и наименьшей посещаемостью, рассчитывать среднюю посещаемость
# за неделю и выводить дни с посещаемостью выше среднего.
#
# days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# visits = []