# Проект Game Hub
#
# Вам необходимо создать консольный чат-бот Game Hub, где пользователю доступны шесть игр.
# Каждая игра располагается в отдельном модуле, которые импортируются в файл `main.py`,
# где находится меню и в котором запускается игра.
#
# main.py
from guess_number import game_guess_number
from quiz_game import quiz_game_main
from rock_paper_scissors import game_paper_scissors
from hangman import game_hangman
from text_adventure import text_quest
from minesweeper import main_game_minesweeper


def main_menu():
    while True:
        print("\nДобро пожаловать в Game Hub!")
        print("1. Угадай число")
        print("2. Камень, ножницы, бумага")
        print("3. Викторина")
        print("4. Виселица")
        print("5. Текстовый квест")
        print("6. Сапер")
        print("0. Выход")
        print(28 * "-")
        choice = input("Выберите игру (1-6): ")
        if choice == '1':
            game_guess_number()
            print("")
        elif choice == '2':
            game_paper_scissors()
            print("")
        elif choice == '3':
            quiz_game_main()
            print("")
        elif choice == '4':
            game_hangman()
            print("")
        elif choice == '5':
            text_quest()
            print("")
        elif choice == '6':
            main_game_minesweeper()
            print("")
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Выберите действие от 0 до 6 из меню.")


if __name__ == "__main__":
    print('Файл запущен напрямую')
    main_menu()
# допишите файл main.py в конце и протестируйте работоспособность всех игр.
#
# Постарайтесь реализовать не только логику игры, но и обработать потенциальный ошибочный ввод пользователя.
# Предусмотрите возможность досрочного завершения игры, возвращения в меню и выбор новой игры.
#
# Распределите создание игр между студентами своей команды. Обсуждайте возникшие трудности и делайте код ревью.
# В конце соедините получившиеся игры в файле main и протестируйте совместную работу всех игр.
#
# Обращайтесь к chatGPT только с точечными вопросами по реализации, например,
# “Как в модуле random вызвать функцию, которая выберет случайное значение в списке?”.
# Если вы обратитесь к нему с условиями игры, и он за вас ее напишет, то вы ничему не научитесь.
#
# Описания игр находятся в отдельных файлах, созданных под каждую игру.
# 1. Угадай число - guess_number.py
# 2. Камень, ножницы, бумага - rock_paper_scissors.py
# 3. Викторина - quiz_game.py
# 4. Виселица - hangman.py
# 5. Текстовый квест - text_adventure.py
# 6. Сапер - minesWeeper.py
