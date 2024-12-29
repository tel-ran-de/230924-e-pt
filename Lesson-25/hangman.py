# Игра "Виселица"
#
# За основу возьмите свой код, разработанный в предыдущем проектном уроке, посвященном Game Hub (урок 13).
# Если в тот раз вы не реализовали весь функционал, то сначала реализуйте полностью игру, а затем переходите
# к рефакторингу на основе заданий из этого урока.
#
# Рефакторинг
# - Добавить логирование начала и окончания игры и всех попыток игрока с временными метками (дата и время).
# - Добавить обработку ошибок с использованием `try/except`, где это необходимо.
# - Добавить возможность сохранять текущий прогресс игры в файл для продолжения игры позже,
# если игра не была завершена победой или поражением (то есть было прерывание программы во время игры).


import os
import time
import json
from datetime import datetime


# Функция для логирования
def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {message}")
    with open("game_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - {message}\n")


# Функция для сохранения прогресса игры
def save_game(word, guessed_letters, attempts_left):
    game_state = {
        "word": word,
        "guessed_letters": guessed_letters,
        "attempts_left": attempts_left
    }
    with open("game_state.json", "w") as file:
        json.dump(game_state, file)
    log("Прогресс игры сохранен.")


# Функция для загрузки сохраненного прогресса
def load_game():
    if os.path.exists("game_state.json"):
        try:
            with open("game_state.json", "r") as file:
                game_state = json.load(file)
            log("Прогресс игры загружен.")
            return game_state
        except Exception as e:
            log(f"Ошибка при загрузке игры: {e}")
    return None


# Функция для отображения текущего состояния слова
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


# Основная логика игры
def hangman():
    word = "python"  # Загаданное слово
    guessed_letters = []  # Угаданные буквы
    attempts_left = 6  # Количество попыток
    game_over = False

    # Загружаем сохраненную игру, если она есть
    saved_game = load_game()
    if saved_game:
        word = saved_game["word"]
        guessed_letters = saved_game["guessed_letters"]
        attempts_left = saved_game["attempts_left"]

    log("Игра началась.")

    while not game_over:
        try:
            print(f"Текущее слово: {display_word(word, guessed_letters)}")
            print(f"Осталось попыток: {attempts_left}")
            guess = input("Введите букву: ").lower()

            # Проверка на правильность ввода
            if len(guess) != 1 or not guess.isalpha():
                print("Пожалуйста, введите одну букву.")
                continue

            # Проверка, не была ли буква уже угадана
            if guess in guessed_letters:
                print("Вы уже угадывали эту букву.")
                continue

            guessed_letters.append(guess)

            # Проверка, есть ли буква в слове
            if guess in word:
                print(f"Правильно! Буква {guess} есть в слове.")
            else:
                attempts_left -= 1
                print(f"Ошиблись! Буквы {guess} нет в слове.")

            # Сохраняем прогресс игры
            save_game(word, guessed_letters, attempts_left)

            # Проверка на выигрыш
            if all(letter in guessed_letters for letter in word):
                print(f"Поздравляем! Вы угадали слово: {word}")
                game_over = True
                log("Игра закончена победой.")

            # Проверка на проигрыш
            if attempts_left <= 0:
                print(f"Вы проиграли! Загаданное слово было: {word}")
                game_over = True
                log("Игра закончена поражением.")

        except Exception as e:
            log(f"Ошибка во время игры: {e}")
            print("Произошла ошибка. Пожалуйста, попробуйте снова.")
            save_game(word, guessed_letters, attempts_left)

    log("Игра завершена.")


# Запуск игры
if __name__ == "__main__":
    hangman()