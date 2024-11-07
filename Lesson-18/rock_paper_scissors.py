# Игра: Камень, ножницы, бумага
#
# Создайте игру "Камень, ножницы, бумага", где пользователь играет против компьютера.
# Компьютер случайным образом выбирает одно из трех значений: камень, ножницы или бумагу.
# Пользователь вводит свой выбор, и программа определяет победителя. Если выборы одинаковы, игра объявляет ничью.
# Игра продолжается до тех пор, пока один из игроков (пользователь или компьютер)
# не одержит на три победы больше, чем соперник. В конце показывается итоговый счет и объясляется победитель.

import random


def game_paper_scissors():
    comp_choice = random.randint(1, 3)
    win_comp = 0
    win_user = 0
    while True:
        print("1. Камень")
        print("2. Ножницы")
        print("3. Бумага")
        user_choice = int(input("Выберите действие: "))
        if user_choice < 1 or user_choice > 3:
            print("Некорректный ввод! ")
        if win_comp-win_user == 2:
            print(f"Победил компьютер счет {win_comp+1} - {win_user}")
            break
        elif win_user-win_comp == 2:
            print(f"Победил пользователь счет {win_user+1} - {win_comp}")
            break

        if user_choice == 1:
            if comp_choice == 1:
                print("Ничья")
            elif comp_choice == 2:
                win_user+=1
                print(f"Победил пользователь счет {win_user} - {win_comp}")
            else:
                win_comp+=1
                print(f"Победил компьютер счет {win_comp} - {win_user}")
        elif user_choice == 2:
            if comp_choice == 1:
                win_comp += 1
                print(f"Победил компьютер счет {win_comp} - {win_user}")
            elif comp_choice == 2:
                print("Ничья")
            else:
                win_user += 1
                print(f"Победил пользователь счет {win_user} - {win_comp}")
        elif user_choice == 3:
            if comp_choice == 1:
                win_user += 1
                print(f"Победил пользователь счет {win_user} - {win_comp}")
            elif comp_choice == 2:
                win_comp += 1
                print(f"Победил компьютер счет {win_comp} - {win_user}")
            else:
                print("Ничья")

game_paper_scissors()

if __name__ == '__main__':
    print('Файл запущен напрямую')