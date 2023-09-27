"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча
и выводит на стандартный вывод сводную таблицу результатов всех матчей. За победу команде начисляется 3 очка,
за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Порядок вывода команд произвольный.
"""

number = int(input())
Dict = {}
team = "team"
games, wins, draw, defeat, ball = 0, 0, 0, 0, 0
for x in range(number):
    str1 = input()
    lst = str1.split(";")
    for i in range(len(lst)):
        if lst[i].isdigit():
            if i == 3:
                if int(lst[i - 2]) > int(lst[i]):
                    Dict[lst[i - 1]][0] += 1
                    Dict[lst[i - 3]][0] += 1
                    Dict[lst[i - 1]][3] += 1
                    Dict[lst[i - 3]][4] += 3
                    Dict[lst[i - 3]][1] += 1
                elif int(lst[i - 2]) < int(lst[i]):
                    Dict[lst[i - 1]][0] += 1
                    Dict[lst[i - 3]][0] += 1
                    Dict[lst[i - 1]][1] += 1
                    Dict[lst[i - 1]][4] += 3
                    Dict[lst[i - 3]][3] += 1
                else:
                    Dict[lst[i - 1]][0] += 1
                    Dict[lst[i - 3]][0] += 1
                    Dict[lst[i - 1]][2] += 1
                    Dict[lst[i - 1]][4] += 1
                    Dict[lst[i - 3]][2] += 1
                    Dict[lst[i - 3]][4] += 1
            else: pass
        else:
            if lst[i] in Dict:
                 pass
            else:
                Dict[lst[i]] = [games, wins, draw, defeat, ball]
                team = lst[i]
for key, value in Dict.items():
    print((key + ':'), *value, end='\n')