import random

def minesweeper():
    size = 5
    num_mines = 5
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines = random.sample(range(size * size), num_mines)
    for mine in mines:
        row, col = divmod(mine, size)
        board[row][col] = '✹'

    revealed = [[False for _ in range(size)] for _ in range(size)]

    def count_mines(row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < size and 0 <= c < size and board[r][c] == '✹':
                count += 1
        return count

    def reveal_board(row, col):
        if not (0 <= row < size and 0 <= col < size) or revealed[row][col]:
            return
        revealed[row][col] = True
        if board[row][col] == '✹':
            return
        count = count_mines(row, col)
        if count > 0:
            board[row][col] = str(count)
        else:
            board[row][col] = ' '
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                reveal_board(row + dr, col + dc)

    def print_board():
        for row in range(size):
            for col in range(size):
                if revealed[row][col]:
                    print(board[row][col], end=' ')
                else:
                    print('.', end=' ')
            print()

    def print_board_with_mines():
        for row in range(size):
            for col in range(size):
                if board[row][col] == '✹':
                    print('✹', end=' ')
                else:
                    print(board[row][col], end=' ')
            print()

    while True:
        print_board()
        try:
            user_row, user_col = map(int, input("Введите координаты клетки (например, '2 3'): ").split())
            if not (1 <= user_row <= size and 1 <= user_col <= size):
                print("Неверные координаты. Попробуйте снова.")
                continue
            row, col = user_row - 1, user_col - 1  # Преобразование координат из диапазона 1-5 в 0-4
        except ValueError:
            print("Неверный ввод. Попробуйте снова.")
            continue

        if board[row][col] == '✹':
            print("Вы наступили на мину! Игра окончена.")
            print_board_with_mines()
            break

        reveal_board(row, col)

        if sum(sum(row) for row in revealed) == size * size - num_mines:
            print("Поздравляю! Вы открыли все клетки без мин и победили!")
            print_board_with_mines()
            break

if __name__ == "__main__":
    minesweeper()
