"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме
элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов
соседний элемент находится с противоположной стороны матрицы. В случае одной строки/столбца элемент
сам себе является соседом по соответствующему направлению.
"""

numbers = []
new_number = ''
while new_number != 'end':
    new_number = input()
    if new_number != 'end':
            numbers.append(list(map(int, str(new_number).split())))
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print((numbers[i - 1][j] + numbers[(i + 1) % len(numbers)][j] + numbers[i][j - 1] + numbers[i][(j + 1) % len(numbers[i])]), end=' ')
    print()