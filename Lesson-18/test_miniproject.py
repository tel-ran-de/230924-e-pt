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
        for row in range(size):
            for col in range(size):
                if revealed[row][col]:
                    print(board[row][col], end=' ')
                else:
                    print('-', end=' ')
            print()

        try:
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

        if board[row][col] == '*':
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

        # Открытие клетки
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
    main_game_minesweeper()
