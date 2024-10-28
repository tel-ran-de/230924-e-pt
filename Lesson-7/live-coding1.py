# длина строки
print('длина строки')
just_str = '230924-e-pt'
print(len(just_str))
print()

# конкатенация строк
print('конкатенация строк')
str1 = 'Hello'
str2 = 'World'
result_concat = str1 + ' ' + str2 + '!'
print(result_concat)
print()

# повторение строк
print('повторение строк')
str3 = 'Hello'
result_repeat = str3 * 3
print(result_repeat)
print()

# нельзя складывать строку и число
# str4 = 'Python'
# number = 3
# res = str4 + number
# TypeError: can only concatenate str (not "int") to str

# индексация строк
print('индексация строк')
hello_str = 'Hello'
# H - [0] или [-5]
# o - [4] или [-1]
second_chr = hello_str[1]
second_last_chr = hello_str[-2]
print(second_chr, second_last_chr)
print()


# срезы (slice)
print('срезы (slice)')
str_for_slice = 'Python Programming!'
last_chr = str_for_slice[-1]
print(last_chr)  # !
slice_7_to_end = str_for_slice[7:]
print(slice_7_to_end)  # Programming
slice_start_to_3 = str_for_slice[:3]
print(slice_start_to_3)
# срезы задаются так [x:y]
# где x начало среза (включительно)
#   а y это конец среза (не включительно)
third_ind = 3
ninth_ind = 9
print(str_for_slice[third_ind:ninth_ind])
# можно использовать одновременно положительные и отрицательные срезы
print(str_for_slice[2:-5])

reversed_str = str_for_slice[::-1]
print(reversed_str)
reversed_str1 = str_for_slice[7:1:-1]
print(reversed_str1)
str_only_even = str_for_slice[0::2]
print(str_only_even)
str_only_odd = str_for_slice[1::2]
print(str_only_odd)