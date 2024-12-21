# Игра: Угадай число
#
# За основу возьмите свой код, разработанный в предыдущем проектном уроке, посвященном Game Hub (урок 13).
# Если в тот раз вы не реализовали весь функционал, то сначала реализуйте полностью игру, а затем переходите
# к рефакторингу на основе заданий из этого урока.
#
# Рефакторинг
# - Добавить логирование действий (попыток пользователя) с использованием модуля `datetime`.
# В файл записывается время начало игры, время и значение каждой попытки, время окончания игры и результат.
# - Добавить обработку ошибок с использованием `try/except`, где это необходимо.



import random
import datetime



def log_action(message):
    with open("guess_number_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {message}\n")



def guess_number():
    number_to_guess = random.randint(0, 100)
    attempts = 6
    guesses = []

    log_action("Начало игры")

    print("Угадайте число от 0 до 100. У вас есть 6 попыток.")

    for attempt in range(attempts):
        try:
            guess = input(f"Попытка {attempt + 1}: Введите число: ")
            if not guess.isdigit():
                raise ValueError("Пожалуйста, введите целое число.")
            guess = int(guess)
            guesses.append(guess)
            log_action(f"Попытка {attempt + 1}: Введено число {guess}")

            if guess < number_to_guess:
                print("Загаданное число больше.")
            elif guess > number_to_guess:
                print("Загаданное число меньше.")
            else:
                print(f"Отлично! Вы угадали число {number_to_guess} с {attempt + 1} попытки!")
                log_action(f"Игрок угадал число {number_to_guess} с {attempt + 1} попытки.")
                break
        except ValueError as e:
            print(e)

    else:
        print(f"К сожалению, вы не угадали число. Загаданное число было: {number_to_guess}.")
        log_action(f"Игрок не угадал число. Загаданное число было: {number_to_guess}.")

    print(f"Ваши попытки: {guesses}")
    print(f"Загаданное число: {number_to_guess}")
    log_action("Конец игры\n================")

guess_number()