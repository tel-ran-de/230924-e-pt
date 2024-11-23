# Игра "Скорость печати" (print_speed.py)
#
# Программа запрашивает имя и фамилию пользователя. Затем производит обратный отсчет в консоле: 3, 2, 1, “поехали”.
# Далее выводит задание: Напечатай фрагмент текста из 180 символов: “какое-то предложение”.
# Пользователь печатает в консоль фрагмент текста и нажимает enter.
# Программа проверяет, есть ли во вводе ошибки и замеряет скорость печати.
# Выводит результат:
# - имя, фамилию;
# - фрагмент текста, который нужно было записать;
# - ввод пользователя;
# - есть ошибки или нет (то есть полностью ли совпадает ввод пользователя и фрагмент текста);
# - время, потраченное пользователем на ввод.
#
# Эта же информация, плюс дата и время начала и окончания игры должна записываться в лог-файл.
# Фрагменты текста для печати берутся в рандомном порядке из файла. То есть для каждой попытки из файла
# выбирается какой-то участок текста на 180 символов (включая пробелы) и выдается пользователю.
#
# Добавьте обработку ошибок с использованием `try/except`, где это необходимо.