# Тема: Модуль datetime
from datetime import datetime

# Задача 1: Определение текущей даты и времени
# Напишите программу, которая выводит текущие дату и время в формате "YYYY-MM-DD HH:MM:SS".
# Пример: 2024-06-11 14:35:45

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)

# Задача 2: Вычисление возраста
# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.

# # Функция для вычисления возраста
def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
    today = datetime.today()
    result = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return result

bd = input("Введите дату рождения в формате DD.MM.YYYY: ")
age = calculate_age(bd)
print(f"Ваш возраст: {age} лет")


# Задача 3: Расчет дней до следующего мероприятия
# Напишите программу, которая принимает дату следующего мероприятия в формате "YYYY-MM-DD" и выводит количество дней,
# оставшихся до этой даты.

def days_until_event(event_date):
    event_date = datetime.strptime(event_date, "%Y-%m-%d").date()   # Преобразование строки в объект даты
    today = datetime.today().date()

    days_remaining = (event_date - today).days  # Вычисление разницы в днях

    if days_remaining < 0:
        return "Мероприятие уже прошло!"    # Проверка на прошедшую дату
    return days_remaining

event_date_input = input("Введите дату следующего мероприятия в формате YYYY-MM-DD: ")
try:
    result = days_until_event(event_date_input)
    if isinstance(result, int):
        print(f"До мероприятия осталось {result} дней.")
    else:
        print(result)
except ValueError:
    print("Ошибка: Некорректный формат даты. Используйте YYYY-MM-DD.")

# Задача 4: Определение дня недели
# Напишите программу, которая принимает дату в формате "YYYY-MM-DD" и выводит день недели для этой даты.

# определения дня недели
def get_day_of_week(date_input):
    # Преобразование строки в объект даты
    date = datetime.strptime(date_input, "%Y-%m-%d").date()
    # Получение дня недели
    day_of_week = date.strftime("%A")  # Полное название дня недели
    return day_of_week

date_input = input("Введите дату в формате YYYY-MM-DD: ")
try:
    day_of_week = get_day_of_week(date_input)
    print(f"День недели для даты {date_input}: {day_of_week}")
except ValueError:
    print("Ошибка: Некорректный формат даты. Используйте YYYY-MM-DD.")

# Задача 5: Сравнение двух дат
# Напишите программу, которая принимает две даты в формате "YYYY-MM-DD" и определяет, какая из них позже.


def compare_dates(date1, date2):
    # Преобразование строк в объекты даты
    date1 = datetime.strptime(date1, "%Y-%m-%d").date()
    date2 = datetime.strptime(date2, "%Y-%m-%d").date()

    if date1 > date2:
        return f"Дата {date1} позже даты {date2}."
    elif date1 < date2:
        return f"Дата {date1} раньше даты {date2}."
    else:
        return f"Дата {date1} совпадает с датой {date2}."

date1_input = input("Введите первую дату в формате YYYY-MM-DD: ")
date2_input = input("Введите вторую дату в формате YYYY-MM-DD: ")

try:
    result = compare_dates(date1_input, date2_input)
    print(result)
except ValueError:
    print("Ошибка: Некорректный формат даты. Используйте YYYY-MM-DD.")
