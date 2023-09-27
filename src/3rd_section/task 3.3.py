"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках
указываются эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
"""

d = int(input())
known_words = set(input().lower() for i in range(d))
l = int(input())
text = set(input().lower() for i in range(l))

errors = set()
for line in text:
    for word in line.split():
        if word not in known_words:
            errors.add(word)
for error in errors:
    print(error)