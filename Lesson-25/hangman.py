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
#игра hangman.py с исключениями, чтобы программа не завершалась с ошибкой при некорректном вводе.
import random
import logging
from datetime import datetime
import json
import os #для проверки существования файла
#настраиваю логирование
logging.basicConfig(filename="hangman.log", level=logging.INFO, format="%(asctime)s - %(message)s", encoding="utf-8")
#hangman.log файл в который будут записываться логи, %(asctime)s добавляет метку времени (дата и время)
# к каждому сообщению,  %(message)s добавляет само сообщение.
# Список слов
words = ["mouse", "elephant", "duck", "cat", "dog", "horse"]
# Подключаю рандом для выбора слова
word = random.choice(words)
# Создаем переменные и присваиваем им начальные значения
# - записываем угаданные буквы в список, неправильные попытки и количество попыток
guessed_letters = []  # Список угаданных букв
wrong_attempts = 0
max_attempts = 6
save_file = "hangman_save.json"

def load_game():#функции для сохранения и загрузки текущего прогресса игры в файл.
    global word, guessed_letters, wrong_attempts
    if os.path.exists(save_file):#в сэйф файле сохраняем прогресс игры
        with open(save_file, 'r', encoding='utf-8') as file:#проверяем существует лий файл сохранения, если да
            data = json.load(file)#то открывает и загружает данные,
            word = data['word']
            guessed_letters = data['guessed_letters']
            wrong_attempts = data['wrong_attempts']
            logging.info("Game logen")#если файл не нашел то логирует сообщение о начале новой игры
    else:
        logging.info("Файл сохранения не найден. Начинаем новую игру.")

def save_game():#словарь с данными игры
    data = {
        'word': word,#сохраняется загаданное слово
        'guessed_letters': guessed_letters,#сохраняется список угаданных букв
        'wrong_attempts': wrong_attempts#сохранение неудачных попыток
    }
    with open(save_file, 'w', encoding='utf-8') as file:#открываю файл hangman_save.json для записи
        json.dump(data, file)#записываю словарь дата в файл в формате джейсон
    logging.info("Игра сохранена.")#pаписываем сообщение в лог-файл, что игра была сохранена

def display_game_state():
    display_word = ""  # Пустая строка для записи и показа состояния отгадывания слова
    for letter in word:  # Проходим по каждой букве в загаданном слове
        if letter in guessed_letters:  # Если буква есть в guessed_letters
            display_word += letter  # Добавляем ее к строке display_word
        else:
            display_word += "*"  # Если нет, то ставим звезду
    print(display_word)

# Функция для обработки букв, принимает один аргумент letter
def process_letter(letter):
    global wrong_attempts
    if letter in word:  # Проверяем, содержится ли введенная буква в загаданном слове word
        guessed_letters.append(letter)  # Добавляем букву в guessed_letters, если она есть в word
    else:
        wrong_attempts += 1  # Иначе увеличиваем количество неправильных попыток на 1

def display_hangman(attempts):  # Берем один аргумент attempts
    stages = [  # Список отображения этапов угадывания
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        --------
        """
    ]

    return stages[attempts]  # Возврат строки из списка этапов соответственно текущему количеству неправильных попыток

def main():#точка входа в программу  и управленние всей логикой игры
    logging.info("Начало новой игры.")#записываем сообщение в лог-файл, говорим что начата новая игра
    load_game()#загружаю сохраненную игру
    try:
        while wrong_attempts < max_attempts:  # В цикле пока число неправильных попыток меньше максимальных
            print(display_hangman(wrong_attempts))  # На начало каждой итерации отображаем этап виселицы
            display_game_state()  # Показываем текущее состояние слова
            letter = input("Введите букву: ").lower()
            if len(letter) != 1 or not letter.isalpha():  # Проверка на корректность ввода
                print("Ошибка: введите одну букву.")
                continue
            if letter in guessed_letters:  # Если буква уже была угадана
                print("Вы уже угадали эту букву.")  # Выводится сообщение
                continue  # Идем на следующий круг
            process_letter(letter)  # Если буква не была угадана ранее, передаем букву в функцию process_letter для обработки
            logging.info(f"Попытка: {letter}, Угаданные буквы: {guessed_letters}, Неправильные попытки: {wrong_attempts}")
            if all(letter in guessed_letters for letter in word):  # После обработки буквы проверяем, угаданы ли все буквы в слове
                print(f"Поздравляем, вы выиграли! Загаданное слово: {word}")
                logging.info("Игра завершена победой.")
                if os.path.exists(save_file):
                    os.remove(save_file)
                break
        else:
            print(display_hangman(wrong_attempts))
            print(f"Вы проиграли! Загаданное слово было: {word}")
            logging.info("Игра завершена поражением.")
            if os.path.exists(save_file):
                os.remove(save_file)
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        save_game()

if __name__ == "__main__": main()


