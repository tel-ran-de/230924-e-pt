# Проект Game Hub
#
# Вам необходимо создать консольный чат-бот Game Hub, где пользователю доступны шесть игр.
# Каждая игра располагается в отдельном модуле, которые импортируются в файл `main.py`,
# где находится меню и в котором запускается игра.
#
# main.py
#
def main_menu():
    while True:
        print("\nДобро пожаловать в Game Hub!")
        print("1. Угадай число")
        print("2. Камень, ножницы, бумага")
        print("3. Викторина")
        print("4. Виселица")
        print("5. Текстовый квест")
        print("6. Сапер")
        print("7. Выход")
        print(50 * "-")
        choice = input("Выберите игру (1-6): ")
        if choice == '1':
            print("")
        elif choice == '2':
            print("")
        elif choice == '3':
            print("")
        elif choice == '4':
            print("")
        elif choice == '5':
            print("")
        elif choice == '6':
            print("")
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Выберите действие от 1 до 7 из меню.")


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
