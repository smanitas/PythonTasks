"""
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит
равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
На вход программе подаётся строка из шести цифр.
Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
"""

a, b, c, d, e, f = input()
sum1= int(a)+int(b)+int(c)
sum2= int(d)+int(e)+int(f)
if sum1==sum2:
    print ('Счастливый')
else:
    print ('Обычный')