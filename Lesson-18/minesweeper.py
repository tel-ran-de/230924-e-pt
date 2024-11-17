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
import random

def main_game_minesweeper():
    size = 5
    max_mines = 5
    board = [['-' for _ in range(size)] for _ in range(size)]
    revealed = [[False] * size for _ in range(size)]
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Генерация мин
    count_mines = 0
    while count_mines < max_mines:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        if board[row][col] != '*':
            board[row][col] = '*'
            count_mines += 1

    print(47 * "-")
    print("Игра: Сапёр.")
    print(47 * "-")

    while True:
        for row in range(size): # Вывод игрового поля
            for col in range(size):
                if revealed[row][col]:
                    print(board[row][col], end=' ')
                else:
                    print('-', end=' ') # если revealed == False в клетке печатаем "-"
            print()

        try:    # проверка ввода пользователя
            print(47 * "-")
            user_input = input("Введите координаты клетки (строка столбец): ")
            print(47 * "-")
            user_row, user_col = user_input.split()
            user_row, user_col = int(user_row), int(user_col)
            if not (1 <= user_row <= size and 1 <= user_col <= size):
                print("Неверные координаты. Попробуйте снова.")
                continue
            row, col = user_row - 1, user_col - 1  # Преобразование координат из диапазона 1-5 в 0-4
        except ValueError:
            print("Неверный ввод. Попробуйте снова.")
            continue

        if board[row][col] == '*':  # проверка на мину
            print("Вы наступили на мину! Игра окончена.")
            for row in range(size):
                for col in range(size):
                    if board[row][col] == '*':
                        print('*', end=' ')
                else:
                        count = 0
                        for dr, dc in directions:
                            r, c = row + dr, col + dc
                            if 0 <= r < size and 0 <= c < size and board[r][c] == '*':
                                count += 1
                        if count > 0:
                            print(count, end=' ')
                        else:
                            print('-', end=' ')
                print()
            break

        # Открытие клетки, если есть вокруг мины, пишем их кол-во иначе пустая клетка " "
        queue = [(row, col)]
        while queue:
            r, c = queue.pop(0)
            if not (0 <= r < size and 0 <= c < size) or revealed[r][c]:
                continue
            revealed[r][c] = True
            if board[r][c] == '*':
                continue
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < size and 0 <= nc < size and board[nr][nc] == '*':
                    count += 1
            if count > 0:
                board[r][c] = str(count)
            else:
                board[r][c] = ' '
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < size and 0 <= nc < size and not revealed[nr][nc]:
                        queue.append((nr, nc))
        # все клетки без мин открыты - Победа
        if sum(sum(row) for row in revealed) == size * size - max_mines:
            print("Поздравляю! Вы победили!")
            for row in range(size):
                for col in range(size):
                    if board[row][col] == '*':
                        print('*', end=' ')
                    else:
                        count = 0
                        for dr, dc in directions:
                            r, c = row + dr, col + dc
                            if 0 <= r < size and 0 <= c < size and board[r][c] == '*':
                                count += 1
                        if count > 0:
                            print(count, end=' ')
                        else:
                            print('-', end=' ')
                print()
            break

if __name__ == "__main__":
    print('Файл запущен напрямую')
    main_game_minesweeper()
