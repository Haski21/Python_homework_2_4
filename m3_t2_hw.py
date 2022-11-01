"""
Строка из нескольких слов, не более 10.
Определите, сколько букв содержит самое длинное слово в строке.
Пример:
In: Как дела в учебе
Out: 5
"""

first_str = input('Input str:')
FOO = 0
TEMP = 0

for i in range(len(first_str)):
    if first_str[i] == ' ' or first_str[i] == ',' or first_str[i] == '.':
        TEMP = 0
    else: TEMP += 1
    if FOO <= TEMP:
        FOO = TEMP
print('the biggest word is:',FOO)
