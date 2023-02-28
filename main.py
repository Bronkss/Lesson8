"""
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на
печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
Протестируем функцию на файле «article.txt» со следующим содержимым:

Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела
"""

def read_last(lines, file):
    with open(file, encoding='utf-8') as file:
        for line in (file.readlines() [-lines:]):
            print(line, end='')

read_last(5, 'file.txt')

"""
Документ «article.txt» содержит следующий текст:

Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела

Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину 
(или список слов, если таковых несколько).
"""

# def longest_words(file):
#     with open(file, encoding='utf-8') as file:
#         while True:
#             if file == '':
#                 break
#             for letter in (file.readline().split()):
#                 print(int(len(letter)))
#                 print(max(len(letter)))
#
# longest_words('article.txt')

def longest_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        list_str = file.read().split()
        max_len = len(sorted(list_str, key=len, reverse=True)[0]) # нашёл вот такой способ
        print('максимальная длина строки =', max_len)

longest_words('article.txt')
