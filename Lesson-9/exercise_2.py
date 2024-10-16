# Упражнение 1: Управление списком фильмов и их рейтингов

# 1.1 Создайте список фильмов, содержащий элементы "Movie1", "Movie2", "Movie3".
films_list = ["Movie1", "Movie2", "Movie3"]
# 1.2 Пропишите условие: добавить в список фильм "Movie4", если его еще нет в списке.
if "Movie4" in films_list:
    print("Данный фильм уже содержится в списке")
else:
    films_list.append("movie4")
# 1.3 Пропишите условия: если количество фильмов больше 2, то название второго фильма меняется на "Updated Movie2".
# Если количество фильмов меньше 5, то объедините имеющийся список с новым списком ["Movie5", "Movie6", "Movie7"]
films_list2 = ["movie5", "Movie6", "Movie7"]
film_qantity = int(len(films_list))
if film_qantity > 2:
    films_list[1] = "Updares Movie2"
# пробовал эту строку через elif, не работает почему то
if film_qantity < 5:
    films_list.extend(films_list2)
else:
    print()
# 1.4 Создайте вложенный список, где каждый фильм имеет свой год выпуска и рейтинг:
# ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9],
# ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]
films_detals = [
    ["Movie1", 2010, 8.1],
    ["Updated Movie2", 2015, 7.5],
    ["Movie3", 2020, 8.6],
    ["Movie4", 2021, 7.9],
    ["Movie5", 2013, 8.5],
    ["Movie6", 2018, 8.6],
    ["Movie7", 2023, 7.0]
]
# 1.5 Добавьте фильм ["Movie", 2002, 7.7] в начало вложенного списка.
films_detals.insert(0, ["Movie", 2002, 7.7])
# 1.6 Выведите список фильмов и вложенный список.
# print(movie_list)  #  "Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6", "Movie7"
# print(movie_details)  # Ожидаемый результат: [["Movie", 2002, 7.7], ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5],
# ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]
print(films_list)
print(films_detals)





# Упражнение 2: Анализ списка курсов и их продолжительности

# 2.1 Создайте список курсов, содержащий элементы "Python", "Java", "JavaScript".
kurses = ["Python", "Java", "JavaScript"]

# 2.2 Добавьте в список курс "C++".
kurses.append("C++")

# 2.3 Измените название второго курса на "Kotlin".
kurses[1] = "Kotlin"

# 2.4 Если первые три курса "Python", "Kotlin", "JavaScript", то создайте срез, содержащий первые три курса.
if kurses[0:3] == (["Python", "Kotlin", "JavaScript"]):
    print(kurses[0:3])

# 2.5 Отсортируйте курсы по названиям.
kurses.sort()
print(kurses)

# 2.6 Cоздайте вложенный список, где каждый курс имеет свою продолжительность в часах.
# ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]
kurses_details = [
    ["Python", 40],
    ["Kotlin", 30],
    ["JavaScript", 35],
    ["C++", 50]
]
print(kurses_details)

# 2.7 Выполните сложение часов всех курсов во вложенном списке и выведите общую продолжительность всех курсов.
print(kurses_details[0] [1] + kurses_details[1] [1] + kurses_details[2] [1] + kurses_details[3] [1])

# 2.8 Выведите в консоль:
# - отсортированный список курсо, # Ожидаемый результат:['C++', 'JavaScript', 'Kotlin', 'Python']
# - срез, # Ожидаемый результат: ['Python', 'Kotlin', 'JavaScript']
# - вложенный список, # Ожидаемый результат: [['Python', 40], ['Kotlin', 30], ['JavaScript', 35], ['C++', 50]]
# - общую продолжительность всех курсов. # Ожидаемый результат: 155

