# Игра "Анаграммы" (anagrams.py)
#
# Игроку дается слово, и он должен составить из его букв как можно больше других слов за одну минуту.
# Слова должны содержаться в JSON файле. В каждом слове не менее 5 букв.
# Для каждой игры рандомно выбирается слово и выводится пользователю.
#
# Далее происходит отсчет одной минуты (не отображается в консоле).
# В это время пользователь должен через запятую вводить слова, состоящие из тех же букв, что и заданное слово.
# По истечению одной минуты программа проверяет ввод пользователя по следующим параметрам:
#
# - Придуманные пользователем слова не дублируют заданное слово;
# - Придуманные слова уникальны;
# - Придуманные слова состоят из тех же букв, что и заданное слово.
#
# Программа засчитывает только те слова, которые соответствуют критериям выше.
# Как результат игры программа выводит: заданное слово, количество засчитанных слов, придуманных пользователем,
# сами засчитанные слова, не засчитанные слова.
# Эта же информация, плюс дата и время начала и окончания игры должна записываться в лог-файл.
# Добавьте обработку ошибок с использованием `try/except`, где это необходимо.