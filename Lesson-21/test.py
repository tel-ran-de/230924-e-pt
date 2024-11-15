import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Константы
DEFAULT_BOARD_SIZE = 10
DEFAULT_NUM_MINES = 15

class Minesweeper:
    def __init__(self, root):
        self.root = root
        self.root.title("Сапёр")

        self.board_size = DEFAULT_BOARD_SIZE
        self.num_mines = DEFAULT_NUM_MINES

        self.create_menu()
        self.start_new_game()

    # Создаем меню
    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        game_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Игра", menu=game_menu)
        game_menu.add_command(label="Новая игра", command=self.start_new_game)
        game_menu.add_command(label="Выбрать размер поля", command=self.choose_board_size)
        game_menu.add_separator()
        game_menu.add_command(label="Выход", command=self.root.quit)

    # Начинаем новую игру
    def start_new_game(self):
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.mines = set()
        self.flags = set()

        self.create_board()
        self.create_buttons()

    # Выбор размера поля
    def choose_board_size(self):
        size = simpledialog.askinteger("Размер поля", "Введите размер поля (от 5 до 20):", minvalue=5, maxvalue=20)
        if size:
            self.board_size = size
            self.num_mines = max(5, size * size // 6)
            self.start_new_game()

    # Создаем игровое поле с минами
    def create_board(self):
        while len(self.mines) < self.num_mines:
            x, y = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
            self.mines.add((x, y))

        for x, y in self.mines:
            self.board[x][y] = '*'

    # Подсчёт мин вокруг клетки
    def count_adjacent_mines(self, x, y):
        count = 0
        for i in range(max(0, x-1), min(self.board_size, x+2)):
            for j in range(max(0, y-1), min(self.board_size, y+2)):
                if self.board[i][j] == '*':
                    count += 1
        return count

    # Создаем кнопки на игровом поле
    def create_buttons(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        for i in range(self.board_size):
            for j in range(self.board_size):
                button = tk.Button(self.root, width=2, height=1, command=lambda x=i, y=j: self.reveal_cell(x, y))
                button.bind("<Button-3>", lambda event, x=i, y=j: self.toggle_flag(x, y))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    # Открываем клетку
    def reveal_cell(self, x, y):
        if (x, y) in self.flags or self.buttons[x][y]['text'] == 'F':
            return

        if self.board[x][y] == '*':
            self.game_over(False)
            return

        count = self.count_adjacent_mines(x, y)
        if count > 0:
            self.buttons[x][y].config(text=str(count), state='disabled', disabledforeground='blue', relief=tk.SUNKEN, bg='lightgray')
        else:
            self.buttons[x][y].config(text='', state='disabled', relief=tk.SUNKEN, bg='lightgray')
            # Открываем соседние клетки, если нет мин вокруг
            for i in range(max(0, x-1), min(self.board_size, x+2)):
                for j in range(max(0, y-1), min(self.board_size, y+2)):
                    if self.buttons[i][j]['state'] != 'disabled':
                        self.reveal_cell(i, j)

        self.check_victory()

    # Устанавливаем или снимаем флажок
    def toggle_flag(self, x, y):
        if self.buttons[x][y]['state'] == 'disabled':
            return

        if (x, y) in self.flags:
            self.buttons[x][y].config(text='')
            self.flags.remove((x, y))
        else:
            self.buttons[x][y].config(text='F', fg='red')
            self.flags.add((x, y))

    # Проверяем победу
    def check_victory(self):
        opened_cells = sum(self.buttons[i][j]['state'] == 'disabled' for i in range(self.board_size) for j in range(self.board_size))
        if opened_cells == self.board_size * self.board_size - self.num_mines:
            self.game_over(True)

    # Обработка конца игры
    def game_over(self, victory):
        for x, y in self.mines:
            self.buttons[x][y].config(text='*', fg='black', bg='red')
        message = "Вы победили!" if victory else "Вы проиграли!"
        messagebox.showinfo("Игра окончена", message)
        self.start_new_game()

# Запуск игры
if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()
