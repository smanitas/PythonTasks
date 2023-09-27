"""
Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
"""

a = int(input())
b = int(input())
c = int(input())
if c <= a >= b and b >= c:
    print(a,'\n', c, '\n', b)
elif c <= a >= b and c >= b:
    print(a, '\n', b, '\n', c)
elif c >= a <= b and b >= c:
    print(b, '\n', a, '\n', c)
elif c >= a <= b and b <= c:
    print(c, '\n', a, '\n', b)
elif a >= c <= b and b >= a:
    print(b, '\n', c, '\n', a)
else:
    print(c, '\n', b, '\n', a)