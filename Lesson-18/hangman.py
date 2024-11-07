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

words = ["mouse", "elephant", "duck", "cat", "dog", "horse"]

word = random.choice(words)

letters = []
falce_attempts = 0
max_attempts = 6

def game_start():
    start_word = ""
    for letter in word:
        if letter in letters:
            start_word += letter
        else:
            start_word += "*"
        print(start_word)
def the_game_is_on(letter):
    global falce_attempts
    if letter in word:
        letters.append(letter)
    else:
        falce_attempts += 1
while falce_attempts < max_attempts:
        game_start()
        letter = input("Введите букву: ")
        the_game_is_on(letter)

        if all(letter in letters for letter in word):
            print("Поздравляем, вы выиграли!")
        break
else:
    print(f"Вы проиграли! Загаданное слово было: {word}")
