# работа с JSON

import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": True
}

# Запись в файл
with open("text_files/data.json", "w") as file:
    json.dump(data, file)

with open("text_files/data_human_readable.json", "w") as file:
    json.dump(data, file, indent=4)

# Чтение из файла
with open("text_files/data_for_read.json", "r") as file:
    data_alice = json.load(file)

print(data_alice)

# создание json-строки из словаря
json_string = json.dumps(data)
print(json_string)

# создание словаря из json-строки
data = json.loads(json_string)
print(data)