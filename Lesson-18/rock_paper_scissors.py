# Игра: Камень, ножницы, бумага
#
# Создайте игру "Камень, ножницы, бумага", где пользователь играет против компьютера.
# Компьютер случайным образом выбирает одно из трех значений: камень, ножницы или бумагу.
# Пользователь вводит свой выбор, и программа определяет победителя. Если выборы одинаковы, игра объявляет ничью.
# Игра продолжается до тех пор, пока один из игроков (пользователь или компьютер)
# не одержит на три победы больше, чем соперник. В конце показывается итоговый счет и объясляется победитель.





import random


choices = ['камень', 'ножницы', 'бумага']


"игры"

def play_game():
    user_score = 0,
    computer_score = 0,

    while abs(user_score - computer_score) < 3:
        "выбор"

        user_choice = input("(камень, ножницы, бумага):").lower()

        "ввод"

        if user_choice not in choices:
            print(" выберите: камень, ножницы или бумага.")
            continue

        "Комп"

        computer_choice = random.choice(choices)
        print(f"Компьютер выбрал: {computer_choice}")

        "Определение"

        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
                (user_choice == 'ножницы' and computer_choice == 'бумага') or \
                (user_choice == 'бумага' and computer_choice == 'камень'):
            print("Вы выиграли!")
            user_score += 1
        else:
            print("Комп !")
            computer_score += 1


        print(f"Текущий счет: {user_score}, Компьютер - {computer_score}")

    "победителя"

    if user_score > computer_score:
        print("\n выиграли ")
    else:
        print("\nК победил!")


# Запуск игры
if __name__ == "__main__":
    play_game()