# Темы: Операции над строками, Индексы и срезы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Объедините строки "Hello" и "London" без пробела. Ожидаемый результат: "HelloLondon"
str1 = 'Hello'
str2 = 'London'
result = str1  + str2
print(result)
print()
# 2. Выведите последний символ строки "Programming". Ожидаемый результат: "g"
str3 = "Programming"
print(str3[-1])
# 3. Дублируйте строку "Hi" три раза. Ожидаемый результат: "HiHiHi"
print("Hi"*3)

# 4. Определите длину строки "Artificial Intelligence".
print(len("Artificial Intelligence"))

# 5. Объедините строки "Good" и "Morning" с запятой между ними. Ожидаемый результат: "Good,Morning"
print("Good" + "," + "Morning")

# 6. Создайте срез строки "Natural Language Processing" со значением "nguag".
print("Natural Language Processing"[10:15])

# 7. Объедините строки "Data" и "Science" с дефисом между ними. Ожидаемый результат: "Data-Science"
print("Data" + "-" + "Science")

# 8. Объедините строки "AI" и "ML" с двоеточием между ними. Ожидаемый результат: "AI:ML"
print("AI" + ":" + "ML")

# 9. Дублируйте строку "Test" шесть раз. Ожидаемый результат: "TestTestTestTestTestTest"
print("Test"*6)

# 10. Выведите первый символ строки "Python". Ожидаемый результат: "P"
print("Python"[0])

# 11. Создайте срез строки "Hello, Anna!" от 0 до 5. Ожидаемый результат: "Hello"
print ("Hello, Anna!"[:5])

# 12. Определите длину строки "Natural Language Processing".
print(len("Natural Language Processing"))

# 13. Выведите второй символ строки "Лето". Ожидаемый результат: "е"
print ("Лето"[1])

# 14. Выведите предпоследний символ строки "Machine Learning". Ожидаемый результат: "n"
print ("Machine Learning"[-2])

# 15. Дублируйте строку "Yes" четыре раза. Ожидаемый результат: "YesYesYesYes"
print("Yes"*4)

# 16. Создайте срез строки "Deep Learning" со значением "ep Le".
print ("Deep Learning"[2:7])

# 17. Выведите третий символ строки "Computer Vision". Ожидаемый результат: "m"
print ("Computer Vision"[2])

# 18. Определите длину строки "Deep Learning". Ожидаемый результат: 13
print(len("Deep Learning"))

# 19. Объедините строки "Python" и "Rocks" с пробелом между ними. Ожидаемый результат: "Python Rocks"
print("Python" + " " + "Rocks")

# 20. Создайте срез строки "Data Science" со значением "cien".
print ("Data Science"[6:10])

#===================================================================================================
# Тема: Основные методы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Преобразуйте строку "hOw aRe yOu?" в верхний регистр.
# Ожидаемый результат: "HOW ARE YOU?"
print("hOw aRe yOu?".upper())

# 2. Посчитайте количество символов "a" в строке "Bananas are amazing!".
print("Bananas are amazing!".count('a'))

# 3. Преобразуйте строку "PYTHON PROGRAMMING" в нижний регистр.
# Ожидаемый результат: "python programming"
print("PYTHON PROGRAMMING".lower())

# 4. Удалите начальные пробелы из строки "   Discover new worlds   ".
# Ожидаемый результат: "Discover new worlds   "
print("   Discover new worlds   ".lstrip())

# 5. Замените "rainy" на "sunny" в строке "It was a rainy day.".
# Ожидаемый результат: "It was a sunny day."
print("It was a rainy day.".replace("rainy", "sunny"))

# 6. Найдите индекс подстроки "innovation" в строке "Innovation drives progress.".
print("Innovation drives progress.".find("innovation"))

# 7. Удалите конечные пробелы из строки "   Explore the universe   ".
# Ожидаемый результат: "   Explore the universe"
print("   Explore the universe   ".rstrip())

# 8. Найдите индекс подстроки "galaxy" в строке "The Milky Way galaxy is vast.".
print("The Milky Way galaxy is vast.".find("galaxy"))

# 9. Разделите строку "Apple;Banana;Cherry;Date" по точке с запятой.
# Ожидаемый результат: ["Apple", "Banana", "Cherry", "Date"]
print("Apple;Banana;Cherry;Date".split(';'))

