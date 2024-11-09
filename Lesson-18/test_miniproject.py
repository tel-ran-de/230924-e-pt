import random

def get_user_choice():
    while True:
        try:
            print("1. Камень")
            print("2. Ножницы")
            print("3. Бумага")
            user_choice = int(input("Выберите действие: "))
            if 1 <= user_choice <= 3:
                return user_choice
            else:
                print("Некорректный ввод! Пожалуйста, введите число от 1 до 3.")
        except ValueError:
            print("Некорректный ввод! Пожалуйста, введите число.")

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "ничья"
    elif (user_choice == 1 and comp_choice == 2) or \
         (user_choice == 2 and comp_choice == 3) or \
         (user_choice == 3 and comp_choice == 1):
        return "пользователь"
    else:
        return "компьютер"

def game_paper_scissors():
    win_comp = 0
    win_user = 0
    print("---------------Игра: 'Камень, ножницы, бумага'.---------------")
    print("Игра продолжается до тех пор, пока один из игроков не одержит на три победы больше, чем соперник.")

    while abs(win_comp - win_user) < 3:
        comp_choice = random.randint(1, 3)
        user_choice = get_user_choice()

        result = determine_winner(user_choice, comp_choice)
        if result == "ничья":
            print("Ничья")
        elif result == "пользователь":
            win_user += 1
            print(f"Победил пользователь. Счет: {win_user} - {win_comp}")
        else:
            win_comp += 1
            print(f"Победил компьютер. Счет: {win_comp} - {win_user}")

    if win_user > win_comp:
        print(f"Победил пользователь счет {win_user} - {win_comp}")
    else:
        print(f"Победил компьютер счет {win_comp} - {win_user}")

if __name__ == '__main__':
    print('Файл запущен напрямую')
    game_paper_scissors()
