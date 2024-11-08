# Упражнение 1: Поиск числа
#
# Напишите программу, которая запрашивает у пользователя числа, пока он не введет число совпадающее
# с переменной num (num = любое число от 0 до 100).  Если введенное число меньше num, программа должна
# выводить сообщение "Слишком маленькое число" и продолжать запрашивать числа. Если число больше num,
# программа должна вывести сообщение "Вы ввели большее число" и продолжать запрашивать числа.
# Если пользователь угадал, то программа должна вывести "Вы угадали число" и завершиться.


num=43
while True:
    numb = int(input("ВВедите число:"))
    if numb < num:
        print("Слишком маленькое число")
    elif numb > num :
        print("Вы ввели большее число")
    else:
        print("Вы угадали число")
        break

print()
print("Упражнение 2: Проверка пароля")
print()

# Упражнение 2: Проверка пароля
#
# Напишите программу, которая будет запрашивать у пользователя пароль до тех пор, пока не будет введен
# правильный пароль "python123", либо пока не закончатся попытки. Если введенный пароль содержит пробелы,
# программа должна выводить сообщение "Пароль не должен содержать пробелов" и продолжать запрашивать пароль.
# Если введен правильный пароль, программа должна выводить сообщение "Доступ разрешен" и завершаться.
# Если после трех неправильных попыток пароль не введен правильно, программа должна выводить сообщение
# "Превышено количество попыток" и завершаться.

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

print()
print("Упражнение 3: Работа со списком покупок")
print()


password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
   passcode = input("Введите пароль: ")

   if " " in passcode:
        print("Пароль не должен содержать пробелов")
        continue

   if passcode == password:
        print("Доступ разрешен")
        break
   else:
       attempts += 1
if attempts == max_attempts:
         print("Превышено количество попыток")



# Упражнение 3: Работа со списком покупок
#
# Напишите программу, которая будет запрашивать у пользователя элементы для списка покупок до тех пор,
# пока не будет введено слово "стоп", либо пока количество покупок не станет больше 6. Если введенное
# слово уже есть в списке, программа должна выводить сообщение "Этот элемент уже в списке" и продолжать
# запрашивать новые элементы. Если введено слово "стоп", программа должна выводить сообщение
# "Формирование списка завершено" и завершаться. Если количество покупок ставится больше 6,
# то программа должна вывести: “Превышен лимит покупок.” и завершиться.
# Перед завершением программа должна выводить итоговый список покупок и общее количество элементов в нем.


shopping_list = []
max_produkt = 6

while len(shopping_list) < max_produkt:
    product = input("Введите элемент для списка покупок: ")
    if product.lower() == "стоп":
        print('Формирование списка завершено')
        break
    if product in shopping_list:
            print("Этот элемент уже в списке")
            continue
    shopping_list.append(product)
    print()

if len(shopping_list) >= max_produkt:
        print("Превышен лимит покупок.")
print("Итоговый список покупок:", shopping_list)
print("Общее количество элементов в списке:", len(shopping_list))
#



# Тема: Цикл for

# Упражнение 1: Подсчет гласных в строке
#
# Напишите программу, которая принимает строку от пользователя и подсчитывать количество гласных букв (a, e, i, o, u)
# в этой строке.Используйте цикл for и условие if.

word=input('Введите слово:')
gls =0
for letter in word:
        if letter in "aeiou":
          gls +=1
print(gls)
print()
print("Упражнение 3: Работа со списком покупок")
print()

vowels = "aeiou"
user_input = input("Введите строку: ")
vowel_count = 0
for char in user_input.lower():
    if char in vowels:
        vowel_count += 1

print(f"Количество гласных букв в строке: {vowel_count}")



# Упражнение 2: Генерация и вывод последовательности чисел
#
# Напишите программу, которая генерит и выводит последовательность чисел от 1 до 20,
# но выводит "Fizz" вместо чисел, кратных 3, "Buzz" вместо чисел, кратных 5, и "FizzBuzz"
# вместо чисел, кратных как 3, так и 5. Используйте цикл for и функцию range.

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print()
print("Генерация и вывод последовательности чисел")
print()


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

while True:
    print("\nМеню")
    print("1. Показать список всех книг")
    print("2. Добавить книгу")
    print("3. Удалить книгу")
    print("4. Поменять статус книги")
    print("5. Показать книги определенного автора")
    print("6. Показать книги с определенным статусом")
    choice = input("Выберите действие, введя его номер: ")

    # Продолжите программу ниже.
    if choice == "1":
        print("\nСписок всех книг:")
        for book in library:
            print(f"{book[0]} - {book[1]} ({book[2]})")

    elif choice == "2":
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        status = input("Введите статус книги (в наличии/выдана): ")
        library.append([title, author, status])
        print(f"Книга '{title}' добавлена.")

    elif choice == "3":
        title = input("Введите название книги, которую хотите удалить: ")
        found = False
        for book in library:
            if book[0].lower() == title.lower():
                library.remove(book)
                found = True
                print(f"Книга '{title}' удалена.")
                break
        if not found:
            print(f"Книга '{title}' не найдена.")

    elif choice == "4":
        title = input("Введите название книги, статус которой хотите поменять: ")
        found = False
        for book in library:
            if book[0].lower() == title.lower():
                new_status = input(f"Введите новый статус для книги '{title}' (в наличии/выдана): ")
                book[2] = new_status
                found = True
                print(f"Статус книги '{title}' изменен на '{new_status}'.")
                break
        if not found:
            print(f"Книга '{title}' не найдена.")

    elif choice == "5":
        author = input("Введите автора: ")
        print(f"\nКниги автора {author}:")
        found = False
        for book in library:
            if book[1].lower() == author.lower():
                print(f"{book[0]} ({book[2]})")
                found = True
        if not found:
            print(f"Книги автора {author} не найдены.")

    elif choice == "6":
        status = input("Введите статус (в наличии/выдана): ")
        print(f"\nКниги со статусом '{status}':")
        found = False
        for book in library:
            if book[2].lower() == status.lower():
                print(f"{book[0]} - {book[1]}")
                found = True
        if not found:
            print(f"Книги со статусом '{status}' не найдены.")

    elif choice == "7":
        print("Программа завершена.")
        break

    else:
        print("Некорректный выбор. Пожалуйста, выберите пункт из меню.")

