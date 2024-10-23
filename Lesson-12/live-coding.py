# Тема: Словари
#
# Продемонстрируйте в режиме live-coding и объясните:
# - Создание словарей
# - Примеры их использования
# - Основные методы словарей
# - Генератор словарей
print('Создание словарей')
print()
print('# Способ 1: Фигурные скобки')
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'London',
}
print(person)
print(person['name'])

print()
print('# Способ 2: функция dict()')
person = dict(name='Alice', age=30)
print(person)
print(person['name'])
person['city'] = 'Athens'
print(person)

print()
print('# Методы словарей')
print('# Доступ к значениям словаря с методом .get()')
print(person['city'])  # Athens
# print(person['lastname'])  # KeyError: 'lastname'
print(person.get('city'))  # Athens
print(person.get('lastname'))  # None
print(person.get('salary', 0))  # 0

print()
print('# .clear() очищает словарь')
person.clear()
print(person)  # {}

print('# .fromkeys() создаёт словарь из коллекции ключей')
countries = ['Poland', 'Spain', 'UK', 'Italy']
countries_none = dict.fromkeys(countries, None)
print(countries_none)  # {'Poland': None, 'Spain': None, 'UK': None, 'Italy': None}

print('# .copy() создаёт словарь из коллекции ключей')
countries_none_copy = countries_none.copy()
print(id(countries_none))  # 2091293584832
print(id(countries_none_copy))  # 2091293506240

print('# .setdefault() создаёт значение по умолчанию, если такой ключ не найден')
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'London',
}
print(person.get('address', 'Not found'))  # Not found
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'London'}
person.setdefault('address', 'Not found')
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'London', 'address': 'Not found'}

print('# .pop() - удаляет значение по ключу и ВОЗВРАЩАЕТ его')
alice_address = person.pop('address')
print(alice_address)  # Not found
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'London'}

print('# .popitem() - удаляет последнее добавленное значение по ключу и ВОЗВРАЩАЕТ ПАРУ ключ-значение')
alice_city = person.popitem()
print(alice_city)  # ('city', 'London')
print(person)  # {'name': 'Alice', 'age': 30}

print('# len() - длина словаря, считает ключей в словаре')
person_len = len(person)
print(person_len)  # 2

print('# in - проверяет есть ли такой ключ (НЕ ЗНАЧЕНИЕ) в словаре')
print('name' in person)  # True
print('age' in person)  # True
print('Alice' in person)  # False
print(30 in person)  # False

print()
print('# перебор элементов словаря')
capitals = {
    'Spain': 'Madrid',
    'Portugal': 'Lisbon',
    'Poland': 'Warsaw',
    'UK': 'London',
}
print('только ключи')
for key in capitals:
    print(key)
# Spain
# Portugal
# Poland
# UK

print()
print('ключи и значения')
for key in capitals:
    print(key, capitals[key])
# Spain Madrid
# Portugal Lisbon
# Poland Warsaw
# UK London

print('# .items() - возвращает ПАРЫ ключ-значения')
print(capitals.items())  # dict_items([('Spain', 'Madrid'), ('Portugal', 'Lisbon'), ('Poland', 'Warsaw'), ('UK', 'London')])
# for item in capitals.items():
#     country = item[0]
#     capital = item[1]
#     print(country, capital)
for country, capital in capitals.items():
    print(country, capital)
# Spain Madrid
# Portugal Lisbon
# Poland Warsaw
# UK London
print('# .keys() - возвращает список ключей словаря')
print(capitals.keys())  # dict_keys(['Spain', 'Portugal', 'Poland', 'UK'])
print('# .values() - возвращает список значений словаря')
print(capitals.values())  # dict_values(['Madrid', 'Lisbon', 'Warsaw', 'London'])

print()
print('# генераторы словарей')
colors_en = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']  # keys
colors_ru = ['Красный', 'Синий', 'Зелёный', 'Жёлтый', 'Фиолетовый']  # values
colors_matching = {colors_en[i]: colors_ru[i] for i in range(len(colors_en))}
# создаётся арифметическая прогрессия от 0 до 4 с помощью range(5)
# на каждой итерации, i принимает значение 0, 1, 2, 3, 4
# на каждой итерации мы обращаемся к двум элементам каждого списка
# первая итерация i = 0, colors_en[i] -> Red; colors_ru[i] -> Красный; создаётся пара ключ: значение в словаре
# вторая итерация i = 1 ...
# третья итерация i = 2 ...
# четвёртая итерация i = 3 ...
# последняя итерация i = 4, colors_en[i] -> Purple; colors_ru[i] -> Фиолетовый; создаётся пара ключ: значение в словаре
print(colors_matching)  # {'Red': 'Красный', 'Blue': 'Синий', 'Green': 'Зелёный', 'Yellow': 'Жёлтый', 'Purple': 'Фиолетовый'}

# Тема: Кортежи и множества
#
# Продемонстрируйте в режиме live-coding и объясните:
# - Создание кортежей и множеств
# - Примеры их использования
# - Основные методы кортежей и множеств
# - Генератор множеств
