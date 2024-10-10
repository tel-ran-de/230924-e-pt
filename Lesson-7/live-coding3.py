# спецсимволы и экранирование
# print('Let's go!')
print('Let\'s go!')
print("Let's go!")
# print(""Привет" - сказала она.")
print('"Привет" - сказала она.')
print("\"Привет\" - сказала она.")
# print("121\11=11")
print("121\\11=11")
print("13//5=2")
print('Hello\nworld!')
print('Hello\tworld!')

# форматирование строк: метод format()
name = 'Alex'
age = 27
greeting_format = "My name is {}, I'm {} years old".format(name, age)
print(greeting_format)

# форматирование строк: f-строки
greeting_f_string = f"My name is {name}, I'm {age} years old"
print(greeting_f_string)

username = input('Введите имя: ')
age = int(input('Введите возраст: '))
print(f'{username}, ты родился в {2024 - age} году.')