print()
print("Управление библиотекой")
print()


#library = [
#    ["Война и мир", "Толстой", "в наличии"],
#            ["Преступление и наказание", "Достоевский", "выдана"],
#            ["Мастер и Маргарита", "Булгаков", "в наличии"]
#]
#
#def show_books():
#    for book in library:
#        print(f"название: {book[0]}, автор: {book[1]}, статус: {book[2]}")
#def add_book():
#    title = input("Введите название книги: ")
#    author = input("Введите автора книги: ")
#    status = input("Введите статус книги (в наличии/ выдана): ")
#    library.append([title, author, status])
#    print(f"Книга ´{title}` добавлена в библиотеку.")
#
#def remove_book():
#    title =input("Введите название книги для удаления: ")
#    for book in library:
#        if book[0].lower() == title.lower():
#            library.remove(book)
#            print(f"Книга `{title}` удалена из библиотеки.")
#
#def change_status():
#    title = input("Введите название книги для изменения статуса: ")
#    for book in library:
#        if book[0].lower() == title.lower():
#            new_status = input("Введите новый статус книги (в наличии/ выдана): ")
#            book[2] = new_status
#            print(f"Статус книги `{title}` изменен на `{new_status}`. ")
#            return
#        print(f"Книга `{title}` не найдена в библиотеке.")
#def search_by_author():
#    author = input("Введите автора для поиска книги: ")
#    found = False
#    for book in library:
#        if book[1].lower() == author.lower():
#            print(f"Название: {book[0]}, Автор: {book[1]}, Статус: {book[2]}")
#            found = True
#            if not found:
#                print(f"Книги автора `{author}` не найдена в библиотеке.")
#
#def search_by_status():
#    status = input("Введите статус книги для поиска (в наличии/ выдана): ")
#    found = False
#    for book in library:
#        if book[2].lower() == status.lower():
#            print(f"Название: {book[0]}, Автор: {book[1]}, Статус: {book[2]}")
#            found = True
#            if not  found:
#                print(f"Книги со статусом `{status}` не найдены.")
#
#while True:
#     print("\nМеню")
#     print("1. Показать список всех книг")
#    print("2. Добавить книгу")
#     print("3. Удалить книгу")
#     print("4. Поменять статус книги")
#     print("5. Показать книги определенного автора")
#     print("6. Показать книги с определенным статусом")
#     choice = input("Выберите действие, введя его номер: ")
#
#     if choice == "1":
#         show_books()
#     elif choice == "2":
#         add_book()
#     elif choice == "3":
#         remove_book()
#     elif choice == "4":
#         change_status()
#     elif choice == "5":
#        search_by_author()
#     elif choice == "6":
#         search_by_status()
#     elif choice == "7":
#         print("Выход из программы.")
#         break
#     else:
#         print("Неверный выбор. Выберите действие из имеющегося списка от 1 до 7.")



# Проект 2: Анализ посещаемости на сайте
#
# Разработайте программу для анализа посещаемости на сайте. Программа должна позволять вводить количество посещений
# за каждый день недели, определять дни с наибольшей и наименьшей посещаемостью, рассчитывать среднюю посещаемость
# за неделю и выводить дни с посещаемостью выше среднего.
#
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
visits = []

for day in days:
    visit_count = int(input(f"Введите количество посещений за {day}: "))
    visits.append(visit_count)

max_visits = max(visits)
min_visits = min(visits)

max_day = days[visits.index(max_visits)]
min_day = days[visits.index(min_visits)]

print(f"\nДень с наибольшей посещаемостью: {max_day} ({max_visits} посещений)")
print(f"День с наименьшей посещаемостью: {min_day} ({min_visits} посещений)")

average_visits = sum(visits) / len(visits)
print(f"\nСредняя посещаемость за неделю: {average_visits:.2f}")

print("\nДни с посещаемостью выше среднего:")
for i in range(len(visits)):
    if visits[i] > average_visits:
        print(f"{days[i]}: {visits[i]} посещений")


print()
print("Анализ посещаемости на сайте")
print()

max_visits = max(visits)
min_visits = min(visits)
max_day = days[visits.index(max_visits)]
min_day = days[visits.index(min_visits)]

average_visits = sum(visits) / len(visits)

above_average_days = [days[i] for i in range(len(visits)) if visits[i] > average_visits]

print("\nРезультаты анализа посещаемости:")
print(f"День с наибольшей посещаемостью: {max_day} ({max_visits} посещений)")
print(f"День с наименьшей посещаемостью: {min_day} ({min_visits} посещений)")
print(f"Средняя посещаемость за неделю: {average_visits:.2f}")
print("Дни с посещаемостью выше среднего:", ", ".join(above_average_days))

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
visits = []

