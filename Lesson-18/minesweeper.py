# Игра: Сапёр
#
# Цель игры: открыть все клетки, не содержащие мин.
#
# Правила игры:
#
# 1. Игровое поле состоит из клеток размером 5x5.
# 2. На поле случайным образом размещены 5 мин.
# 3. Игрок вводит координаты клетки (например, "2 3" для второй строки и третьего столбца), чтобы проверить ее.
# 4. Если игрок открывает клетку с миной, он проигрывает.
# 5. Если игрок открывает клетку без мины, на этой клетке отображается число, указывающее, сколько мин находится в соседних клетках (по горизонтали, вертикали и диагоналям).
# 6. Игрок побеждает, если открывает все клетки, не содержащие мин.
#
# Пример игрового процесса:
#
# 1. Игроку показывается пустое поле:
# - - - - -
# - - - - -
# - - - - -
# - - - - -
# - - - - -
#
# 2. Игрок вводит координаты клетки:
# Введите координаты клетки (строка столбец): 2 3
#
# 3. Если в этой клетке нет мины, открывается число:
# - - - - -
# - - 1 - -
# - - - - -
# - - - - -
# - - - - -
#
# 4. Игрок продолжает вводить координаты, пока не откроет все безопасные клетки или не попадет на мину.
# 5. Если игрок открывает клетку с миной, игра заканчивается:
# - - - - -
# - - * - -
# - - - - -
# - - - - -
# - - - - -
# Вы проиграли! Вы попали на мину.
#
# 6. Если игрок открывает все клетки без мин, игра заканчивается победой:
# - 1 1 1 -
# - 1 * 1 -
# - 2 2 2 -
# - 1 * 1 -
# - 1 1 1 -
# Поздравляем! Вы открыли все безопасные клетки.



################################################################

import random

GRID_SIZE = 5
MINES_COUNT = 5


def create_grid():
    grid = [['-' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    return grid

"Проверка"

def place_mines(grid):
    mines = random.sample(range(GRID_SIZE * GRID_SIZE), MINES_COUNT)
    for mine in mines:
        row, col = divmod(mine, GRID_SIZE)
        grid[row][col] = '*'
    return grid

def count_adjacent_mines(grid, row, col):
    mine_count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
                if grid[r][c] == '*':
                    mine_count += 1
    return mine_count

"Проверка"

def open_cell(grid, revealed, row, col):
    if grid[row][col] == '*':
        return False
    if revealed[row][col]:
        return True

    revealed[row][col] = True
    adjacent_mines = count_adjacent_mines(grid, row, col)

    if adjacent_mines == 0:

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
                    open_cell(grid, revealed, r, c)
    return True
"Проверка"

def print_grid(grid, revealed):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if revealed[row][col]:
                if grid[row][col] == '*':
                    print('*', end=' ')
                else:
                    print(count_adjacent_mines(grid, row, col), end=' ')
            else:
                print('-', end=' ')
        print()

"Проверка"

def check_win(grid, revealed):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] != '*' and not revealed[row][col]:
                return False
    return True

def play_game():
    grid = create_grid()
    grid = place_mines(grid)
    revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    print("'Сапер'!")
    print("размещены 5 мин")
    print("клетки без мин \n")

    while True:
        print_grid(grid, revealed)

        try:
            row, col = map(int, input("(строка): ").split())
            if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
                print("Попробуйте снова")
                continue
        except ValueError:
            print("снова")
            continue

        if not open_cell(grid, revealed, row, col):
            print("попали на мину")
            break

        if check_win(grid, revealed):
            print("oткрыли клетки")
            break

if __name__ == "__main__":
    play_game()


#####################################################################