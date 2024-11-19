# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.




filename = 'data.txt'



with open(filename, 'r') as file:
    content = file.read()
    print("Весь контент файла:")
    print(content)
    print("\n")

with open(filename, 'r') as file:
    first_10_chars = file.read(10)
    print("10 символов файла:")
    print(first_10_chars)
    print("\n")

with open(filename, 'r') as file:
    first_line = file.readline()
    print("Первая строка файла:")
    print(first_line)
    print("\n")

with open(filename, 'r') as file:
    all_lines = file.readlines()
    print("Все строки файла:")
    for line in all_lines:
        print(line, end='')
    print("\n")






# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.






with open('output.txt', 'w') as file:


    file.write("Hello, World!\n"),


    file.writelines(["This is line 1\n", "This is line 2\n"]),



with open('output.txt', 'r') as file:
    content = file.read()
    print(content)






# Задание 3:





# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.






"1.Открытие файла"

with open('pointer_example.txt', 'w+') as file:

    "2. Запись строки"

    file.write("Python File Handling\n")



    "3. Перемещение"

    file.seek(0)
    first_line = file.readline()
    print(f"Первая строка: {first_line}")



    "4. Перемещение позиции"

    file.seek(7)
    five_chars = file.read(5)
    print(f"5 символов с 7: {five_chars}")



    "5. Перемещение в конец файла "

    file.seek(0, 2)  ("позиция 2 - конец")
    file.write("End of file\n")

    "6. Перемещение указателя в начало файла "

    file.seek(0)
    content = file.read()
    print(f":\n{content}")




# Тема: Менеджер контекста и JSON

# Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
# 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
# 3. Прочитайте данные из файла `user.json` и выведите их на экран.






import json


"1. Создаем словарь"

user_info = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}


"2. Записываем этот словарь"

with open('user.json', 'w') as file:
    json.dump(user_info, file)


"3. Читаем данные"

with open('user.json', 'r') as file:
    data = json.load(file)
    print("Данные из файла user.json:")
    print(data)





# Задача 2: Обновление данных в файле JSON
# 1. Прочитайте данные из файла `user.json`.
# 2. Обновите возраст пользователя на 29 лет.
# 3. Запишите обновленные данные обратно в файл JSON с использованием менеджера контекста.





import json


with open('user.json', 'r') as file:
    user_info = json.load(file)


user_info['age'] = 29


with open('user.json', 'w') as file:
    json






# Задача 3: Добавление нового пользователя в массив JSON
# 1. Прочитайте массив объектов из файла `users.json`
# (каждый объект содержит информацию о пользователе: имя, возраст, город).
# 2. Добавьте нового пользователя в массив.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.






import json


with open('users.json', 'r') as file:
    users = json.load(file)



new_user = {
    "name": "Alice Smith",
    "age": 28,
    "city": "Los Angeles"
}
users.append(new_user)



with open('users.json', 'w') as file:
    json.dump(users, file, indent=4)






# Задача 4: Удаление пользователя из массива JSON
# 1. Прочитайте массив объектов из файла `users.json`.
# 2. Удалите одного из пользователей.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.






import json



with open('users.json', 'r') as file:
    users = json.load(file)



user_to_remove = "John Doe"
users = [user for user in users if user['name'] != user_to_remove]




with open('users.json', 'w') as file:
    json.dump(users, file, indent=4),   "вывод"






# Тема: Интеграционная практика. Мини-проект

# Проект: Перепишите проект из уроков 7-8 с записью, чтением, обновлением и удалением товаров в файле (через JSON).
# Используйте файл как базу данных проекта.
#
# Управление инвентарем в интернет-магазине
# Разработайте программу для управления инвентарем интернет-магазина.
# Программа должна позволять добавлять новые товары и удалять имеющиеся,
# обновлять наименование, цену и количество существующих товаров,
# искать товары по названию, выводить список всех товаров и их количество,
# а также выводить товары с количеством ниже заданного значения стоимости и количества.
#
# Меню:
# 1. Показать список товаров.
# 2. Добавить товар.
# 3. Удалить товар.
# 4. Обновить название товара, стоимость или количество.
# 5. Найти товар по названию.
# 6. Вывести список товаров меньше определнной стоимости.
# 7. Вывести список товаров меньше определенного количества.

inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]




import json


def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [],   "возвращаем пустой список"

#  сохранения данных
def save_inventory(inventory):
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file, indent=4)



" 1.  список товаров"



def show_inventory(inventory):
    if inventory:
        print("Список товаров:")
        for item in inventory:
            print(f"Товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
    else:
        print("Инвентарь пуст.")



" 2. Добавить товар"



def add_product(inventory):
    product = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    count = int(input("Введите количество товара: "))
    inventory.append({'product': product, 'price': price, 'count': count})
    save_inventory(inventory)
    print(f"Товар {product} добавлен.")



" 3. Удалить товар"



def remove_product(inventory):
    product = input("Введите название товара для удаления: ")
    inventory = [item for item in inventory if item['product'] != product]
    save_inventory(inventory)
    print(f"Товар {product} удален.")
    return inventory



" 4. Обновить товар"



def update_product(inventory):
    product = input("Введите название товара для обновления: ")
    for item in inventory:
        if item['product'] == product:
            print(f"Обновление товара {product}.")
            new_name = input(f"Введите новое название (или оставьте пустым, чтобы не менять): ")
            if new_name:
                item['product'] = new_name
            new_price = input(f"Введите новую цену (или оставьте пустым, чтобы не менять): ")
            if new_price:
                item['price'] = float(new_price)
            new_count = input(f"Введите новое количество (или оставьте пустым, чтобы не менять): ")
            if new_count:
                item['count'] = int(new_count)
            save_inventory(inventory)
            print(f"Товар {product} обновлен.")
            return inventory
    print(f"Товар {product} не найден.")
    return inventory



" 5. Найти товар"



def find_product(inventory):
    product = input("Введите название товара : ")
    found = [item for item in inventory if item['product'].lower() == product.lower()]
    if found:
        for item in found:
            print(f"Товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
    else:
        print(f" с названием {product} не найден.")

" 6. Вывести товары"

def show_products_under_price(inventory):
    price = float(input(" максимальную цену: "))
    filtered = [item for item in inventory if item['price'] < price]
    if filtered:
        for item in filtered:
            print(f"Товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
    else:
        print(f" с ценой ниже {price} не найдены.")

" 7. Вывести товары"
def show_products_under_count(inventory):
    count = int(input("минимальное количество : "))
    filtered = [item for item in inventory if item['count'] < count]
    if filtered:
        for item in filtered:
            print(f"Товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
    else:
        print(f" меньше {count} не найдены.")


    "меню"


def main():
    inventory = load_inventory()

    while True:
        print("\nМеню:")
        print("1. Показать список товаров")
        print("2. Добавить товар")
        print("3. Удалить товар")
        print("4. Обновить товар")
        print("5. Найти товар по названию")
        print("6. Вывести товары с ценой меньше заданной")
        print("7. Вывести товары с количеством меньше заданного")
        print("8. Выход")

        choice = input(" действие (1-8): ")

        if choice == '1':
            show_inventory(inventory)
        elif choice == '2':
            add_product(inventory)
        elif choice == '3':
            inventory = remove_product(inventory)
        elif choice == '4':
            inventory = update_product(inventory)
        elif choice == '5':
            find_product(inventory)
        elif choice == '6':
            show_products_under_price(inventory)
        elif choice == '7':
            show_products_under_count(inventory)
        elif choice == '8':
            print("Выход")
            break
        else:
            print("снова.")

if __name__ == '__main__':
    main()




###########################################################################################
###########################################################################################
###########################################################################################