# Игра "Текстовый квест"
#
# За основу возьмите свой код, разработанный в предыдущем проектном уроке, посвященном Game Hub (урок 13).
# Если в тот раз вы не реализовали весь функционал, то сначала реализуйте полностью игру, а затем переходите
# к рефакторингу на основе заданий из этого урока.
#
# Рефакторинг
# - Добавить логирование начала и окончания игры и всех ходов игрока с временными метками (дата и время).
# - Добавить обработку ошибок с использованием `try/except`, где это необходимо.
# - Сюжет игры должен подгружаться из файла JSON.
# - Добавить сохранение и загрузку состояния игры с использованием файлов в формате JSON.
# Если программа была прервана по ходу игры, то пользователь при старте программы начинает с того же места.



# {
#     "start": {
#         "text": "Вы просыпаетесь в темной комнате. Куда вы пойдете?",
#         "choices": {
#             "1": "Открыть дверь",
#             "2": "Остаться и осмотреться"
#         }
#     },
#     "1": {
#         "text": "Вы открыли дверь и увидели длинный коридор.",
#         "choices": {
#             "1": "Идти по коридору",
#             "2": "Вернуться в комнату"
#         }
#     },
#     "2": {
#         "text": "Вы остались в комнате и нашли тайник с оружием.",
#         "choices": {
#             "1": "Использовать оружие",
#             "2": "Выйти из комнаты"
#         }
#     }
# }


import json
import os
import logging
from datetime import datetime


# Настройка логирования
logging.basicConfig(filename='game_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')


# Путь к файлам
STORY_FILE = 'game_story.json'
STATE_FILE = 'game_state.json'


# Загрузка сюжета игры
def load_story():
    try:
        with open(STORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Ошибка: файл с сюжетом не найден.")
        return {}
    except json.JSONDecodeError:
        print("Ошибка: проблема с форматом JSON.")
        return {}


# Загрузка состояния игры
def load_game_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Ошибка: проблема с форматом состояния игры.")
    return None


# Сохранение состояния игры
def save_game_state(current_scene):
    try:
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump({"current_scene": current_scene}, f)
        print("Состояние игры сохранено.")
    except Exception as e:
        print(f"Ошибка при сохранении состояния игры: {e}")



# Основной игровой цикл
def play_game():
    # Загрузка сюжета и состояния игры
    story = load_story()
    game_state = load_game_state()

    # Если состояния игры нет, начинаем с начала
    if game_state is None:
        current_scene = "start"
    else:
        current_scene = game_state['current_scene']

    logging.info(f"Игра началась. Стартовая сцена: {current_scene}")



    # Игровой процесс
    while True:
        # Вывод текста текущей сцены
        scene = story.get(current_scene, None)
        if scene is None:
            print("Игра завершена. Сюжет закончился.")
            logging.info("Игра завершена. Сюжет закончился.")
            break

        print(scene["text"])
        print("Ваши выборы:")
        for key, choice in scene["choices"].items():
            print(f"{key}. {choice}")



        # Ввод игрока
        try:
            user_choice = input("Выберите действие (цифра): ").strip()
            if user_choice not in scene["choices"]:
                raise ValueError("Некорректный выбор. Попробуйте снова.")
        except ValueError as e:
            print(e)
            continue



        # Логирование хода
        logging.info(f"Игрок выбрал: {scene['choices'][user_choice]}")

        # Обновляем текущую сцену
        current_scene = user_choice
        save_game_state(current_scene)

if __name__ == "__main__":
    print("Добро пожаловать в текстовый квест!")
    play_game()