# 10. Замените "robots" на "humans" в строке "In the future, robots will rule the world.".
# Ожидаемый результат: "In the future, humans will rule the world."
print("In the future, robots will rule the world.".replace("robots", "humans"))

# 11. Преобразуйте строку "artificial intelligence" в заглавный регистр.
# Ожидаемый результат: "Artificial Intelligence"
print("artificial intelligence".title())

# 12. Разделите строку "Python is a versatile language" по пробелам.
# Ожидаемый результат: ["Python", "is", "a", "versatile", "language"]
print("Python is a versatile language".split())

# 13. Удалите начальные и конечные пробелы из строки "   Learn Python   ".
# Ожидаемый результат: "Learn Python"
print("   Learn Python   ".lstrip().rstrip())
#===================================================================================================
# Темы: Спецсимволы и экранирование символов, Форматирование строк и F-строки
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Вставьте символ новой строки в строку "Hello World".
# Ожидаемый результат:
# Hello
# World
print('Hello \nWorld')

# 2. Вставьте символ обратного слэша в строку "This is a backslash: ".
# Ожидаемый результат: "This is a backslash: \"
print("This is a backslash: \\")

# 3. Экранируйте кавычки в строке "He said, "Hello!"".
# Ожидаемый результат: He said, "Hello!"
print("He said, \"Hello!\"")

# 4. Экранируйте одинарные кавычки в строке "It's a sunny day".
# Ожидаемый результат: It's a sunny day
print("It's a sunny day")

# 5. Вставьте символ новой строки в строку "Python Programming".
# Ожидаемый результат:
# Python
# Programming
print("Python \nProgramming")

# 6. Экранируйте кавычки в строке "She said, 'Hi!'".
# Ожидаемый результат: She said, 'Hi!'
print("She said, 'Hi!'")

# 7. Экранируйте обратный слэш в строке "Path to file: C:\\".
# Ожидаемый результат: Path to file: C:\\
print("Path to file: C:\\\\")

# 8. Используйте метод `format()` для строки "This is a ... course for ... learners." с переменными course="Python"
# и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."
print("This is a {} course for {} learners.".format("Python", "beginner"))

# 9. Используйте F-строку для строки "This is a ... course for ... learners." с переменными
# course="Python" и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."
print(f"This is a {"Python"} course for {"beginner"} learners.")

# 10. Используйте метод `format()` для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
topic="Machine Learning"
print("Welcome to the {} workshop.".format(topic))

# 11. Используйте F-строку для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
topic="Machine Learning"
print(f"Welcome to the {topic} workshop.")

# 12. Придумайте название переменной и поместите в нее строку "machine learning",
# затем преобразуйте первые буквы слов в заглавный регистр, чтобы получилось "Machine Learning".
# Затем создайте переменную со строкой "Course: ". Используйте метод `format()`, чтобы показать в консоли
# "Course: Machine Learning"
topic = "machine learning"
topic = topic.title()
print("Course: {}".format(topic))

# 13. Объедините строки "Data" и "Science" с пробелом между ними, дублируйте результат три раза, и используйте F-строку
# для строки "Field: ...". Ожидаемый результат: "Field: Data ScienceData ScienceData Science"

print("Field: " + "Data Science"*3)

# 14. Выведите третий символ строки "Information", затем используйте метод `format()` для строки "Third character: ...".
# Ожидаемый результат: "Third character: f"

str = "Information"
print(str[2])
print("Third character: {} ".format(str[2]))

# 15. Определите длину строки "Neural Networks", умножьте её на 2, и используйте F-строку для строки "Length: ".
# Ожидаемый результат: "Length: 28"

st = "Neural Networks"
st = st.replace(' ', '')
count_st = (len(st)*2)
print(f"Length: {count_st}")

# 16. Преобразуйте строку "Deep Learning" в заглавный регистр, найдите индекс подстроки "LEARNING", и выведите символ
# на этом индексе. Ожидаемый результат: "L"

str16 = "Deep Learning".upper()
str16_1 = str16.find("LEARNING")
print(str16[str16_1])

# 20. Определите длину строки "Starta", затем преобразуйте её в строку и добавьте к строке " has length of ",
# используя метод `format()`. Ожидаемый результат: "Starta has length of 6"

topic="Starta"
l=len(topic)
print("{} has length of".format(topic), l)