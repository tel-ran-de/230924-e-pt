# Тема: Упаковка аргументов с помощью *args, **kwargs и распакоgвка через * и **

# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.




def sum_all(*args):
    return sum(args)

result = sum_all(1, 2, 3, 4, 5)

print(result)  # Вывод:





# 2. Напишите функцию combine_lists, которая принимает несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.




def combine_lists(*args):
    combined_list = []
    for lst in args:
        combined_list.extend(lst)
    return combined_list

result = combine_lists([1, 2, 3], ['a', 'b'], [True, False])

print(result)  #  : [1, 2, 3, 'a', 'b', True, False]





# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age, распакуйте его и передайте в функцию print_details.



def print_details(name, age):
    print(f"Name: {name}, Age: {age}")

details = {'name': 'Alice', 'age': 30}

print_details(**details)






# 4. Напишите функцию filter_numbers, которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.




def filter_numbers(*args):
    return [num for num in args if num > 10]

result = filter_numbers(5, 12, 3, 20, 8, 15)

print(result),        # [12, 20, 15]







######################################################################################
# Тема: Глобальные и локальные переменные. Вложенные функции и замыкания.
######################################################################################






# 1. Напишите функцию increment_global, которая увеличивает значение глобальной переменной counter на 1 каждый раз,
# когда она вызывается.
# increment_global()
# print(counter)  # Вывод: 1
# increment_global()
# print(counter)  # Вывод: 2




"значение глобальной переменной"

counter = 0

def increment_global():
    global counter
    counter += 1,     ("увеличивает на 1")

increment_global()
print(counter),        # 1

increment_global()
print(counter),        # 2






# 2. Напишите функцию outer, которая содержит внутреннюю функцию inner. Внутренняя функция должна увеличивать
# значение переменной count, объявленной во внешней функции, на 1 каждый раз при её вызове.
# counter = outer()
# print(counter())  # Вывод: 1
# print(counter())  # Вывод: 2



def outer():
    count = 0,

    def inner():
        nonlocal count   # ("во внешней функции")
        count += 1
        return count

    return inner

"Создаём"

counter = outer()

"Пример"

print(counter()),  #  1
print(counter()),  #  2
print(counter()),  #  3







# 3. Напишите функцию make_multiplier, которая принимает аргумент factor. Внутри этой функции создайте и
# верните функцию multiplier, которая умножает свой аргумент на factor.
#
# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))  # Вывод: 10
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))  # Вывод: 15

# def make_multiplier(factor):
#     def multiplier(x):
#         return x * factor
#     return multiplier
#
# # Пример использования
# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))  # Вывод: 10
#
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))  # Вывод: 1




def make_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier

"Пример"

mult_by_2 = make_multiplier(2)
print(mult_by_2(5)),       # 10

mult_by_3 = make_multiplier(3)
print(mult_by_3(5)),       # 15




####################################################################################
# Тема: Дополнительная практика
####################################################################################




# 1. Напишите функцию create_user, которая принимает параметры username, email
# и произвольное количество дополнительных данных с помощью **kwargs.
# Функция должна возвращать словарь с информацией о пользователе.





def create_user(username, email, **kwargs):
    user_info = {
        "username": username,
        "email": email
    }

    user_info.update(kwargs)

    return user_info


"Пример"

user1 = create_user("Alice", "alice@example.com", age=30, city="New York")
user2 = create_user("Bob", "bob@example.com", profession="Developer")

print(user1)
# {'username': 'Alice', 'email': 'alice@example.com', 'age': 30, 'city': 'New York'}

print(user2)
# {'username': 'Bob', 'email': 'bob@example.com', 'profession': 'Developer'}







# 2. Напишите функцию make_replacer, которая принимает два аргумента old и new. Внутри этой функции создайте
# и верните функцию replacer, которая заменяет все вхождения old на new в переданной ей строке.
# replace_a_with_o = make_replacer("a", "o")
# print(replace_a_with_o("banana"))  # Вывод: bonono
# print(replace_a_with_o("apple"))   # Вывод: opple




def make_replacer(old, new):
    def replacer(text):
        return text.replace(old, new)

    return replacer

"Пример"

replace_a_with_o = make_replacer("a", "o")
print(replace_a_with_o("banana")),        # "bonono"
print(replace_a_with_o("apple")),         # "opple"







# 3. Напишите функцию make_suffixer, которая принимает строку suffix и возвращает внутреннюю функцию suffixer.
# Внутренняя функция должна добавлять suffix к любому переданному ей аргументу.
# add_exclamation = make_suffixer("!")
# print(add_exclamation("Hello"))  # Вывод: Hello!
# print(add_exclamation("Wow"))    # Вывод: Wow!




def make_suffixer(suffix):
    def suffixer(text):
        return text + suffix

    return suffixer


add_exclamation = make_suffixer("!")
print(add_exclamation("Hello")),        # "Hello!"
print(add_exclamation("Wow")),          # "Wow!"







# 4. Напишите функцию make_case_changer, которая принимает аргумент case (значения могут быть "upper" или "lower").
# Внутри этой функции создайте и верните функцию case_changer, которая изменяет регистр строки в зависимости от
# переданного аргумента (если передан аргумент с заглавными буквами, то делаете их строчными, если со строчными,
# то делает их заглавными).
# to_upper = make_case_changer("upper")
# print(to_upper("hello"))  # Вывод: HELLO
# to_lower = make_case_changer("lower")
# print(to_lower("WORLD"))  # Вывод: world




def make_case_changer(case):
    "меняет регистр"
    def case_changer(text):
        if case == "upper":
            return text.upper()
        elif case == "lower":
            return text.lower()
        else:
            raise ValueError("Invalid case type. Use 'upper' or 'lower'.")

    return case_changer

to_upper = make_case_changer("upper")
print(to_upper("hello")),                  # "HELLO"

to_lower = make_case_changer("lower")
print(to_lower("WORLD")),                  # "world"





################################################################################################
################################################################################################
################################################################################################