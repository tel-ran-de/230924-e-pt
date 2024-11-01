
from itertools import product

inventory = [
    {'product': "Mouse", 'price': 10, 'count': 13},
    {'product': "Laptop", 'price': 50, 'count': 1},
    {'product': "Monitor", 'price': 30, 'count': 33},
    {'product': "Keyboard", 'price': 20, 'count': 10}
]
while True:
    print("-----------------------------------------------------------------")
    print("\n М Е Н Ю :")
    print("-----------------------------------------------------------------")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить название товара, стоимость или количество.")
    print("5. Найти товар по названию.")
    print("6. Вывести список товаров меньше определенной стоимости.")
    print("7. Вывести список товаров меньше определенного количества.")
    print("0. Выход из программы.")
    print("-----------------------------------------------------------------")
    choice = input("Выберите действие: ")
    print("-----------------------------------------------------------------")
    if  choice == '1':
        print("Список товаров: ")
        print("-----------------------------------------------------------------")
        for item in inventory:
            print(f'| Наименование: |  {item["product"]} | Цена: {item["price"]} евро | Количество: {item["count"]} штук |')
    elif choice == '2':
        product = input("Введите наименование товара: ")
        price = int(input("Введите цену товара: "))
        count = int(input("Введите количество товара: "))
        inventory.append({"product": product, "price": price, "count": count})
        print(f"Товар {product} добавлен.")
    elif choice == '3':
        product = input("Введите наименование товара для удаления из списка: ")
        print("-----------------------------------------------------------------")
        for item in inventory:
            if item["product"].lower() == product.lower():
                inventory.remove(item)
                print(f"Товар {product} удален.")
                break
            else:
                print(f"Товар {product} не найден.")
                break
    elif choice == '4':
        product = input("Введите название товара для обновления: ")
        for item in inventory:
            if item['product'].lower() == product.lower():
                item['product'] = input("Введите новое название товара: ")
                item['price'] = int(input("Введите новую цену товара: "))
                item['count'] = int(input("Введите новое количество товара: "))
                print(f"Товар {product} изменен.")
                break
            else:
                print(f"Товар {product} не найден.")
                break
    elif choice == '5':
        product = input("Введите наименование товара: ")
        print("-----------------------------------------------------------------")
        for item in inventory:
            if item["product"].lower() == product.lower():
                print(f'| Наименование: |  {item["product"]} | Цена: {item["price"]} евро | Количество: {item["count"]} штук |')
                break
        else:
                print(f"Товар {product} не найден.")
    elif choice == '6':
        price = int(input("Введите максимальную цену товара: "))
        print("-----------------------------------------------------------------")
        print(f"Наименование товара с ценой ниже {price} евро: ")
        print("-----------------------------------------")
        for item in inventory:
            if item["price"] <= price:
                print(f'| Наименование: |  {item["product"]} | Цена: {item["price"]} евро | Количество: {item["count"]} штук |')
    elif choice == '7':
        count = int(input("Введите максимальное количество товара: "))
        print("-----------------------------------------------------------------")
        print(f"Наименование товара с количеством меньше {count} штук: ")
        print("-------------------------------------------------")
        for item in inventory:
            if item["count"] <= count:
                print(
                    f'| Наименование: |  {item["product"]} | Цена: {item["price"]} евро | Количество: {item["count"]} штук |')
    elif choice == '0':
        print("Выход из программы.")
        break
    else:
        print("Некорректный ввод. Выберите действие от 1 до 7 из меню.")