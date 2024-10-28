```python
# Упражнение 1: Поиск числа

num = 42  # Пример числа для угадывания

while True:
    guess = int(input("Введите число: "))
    if guess < num:
        print("Слишком маленькое число")
    elif guess > num:
        print("Вы ввели большее число")
    else:
        print("Вы угадали число")
        break

# Упражнение 2: Проверка пароля

correct_password = "python123"
attempts = 3

while attempts > 0:
    password = input("Введите пароль: ")
    if ' ' in password:
        print("Пароль не должен содержать пробелов")
    elif password == correct_password:
        print("Доступ разрешен")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Неправильный пароль. Осталось попыток: {attempts}")
        else:
            print("Превышено количество попыток")

# Упражнение 3: Работа со списком покупок

shopping_list = []

while True:
    item = input("Введите элемент для списка покупок (или 'стоп' для завершения): ")
    if item == "стоп":
        print("Формирование списка завершено")
        break
    elif len(shopping_list) >= 6:
        print("Превышен лимит покупок.")
        break
    elif item in shopping_list:
        print("Этот элемент уже в списке")
    else:
        shopping_list.append(item)

print("Итоговый список покупок:", shopping_list)
print("Общее количество элементов:", len(shopping_list))

# Упражнение 1: Подсчет гласных в строке

string = input("Введите строку: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Количество гласных букв:", count)

# Упражнение 2: Генерация и вывод последовательности чисел

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Проект 1: Управление библиотекой

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

    if choice == '1':
        for book in library:
            print(book)
    elif choice == '2':
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        status = input("Введите статус книги: ")
        library.append([title, author, status])
    elif choice == '3':
        title = input("Введите название книги для удаления: ")
        for book in library:
            if book[0] == title:
                library.remove(book)
                break
    elif choice == '4':
        title = input("Введите название книги для изменения статуса: ")
        new_status = input("Введите новый статус книги: ")
        for book in library:
            if book[0] == title:
                book[2] = new_status
                break
    elif choice == '5':
        author = input("Введите автора для поиска: ")
        for book in library:
            if book[1] == author:
                print(book)
    elif choice == '6':
        status = input("Введите статус для поиска: ")
        for book in library:
            if book[2] == status:
                print(book)
    else:
        print("Неверный выбор")

# Проект 2: Анализ посещаемости на сайте

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
visits = []

for day in days:
    visit = int(input(f"Введите количество посещений для {day}: "))
    visits.append(visit)

max_visits = max(visits)
min_visits = min(visits)
average_visits = sum(visits) / len(visits)

print(f"День с наибольшей посещаемостью: {days[visits.index(max_visits)]} ({max_visits} посещений)")
print(f"День с наименьшей посещаемостью: {days[visits.index(min_visits)]} ({min_visits} посещений)")
print(f"Средняя посещаемость за неделю: {average_visits:.2f}")

print("Дни с посещаемостью выше среднего:")
for i in range(len(visits)):
    if visits[i] > average_visits:
        print(f"{days[i]}: {visits[i]} посещений")
```