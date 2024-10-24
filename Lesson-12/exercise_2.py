# Задача 1: Обработка данных о координатах
# У вас есть список координат, каждая из которых представлена кортежем (x, y).
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите все координаты.
# 2. Найдите сумму всех координат по оси x и по оси y.
# 3. Добавьте новую координату (70, 80).
# 4. Замените первую координату на (15, 25).
# 5. Выведите все координаты, отсортированные по оси x.
#
coordinates = [(10, 20), (30, 40), (50, 60)]

for coord in coordinates:
    print(coord)

sum_x = sum(x for x, y in coordinates)
sum_y = sum(y for x, y in coordinates)
print(f"\nСумма координат по оси x: {sum_x}")
print(f"Сумма координат по оси y: {sum_y}")

coordinates.append((70, 80))

coordinates[0] = (15, 25)

sorted_coordinates = sorted(coordinates, key=lambda coord: coord[0])
print("\nКоординаты, отсортированные по оси x:")
for coord in sorted_coordinates:
    print(coord)


# Задача 2: Обработка данных о продуктах
# У вас есть список продуктов, каждый из которых представлен кортежем (название, цена).
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите все продукты.
# 2. Найдите суммарную стоимость всех продуктов.
# 3. Добавьте новый продукт "Date" с ценой 4.
# 4. Замените цену "Apple" на 2.5.
# 5. Выведите все продукты, отсортированные по цене.
#
products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]

for product in products:
    print(product)

total_cost = sum(price for name, price in products)
print(f"\nСуммарная стоимость всех продуктов: {total_cost}")

products.append(("Date", 4))

products = [(name, 2.5) if name == "Apple" else (name, price) for name, price in products]

sorted_products = sorted(products, key=lambda product: product[1])
print("\nПродукты, отсортированные по цене:")
for product in sorted_products:
    print(product)


# Задача 3: Управление группами пользователей
# У вас есть множество пользователей, и вам необходимо выполнить различные операции с этими данными.
#
# Задание:
# 1. Выведите всех пользователей.
# 2. Добавьте нового пользователя "David".
# 3. Удалите пользователя "Bob".
# 4. Проверьте, есть ли пользователь "Alice" в множестве.
# 5. Выведите количество пользователей.
#
users = {"Alice", "Bob", "Charlie"}

for user in users:
    print(user)

users.add("David")

users.remove("Bob")

if "Alice" in users:
    print("\nПользователь 'Alice' есть в множестве.")

print(f"\nКоличество пользователей: {len(users)}")

# Задача 4: Управление наборами данных
# У вас есть два множества, представляющих различные наборы данных.
# Необходимо провести различные операции с этими множествами.
#
# Задание:
# 1. Выведите элементы обоих множеств.
# 2. Найдите объединение двух множеств.
# 3. Найдите пересечение двух множеств.
# 4. Найдите разность множеств `set1` и `set2`.
# 5. Проверьте, является ли `set2` подмножеством `set1`.
#
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Множество 1:", set1)
print("Множество 2:", set2)

union = set1.union(set2)
print("\nОбъединение множеств:", union)

intersection = set1.intersection(set2)
print("Пересечение множеств:", intersection)

difference = set1.difference(set2)
print("Разность множеств (set1 - set2):", difference)

is_subset = set2.issubset(set1)
print(f"\nЯвляется ли set2 подмножеством set1: {is_subset}")
