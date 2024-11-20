# Игра "Виселица"
#
# Напишите программу для игры "Виселица". Игроку дается слово, которое он должен угадать, называя буквы.
# Если игрок называет неправильную букву, ему начисляется штрафное очко.
# Игра заканчивается победой при угадывании слова или проигрышем при достижении лимита штрафных очков.
#
# Требования:
#
# 1. Программа должна случайным образом выбирать слово из списка.
# 2. Игрок должен иметь возможность вводить буквы по одной за попытку.
# 3. Если игрок угадал букву, она должна отображаться в правильных позициях в слове.
# Вместо остальных (скрытых) букв показываются звездочки *.
# 4. Если игрок назвал неправильную букву, количество штрафных очков должно увеличиваться.
# 5. Игра заканчивается победой, если все буквы слова угаданы, или проигрышем,
# если количество штрафных очков достигает лимита (например, 6).





import random

"Список слов "
word_list = ['python', 'programming', 'developer', 'hangman', 'computer', 'algorithm']

"штрафных очков"
max_tries = 6


"Виселица"


def play_hangman():

    "случайное слово"
    word = random.choice(word_list)
    word_length = len(word)

    "хранения  букв"
    guessed_letters = set()

    "скрытых букв "
    hidden_word = ['*' for _ in range(word_length)]

    "штраф очков"
    attempts_left = max_tries

    print("'Виселица'!")



    while attempts_left > 0:
        print("\nслово: " + ' '.join(hidden_word))
        print(f"попыток: {attempts_left}")


        guess = input("букву: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("букву.")
            continue

        if guess in guessed_letters:
            print(f"угадывали букву '{guess}'.")
            continue

        "список"
        guessed_letters.add(guess)


        if guess in word:
            print(f"Буква '{guess}'.")
            for i in range(word_length):
                if word[i] == guess:
                    hidden_word[i] = guess
        else:
            attempts_left -= 1
            print(f"Буквы'{guess}' нет .")


        if '*' not in hidden_word:
            print("\n угадали слово:", word)
            break

    "закончились"
    if attempts_left == 0:
        print("\n Слово:", word)


"Запуск"
if __name__ == "__main__":
    play_hangman()

################################################################################


