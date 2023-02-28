# user_letter = input('Введите букву: ')
# count = 0
# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     for letter in text:
#         if letter == user_letter:
#             count += 1
#
# print(count)

"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
"""

some_list = [9, 8, 7, 6]

summ = 1
with open('file.txt', 'r', encoding='utf-8') as file:
    text = file.read().splitlines()
    for ind in text:
        summ *= some_list[int(ind)]

    print(summ)


from random import randint
n = int(input('Введите кол-во элементов в списке: '))
some_list = [randint(-n, n) for _ in range(n)]
print(some_list)

with open('les8test.txt', 'w', encoding='utf-8') as file:
    for _ in range(randint(1, n)):
        file.write(str(randint(0, n - 1)) + '\n')

with open('les8test.txt', 'r', encoding='utf-8') as file:
    mult = 1
    for ind in file.read().splitlines():
        mult *= some_list[int(ind)]
print(mult)