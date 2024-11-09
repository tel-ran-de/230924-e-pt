# Игра: Сапёр рекомендации Евгений
pattern_list = [
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

import random


for row in pattern_list:
    print(" ".join(row))
print()

game_coord = []

for v in range(0, 5):
    x1 = random.randrange(0, 5)
    y1 = random.randrange(0, 5)
    pattern_list[int(x1)][int(y1)] = 'X'
    pl = [x1, y1]
    game_coord.append(pl)

for row in pattern_list:
    print(" ".join(row))


while True:
    user = True

    a = input()
    c = a.split()
    print(a, c)
    print(c)  # list

    x, y = c[0], c[1]
    print("Координаты : x:", int(x) + 1, " y:", int(y) + 1)

    # if user == True:
    #    pattern_list[int(x)][int(y)] = 'X'

    for row in pattern_list:
        print(" ".join(row))
    print()