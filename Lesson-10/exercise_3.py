# Проект: Управление библиотекой
#
# Описание:
# Разработайте программу для управления библиотекой. Программа должна позволять добавлять книги в библиотеку,
# удалять книги, искать книги по автору и выводить список всех книг с их авторами и статусами (в наличии или выдана).
#
# Требования: Реализуйте работу всех пунктов меню.


library = [["Война и мир", "Толстой", "в наличии"],
           ["Преступление и наказание", "Достоевский", "выдана"],
           ["Мастер и Маргарита", "Булгаков", "в наличии"]]

def zeig_book():
    print("\nОбщий список книг")
    for book in library:
        print(f"Название: {book[0]}, Автор: {book[1]}, Статус: {book[2]}")
def add_book():
    title = input("Введите название книги: ")
    avtor = input("Введите автора")
    status = input("введите статус 'выдана / в наличии': ")
    library.append([title, avtor, status])
    print(f"Книга {title} добавлена")
def del_book():
    title = input("Введите название книги для удаления: ")
    for book in library:
        if book[0] == title:
            library.remove(book)
            print(f"Книга {title} удалена")
            return
    print("Книга не найдена")
def change_status():
    title = input("Введите название книги для изменения статуса: ")
    for book in library:
        if book[0] == title:
            new_status = input("Введите новый статус книги (в наличии/выдана): ")
            book[2] = new_status
            print(f"Статус книги '{title}' изменен на '{new_status}'.")
            return
    print("Книга не найдена.")
def such_book_avtor():
    avtor = input("Введите автора: ")
    print(f"\nКниги автора '{avtor}'")
    found = False
    for book in library:
        if book[1] == avtor:
            print(f"Название: {book[0]}, Статус: {book[2]}")
            found = True
    if not found:
        print("Не найдено")
def zeig_book_status():
    status = input("Введите статус книги в 'наличии' / 'выдана': ")
    print(f"\nКниги в статусе '{status}'")
    found = False
    for book in library:
        if book[2] == status:
            print(f"\nНазвание: {book[0]}, Автор: {book[1]}")
            found = True
    if not found:
        print("Не найдено")

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
        zeig_book()
    elif choice == "2":
        add_book()
    elif choice == "3":
        del_book()
    elif choice == "4":
        change_status()
    elif choice == "5":
        such_book_avtor()
    elif choice == "6":
        zeig_book_status()
    elif choice == "0":
        print("Выход из программы")
        break
    else:
        print("Что-то пошло не так, попробуйте ещё раз")