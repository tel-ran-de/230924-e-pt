# методы строк
print('методы строк')
greeting_str = 'Hello, World!'
upper_str = greeting_str.upper()
lower_str = greeting_str.lower()
find_str = greeting_str.find('World')
ghost_str = greeting_str.find('Q')  # если буква не найдена, то вернётся -1
print(upper_str)
print(lower_str)
print(find_str)
print(ghost_str)

count_l_str = greeting_str.count('l')
print(count_l_str)
# по умолчанию .split() делит по пробелу
split_str = greeting_str.split()
print(split_str)
split_str_l = greeting_str.split('l')
print(split_str_l)

# replace
# - первый аргумент ЧТО меняем,
# - второй аргумент НА ЧТО меняем,
# - третий аргумент СКОЛЬКО РАЗ меняем
replaced_str = greeting_str.replace('World', 'Python')
print(replaced_str)
replaced_str2 = greeting_str.replace('l', 'q').replace('o', 'ö')
print(replaced_str2)
replaced_str3 = greeting_str.replace('l', 'L', 1)
print(replaced_str3)


# удалить ВСЕ пробелы из строки
s = '   Hello   Python   and   Good night   '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.replace(' ', ''))

