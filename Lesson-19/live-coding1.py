# Продемонстрируйте в режиме live-coding и объясните:
# - работу функции open в различных режимах;
# - чтение и запись данных в файл;
# - работу указателей.


# read
print('# read')
file = open('text_files/example.txt', 'r')
content = file.read(5)
print(content)  # Hello
content = file.read(5)
print(content)  # , Wor

print(file.tell())  # 10
file.seek(0)
print(file.tell())  # 0
content = file.read(5)
print(content)  # Hello
file.close()

# readline
print()
print('# readline')
file = open('text_files/data.txt', 'r')
content = file.readline()
print(content)  # Hello, World!
print(file.tell())  # 15
content = file.readline()
print(content)  # This is a sample file.
print(file.tell())  # 39
file.close()

# readlines
print()
print('# readlines')
file = open('text_files/data.txt', 'r')
content = file.readlines()
print(content)  # ['Hello, World!\n', 'This is a sample file.\n', 'It contains multiple lines of text.\n', 'Each line is separated by a newline character.\n']
print(file.tell())  # 124
file.close()

# write в режиме 'w' очищает содержимое файла
print()
print("# write в режиме 'w' очищает содержимое файла")
file = open('text_files/example.txt', 'w')
file.write('Hello, World!\n')
file.close()

# write в режиме 'a' не очищает содержимое файла
print()
print("# write в режиме 'a' не очищает содержимое файла")
file = open('text_files/example.txt', 'a')
file.write('Welcome to file handling in Python.')
file.close()

# writelines
print()
print("# writelines")
file = open('text_files/writelines.txt', 'w')
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
file.writelines(lines)
# переместим курсор в начало файла
file.seek(0)
lines = ['Line -2\n', 'Line -1\n', 'Line 0\n']
file.writelines(lines)
file.close()

# перемещение курсора в конец файла
# file.seek(0, 2)












# Продемонстрируйте в режиме live-coding и объясните:
# - работу менеджера контекста;
# - чтение и запись данных в json-формате.
