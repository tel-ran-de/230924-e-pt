```python
# 1. Объедините строки "Hello" и "London" без пробела. Ожидаемый результат: "HelloLondon"
result = "Hello" + "London"
print(result)  # Вывод: HelloLondon

# 2. Выведите последний символ строки "Programming". Ожидаемый результат: "g"
result = "Programming"[-1]
print(result)  # Вывод: g

# 3. Дублируйте строку "Hi" три раза. Ожидаемый результат: "HiHiHi"
result = "Hi" * 3
print(result)  # Вывод: HiHiHi

# 4. Определите длину строки "Artificial Intelligence".
result = len("Artificial Intelligence")
print(result)  # Вывод: 23

# 5. Объедините строки "Good" и "Morning" с запятой между ними. Ожидаемый результат: "Good,Morning"
result = "Good" + "," + "Morning"
print(result)  # Вывод: Good,Morning

# 6. Создайте срез строки "Natural Language Processing" со значением "nguag".
result = "Natural Language Processing"[9:14]
print(result)  # Вывод: nguag

# 7. Объедините строки "Data" и "Science" с дефисом между ними. Ожидаемый результат: "Data-Science"
result = "Data" + "-" + "Science"
print(result)  # Вывод: Data-Science

# 8. Объедините строки "AI" и "ML" с двоеточием между ними. Ожидаемый результат: "AI:ML"
result = "AI" + ":" + "ML"
print(result)  # Вывод: AI:ML

# 9. Дублируйте строку "Test" шесть раз. Ожидаемый результат: "TestTestTestTestTestTest"
result = "Test" * 6
print(result)  # Вывод: TestTestTestTestTestTest

# 10. Выведите первый символ строки "Python". Ожидаемый результат: "P"
result = "Python"[0]
print(result)  # Вывод: P

# 11. Создайте срез строки "Hello, Anna!" от 0 до 5. Ожидаемый результат: "Hello"
result = "Hello, Anna!"[0:5]
print(result)  # Вывод: Hello

# 12. Определите длину строки "Natural Language Processing".
result = len("Natural Language Processing")
print(result)  # Вывод: 27

# 13. Выведите второй символ строки "Лето". Ожидаемый результат: "е"
result = "Лето"[1]
print(result)  # Вывод: е

# 14. Выведите предпоследний символ строки "Machine Learning". Ожидаемый результат: "n"
result = "Machine Learning"[-2]
print(result)  # Вывод: n

# 15. Дублируйте строку "Yes" четыре раза. Ожидаемый результат: "YesYesYesYes"
result = "Yes" * 4
print(result)  # Вывод: YesYesYesYes

# 16. Создайте срез строки "Deep Learning" со значением "ep Le".
result = "Deep Learning"[1:7]
print(result)  # Вывод: ep Le

# 17. Выведите третий символ строки "Computer Vision". Ожидаемый результат: "m"
result = "Computer Vision"[2]
print(result)  # Вывод: m

# 18. Определите длину строки "Deep Learning". Ожидаемый результат: 13
result = len("Deep Learning")
print(result)  # Вывод: 13

# 19. Объедините строки "Python" и "Rocks" с пробелом между ними. Ожидаемый результат: "Python Rocks"
result = "Python" + " " + "Rocks"
print(result)  # Вывод: Python Rocks

# 20. Создайте срез строки "Data Science" со значением "cien".
result = "Data Science"[5:9]
print(result)  # Вывод: cien

# Основные методы строк

# 1. Преобразуйте строку "hOw aRe yOu?" в верхний регистр.
# Ожидаемый результат: "HOW ARE YOU?"
result = "hOw aRe yOu?".upper()
print(result)  # Вывод: HOW ARE YOU?

# 2. Посчитайте количество символов "a" в строке "Bananas are amazing!".
result = "Bananas are amazing!".count("a")
print(result)  # Вывод: 5

# 3. Преобразуйте строку "PYTHON PROGRAMMING" в нижний регистр.
# Ожидаемый результат: "python programming"
result = "PYTHON PROGRAMMING".lower()
print(result)  # Вывод: python programming

# 4. Удалите начальные пробелы из строки "   Discover new worlds   ".
# Ожидаемый результат: "Discover new worlds   "
result = "   Discover new worlds   ".lstrip()
print(result)  # Вывод: Discover new worlds

# 5. Замените "rainy" на "sunny" в строке "It was a rainy day.".
# Ожидаемый результат: "It was a sunny day."
result = "It was a rainy day.".replace("rainy", "sunny")
print(result)  # Вывод: It was a sunny day.

# 6. Найдите индекс подстроки "innovation" в строке "Innovation drives progress.".
result = "Innovation drives progress.".find("innovation")
print(result)  # Вывод: 0

# 7. Удалите конечные пробелы из строки "   Explore the universe   ".
# Ожидаемый результат: "   Explore the universe"
result = "   Explore the universe   ".rstrip()
print(result)  # Вывод:    Explore the universe

# 8. Найдите индекс подстроки "galaxy" в строке "The Milky Way galaxy is vast.".
result = "The Milky Way galaxy is vast.".find("galaxy")
print(result)  # Вывод: 15

# 9. Разделите строку "Apple;Banana;Cherry;Date" по точке с запятой.
# Ожидаемый результат: ["Apple", "Banana", "Cherry", "Date"]
result = "Apple;Banana;Cherry;Date".split(";")
print(result)  # Вывод: ['Apple', 'Banana', 'Cherry', 'Date']

# 10. Замените "robots" на "humans" в строке "In the future, robots will rule the world.".
# Ожидаемый результат: "In the future, humans will rule the world."
result = "In the future, robots will rule the world.".replace("robots", "humans")
print(result)  # Вывод: In the future, humans will rule the world.

# 11. Преобразуйте строку "artificial intelligence" в заглавный регистр.
# Ожидаемый результат: "Artificial Intelligence"
result = "artificial intelligence".title()
print(result)  # Вывод: Artificial Intelligence

# 12. Разделите строку "Python is a versatile language" по пробелам.
# Ожидаемый результат: ["Python", "is", "a", "versatile", "language"]
result = "Python is a versatile language".split()
print(result)  # Вывод: ['Python', 'is', 'a', 'versatile', 'language']

# 13. Удалите начальные и конечные пробелы из строки "   Learn Python   ".
# Ожидаемый результат: "Learn Python"
result = "   Learn Python   ".strip()
print(result)  # Вывод: Learn Python

# Спецсимволы и экранирование символов, Форматирование строк и F-строки

# 1. Вставьте символ новой строки в строку "Hello World".
# Ожидаемый результат:
# Hello
# World
result = "Hello\nWorld"
print(result)  # Вывод: Hello\nWorld

# 2. Вставьте символ обратного слэша в строку "This is a backslash: ".
# Ожидаемый результат: "This is a backslash: \"
result = "This is a backslash: \\"
print(result)  # Вывод: This is a backslash: \

# 3. Экранируйте кавычки в строке "He said, "Hello!"".
# Ожидаемый результат: He said, "Hello!"
result = 'He said, "Hello!"'
print(result)  # Вывод: He said, "Hello!"

# 4. Экранируйте одинарные кавычки в строке "It's a sunny day".
# Ожидаемый результат: It's a sunny day
result = "It\'s a sunny day"
print(result)  # Вывод: It's a sunny day

# 5. Вставьте символ новой строки в строку "Python Programming".
# Ожидаемый результат:
# Python
# Programming
result = "Python\nProgramming"
print(result)  # Вывод: Python\nProgramming

# 6. Экранируйте кавычки в строке "She said, 'Hi!'".
# Ожидаемый результат: She said, 'Hi!'
result = "She said, \'Hi!\'"
print(result)  # Вывод: She said, 'Hi!'

# 7. Экранируйте обратный слэш в строке "Path to file: C:\\".
# Ожидаемый результат: Path to file: C:\\
result = "Path to file: C:\\\\"
print(result)  # Вывод: Path to file: C:\\

# 8. Используйте метод `format()` для строки "This is a ... course for ... learners." с переменными course="Python"
# и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."
course = "Python"
level = "beginner"
result = "This is a {} course for {} learners.".format(course, level)
print(result)  # Вывод: This is a Python course for beginner learners.

# 9. Используйте F-строку для строки "This is a ... course for ... learners." с переменными
# course="Python" и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."
course = "Python"
level = "beginner"
result = f"This is a {course} course for {level} learners."
print(result)  # Вывод: This is a Python course for beginner learners.

# 10. Используйте метод `format()` для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
topic = "Machine Learning"
result = "Welcome to the {} workshop.".format(topic)
print(result)  # Вывод: Welcome to the Machine Learning workshop.

# 11. Используйте F-строку для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
topic = "Machine Learning"
result = f"Welcome to the {topic} workshop."
print(result)  # Вывод: Welcome to the Machine Learning workshop.

# 12. Придумайте название переменной и поместите в нее строку "machine learning",
# затем преобразуйте первые буквы слов в заглавный регистр, чтобы получилось "Machine Learning".
# Затем создайте переменную со строкой "Course: ". Используйте метод `format()`, чтобы показать в консоли
# "Course: Machine Learning"
course_name = "machine learning"
formatted_course_name = course_name.title()
result = "Course: {}".format(formatted_course_name)
print(result)  # Вывод: Course: Machine Learning

# 13. Объедините строки "Data" и "Science" с пробелом между ними, дублируйте результат три раза, и используйте F-строку
# для строки "Field: ...". Ожидаемый результат: "Field: Data ScienceData ScienceData Science"
combined_string = "Data Science" * 3
result = f"Field: {combined_string}"
print(result)  # Вывод: Field: Data ScienceData ScienceData Science

# 14. Выведите третий символ строки "Information", затем используйте метод `format()` для строки "Third character: ...".
# Ожидаемый результат: "Third character: f"
third_char = "Information"[2]
result = "Third character: {}".format(third_char)
print(result)  # Вывод: Third character: f

# 15. Определите длину строки "Neural Networks", умножьте её на 2, и используйте F-строку для строки "Length: ".
# Ожидаемый результат: "Length: 28"
length = len("Neural Networks") * 2
result = f"Length: {length}"
print(result)  # Вывод: Length: 28

# 16. Преобразуйте строку "Deep Learning" в заглавный регистр, найдите индекс подстроки "LEARNING", и выведите символ
# на этом индексе. Ожидаемый результат: "L"
upper_string = "Deep Learning".upper()
index = upper_string.find("LEARNING")
result = upper_string[index]
print(result)  # Вывод: L

# 20. Определите длину строки "Starta", затем преобразуйте её в строку и добавьте к строке " has length of ",
# используя метод `format()`. Ожидаемый результат: "Starta has length of 6"
length = len("Starta")
result = "Starta has length of {}".format(length)
print(result)  # Вывод: Starta has length of 6
```