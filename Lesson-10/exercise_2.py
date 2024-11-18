# Тема: Цикл for
#
#
# Напишите программу, которая принимает строку от пользователя и подсчитывать количество гласных букв (a, e, i, o, u)
# в этой строке.Используйте цикл for и условие if.

word=input('Введите слово:')
i=0
for letter in word:
    a=list('aeiou')
    if letter in a:
        i +=1
        print(i)

# вместо чисел, кратных как 3, так и 5. Используйте цикл for и функцию range.


for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# вместо чисел, кратных как 3, так и 5. Используйте цикл for и функцию range.

