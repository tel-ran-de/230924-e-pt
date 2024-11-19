# Игра:Викторина
#
# Создайте игру "Викторина", где пользователю задаются 5 вопросов с вариантами ответов.
# После выбора варианта ответ выводится, правильный ли был сделан выбор.
# В конце игры выводится общее количество правильных ответов.
#
# Столица Франции?
# — 1. Лондон
# — 2. Берлин
# — 3. Париж
#
# Столица Германии?
# — 1. Лондон
# — 2. Берлин
# — 3. Венеция
#
# Столица США?
# — 1. Нью-Йорк
# — 2. Лос-Анджелес
# — 3. Вашингтон
#
# Столица Греции
# — 1. Афины
# — 2. Стамбул
# — 3. Киев
#
# Столица Норвегии
# — 1. Осло
# — 2. Порту
# — 3. Мюнхен


def ask_question(question, options, correct_answer):

    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    answer = input("номер ответа: ")

    if answer.isdigit() and int(answer) == correct_answer:
        print("Правильно!\n")
        return True
    else:
        print(f"Н: {correct_answer}. {options[correct_answer - 1]}\n")
        return False


def run_quiz():

    questions = [
        {
            "question": "Столица Франции?",
            "options": ["Лондон", "Берлин", "Париж"],
            "correct_answer": 3
        },
        {
            "question": "Столица Германии?",
            "options": ["Лондон", "Берлин", "Венеция"],
            "correct_answer": 2
        },
        {
            "question": "Столица США?",
            "options": ["Нью-Йорк", "Лос-Анджелес", "Вашингтон"],
            "correct_answer": 3
        },
        {
            "question": "Столица Греции?",
            "options": ["Афины", "Стамбул", "Киев"],
            "correct_answer": 1
        },
        {
            "question": "Столица Норвегии?",
            "options": ["Осло", "Порту", "Мюнхен"],
            "correct_answer": 1
        }
    ]

    score = 0


    for q in questions:
        correct = ask_question(q["question"], q["options"], q["correct_answer"])
        if correct:
            score += 1


    print(f"\n {score}")


if __name__ == "__main__":
    run_quiz()

#################################################################################################