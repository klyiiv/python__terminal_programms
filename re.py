"""Рубанова А.Д. Регулярные выражения"""
import re

# 1
s1 = 'aaa--bbb==ccc__ddd'
result1 = re.split(r'--|==|__', s1)
print(result1)

"""Регулярное выражение --|==|__ разделяет строку по символам "--", "==", "__".
Функция re.split() возвращает список, содержащий разделенные элементы строки"""

# 2
s2 = 'Yesterday, All my troubles seemed so far away'

first_word = re.match(r'\b\w+\b', s2).group()
print(first_word)

"""Регулярное выражение \b\w+\b ищет последовательность символов,
которая состоит из одного или более словесных символов (\w+),
ограниченных границами слова (\b)
Функция re.match() ищет соответствие регулярному выражению в начале строки,
и с помощью метода .group() мы получаем найденное соответствие"""

# 3
s3 = 'Yesterday, All my troubles seemed so far away'

last_word = re.findall(r'\b\w+\b', s3)[-1]
print(last_word)

"""Регулярное выражение \b\w+\b ищет последовательность символов, которая состоит из одного или более словесных символов (\w+), ограниченных границами слова (\b)
Функция re.findall() ищет все соответствия регулярному выражению в строке и возвращает список
Используя индекс [-1], мы получаем последний элемент этого списка, который является последним словом строки"""

# 4

s4 = "В этом же отрывке найти первое слово каждой строки"
gl_words = re.findall(r'\b[аеёиоуыэюя]\w+', s4, re.IGNORECASE)
print(gl_words)

""""В данном случае, регулярное выражение \b[аеёиоуыэюя]\w+ ищет слова, которые начинаются с гласной буквы (любой из [аеёиоуыэюя]) и содержат один или более символов (\w+)
Флаг re.IGNORECASE делает поиск регистронезависимым, чтобы учесть как заглавные, так и строчные гласные буквы
Функция re.findall() ищет все соответствия регулярному выражению в строке и возвращает список найденных слов"""


# 5

s5 = "В этом же отрывке найти первое слово каждой строки\nПроверить корректность введенного E-mail\nВ следующей строке найти все email-адреса и вывести только доменные имена"

first_words = re.findall(r'^\w+', s5, re.MULTILINE)
print(first_words) 

"""Р егулярное выражение ^\w+ ищет последовательность символов, которая состоит из одного или более словесных символов (\w+),
в начале каждой строки (^) при использовании флага re.MULTILINE
Функция re.findall() ищет все соответствия регулярному выражению в тексте и возвращает список найденных первых слов каждой строки"""