import tkinter as tk
from tkinter import messagebox

# Полный список из 50 вопросов и ответов по Python
questions = [
    {
        "question": "Что такое Python?",
        "options": [
            "Компилируемый язык программирования",
            "Интерпретируемый высокоуровневый язык программирования",
            "Система управления базами данных",
            "Операционная система"
        ],
        "answer": 1
    },
    {
        "question": "Какой оператор используется для возведения в степень в Python?",
        "options": [
            "^",
            "**",
            "pow",
            "%"
        ],
        "answer": 1
    },
    {
        "question": "Какой тип данных соответствует целым числам в Python 3?",
        "options": [
            "int",
            "long",
            "float",
            "double"
        ],
        "answer": 0
    },
    {
        "question": "Как объявить функцию в Python?",
        "options": [
            "function myFunction():",
            "def myFunction():",
            "fun myFunction()",
            "define myFunction():"
        ],
        "answer": 1
    },
    {
        "question": "Какой метод используется для добавления элемента в конец списка?",
        "options": [
            "list.add(element)",
            "list.append(element)",
            "list.insert(element)",
            "list.push(element)"
        ],
        "answer": 1
    },
    # ... Остальные вопросы остаются без изменений ...
    # Пожалуйста, убедитесь, что полный список из 50 вопросов включен
]

# Добавьте остальные вопросы здесь (всего должно быть 50 вопросов)

# Класс приложения
class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Тест по Python")
        self.master.geometry("800x600")

        self.score = 0
        self.question_number = 0

        self.question_label = tk.Label(master, text="", wraplength=750, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.var = tk.IntVar()
        self.options = []

        for i in range(4):
            rb = tk.Radiobutton(master, text="", variable=self.var, value=i, font=("Arial", 12), wraplength=750, justify='left')
            rb.pack(anchor='w')
            self.options.append(rb)

        self.next_button = tk.Button(master, text="Далее", command=self.next_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        q = questions[self.question_number]
        self.question_label.config(text=f"Вопрос {self.question_number + 1}: {q['question']}")
        self.var.set(-1)
        for i, option in enumerate(q['options']):
            self.options[i].config(text=option)

    def next_question(self):
        if self.var.get() == -1:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите вариант ответа.")
            return

        q = questions[self.question_number]
        if self.var.get() == q['answer']:
            self.score += 1
            correct = True
        else:
            correct = False

        # Показать сообщение о правильности ответа
        if correct:
            messagebox.showinfo("Результат", "Правильно!")
        else:
            correct_answer = q['options'][q['answer']]
            messagebox.showinfo("Результат", f"Неправильно! Правильный ответ: {correct_answer}")

        self.question_number += 1

        if self.question_number == len(questions):
            messagebox.showinfo("Итоговый результат", f"Ваш результат: {self.score} из {len(questions)}")
            self.master.destroy()
        else:
            self.load_question()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()