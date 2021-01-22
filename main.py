# Sudoku solving algorithm
field = [list('004860030'),
         list('001000090'),
         list('800009060'),
         list('500206001'),
         list('027001000'),
         list('000043006'),
         list('050000000'),
         list('009000400'),
         list('000400015')]

total_found = 0
prev_found = 0
while total_found < 81:
    for i in range (9):
        for j in range (9):
            if field[i][j] == '0':  # если клетка пустая, анализируем варианты
                cur = list('123456789')
                for k in range(9):
                    if (field[i][k]!='0'): cur[ord(field[i][k])-49]='0' # проход по вертикали
                    if (field[k][j]!='0'): cur[ord(field[k][j])-49]='0' # проход по горизонтали
                    # вычисление и проход по текущему квадрату 3х3
                    horiz_shift = (j//3)*3 + k // 3
                    vert_shift = (i//3)*3 + k % 3
                    if (field[vert_shift][horiz_shift]!='0'): cur[ord(field[vert_shift][horiz_shift])-49]='0'
                if cur.count('0') == 8: field[i][j] = ''.join(sorted(cur))[8]
    # считаем оставшиеся пустые клетки
    total_found = 81
    for row in field:
        total_found -= row.count('0')
    print (f'Заполнено: {total_found} клеток игрового поля')
    if total_found == prev_found:
        print ('Сдаюсь нахер!')
        break
    prev_found = total_found
for i in range(9):
    print (field[i])

