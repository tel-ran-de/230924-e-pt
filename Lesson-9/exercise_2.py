# Упражнение 1: Управление списком фильмов и их рейтингов

# 1.1 Создайте список фильмов, содержащий элементы "Movie1", "Movie2", "Movie3".
#list = ["Movie1", "Movie2", "Movie3"]
#print(list)
#
# 1.2 Пропишите условие: добавить в список фильм "Movie4", если его еще нет в списке.
#list.append("Movie4")
#print(list)
#
# 1.3 Пропишите условия: если количество фильмов больше 2, то название второго фильма меняется на "Updated Movie2".
# Если количество фильмов меньше 5, то объедините имеющийся список с новым списком ["Movie5", "Movie6", "Movie7"]
#movies = ["Movie1", "Movie2", "Movie3", "Movie4"]
#new_movies = ["Movie5", "Movie6", "Movie7"]
#if len(movies) > 2:
 #   movies[1] = "Updated Movie2"
#if len(movies) < 5:
   # movies.extend(new_movies)
#print(movies)

# 1.4 Создайте вложенный список, где каждый фильм имеет свой год выпуска и рейтинг:
# ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5], ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9],
# ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]
#print(movie_list)
#print(movie_details)film = [
   # ["Movie1", 2010, 8.1],
   # ["Updated Movie2", 2015, 7.5],
   # ["Movie3", 2020, 8.6],
   # ["Movie4", 2021, 7.9],
    #["Movie5", 2013, 8.5],
   # ["Movie6", 2018, 8.6],
  #  ["Movie7", 2023, 7.0]
#]
#print(film)

# 1.5 Добавьте фильм ["Movie", 2002, 7.7] в начало вложенного списка.
#film.insert(0,  "Movie, 2002, 7.7")
#print(film)
# 1.6 Выведите список фильмов и вложенный список.
# print(movie_list)  #  "Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6", "Movie7"
# print(movie_details)  # Ожидаемый результат: [["Movie", 2002, 7.7], ["Movie1", 2010, 8.1], ["Updated Movie2", 2015, 7.5],
# ["Movie3", 2020, 8.6], ["Movie4", 2021, 7.9], ["Movie5", 2013, 8.5], ["Movie6", 2018, 8.6], ["Movie7", 2023, 7.0]]
#movie_list = ["Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6", "Movie7"]
#movie_details = [
#    ["Movie1", 2010, 8.1],
 #   ["Updated Movie2", 2015, 7.5],
#    ["Movie3", 2020, 8.6],
 #   ["Movie4", 2021, 7.9],
#   ["Movie5", 2013, 8.5],
 #   ["Movie6", 2018, 8.6],
#    ["Movie7", 2023, 7.0]
#]
#print(movie_list)
#print(movie_details)


# Упражнение 2: Анализ списка курсов и их продолжительности

# 2.1 Создайте список курсов, содержащий элементы "Python", "Java", "JavaScript".

courses = ["Python", "Java", "JavaScript"]

# 2.2 Добавьте в список курс "C++".
courses.append("C++")
#print(courses)

# 2.3 Измените название второго курса на "Kotlin".
courses[1] = "Kotlin"
#print(courses)

# 2.4 Если первые три курса "Python", "Kotlin", "JavaScript", то создайте срез, содержащий первые три курса.
#courses.append("Java")
#print(courses)
print(courses[0:3])

# 2.5 Отсортируйте курсы по названиям.
print(sorted(courses))

# 2.6 Cоздайте вложенный список, где каждый курс имеет свою продолжительность в часах.
# ["Python", 40], ["Kotlin", 30], ["JavaScript", 35], ["C++", 50]
courses_prog = [
    ["Python", 40],
    ["Kotlin", 30],
    ["JavaScript", 35],
    ["C++", 50]
]
print(courses_prog)

# 2.7 Выполните сложение часов всех курсов во вложенном списке и выведите общую продолжительность всех курсов.
total_hours = sum(course[1] for course in courses_prog)
print(total_hours)

# 2.8 Выведите в консоль:
# - отсортированный список курсо, # Ожидаемый результат:['C++', 'JavaScript', 'Kotlin', 'Python']
# - срез, # Ожидаемый результат: ['Python', 'Kotlin', 'JavaScript']
# - вложенный список, # Ожидаемый результат: [['Python', 40], ['Kotlin', 30], ['JavaScript', 35], ['C++', 50]]
# - общую продолжительность всех курсов. # Ожидаемый результат: 155

