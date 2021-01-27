# Sudoku solving algorithm
field = [list('100006032'),
         list('204000000'),
         list('006200005'),
         list('002501080'),
         list('030040000'),
         list('500820000'),
         list('000000000'),
         list('700100420'),
         list('000070061')]

def total_found():
    found = 81
    for row in field: found -= row.count('0')
    return found

# проверяет, может ли значение K стоять где-то кроме клетки с координатами [i,j]
def test_only(i, j, k):
    # проверить, есть ли возможность разместить K в альтернтаивной позиции. Если нет - вернуть True
    # суть алгоритма: если в горизонтали ИЛИ вертикали ИЛИ квадрате не нашлось другого места для K, вернём True
    result = False
    column_alternative = True
    line_alternative = True
    block_alternative = True
    for i1 in range(9):
        if (i != i1) and (field[i1][j] == '0'):                 # если это не сама проверяемая клетка и не заполненная клетка
            if k in test_not(i1,j): column_alternative = False  # если в этой клетке может быть К, проверка по вертикали не пройдена
        if (j != i1) and (field[i][i1] == '0'):                 # если это не сама проверяемая клетка и не заполненная клетка
            if k in test_not(i, i1): line_alternative = False   # если в ней может быть K, проверка по горизонтали не пройдена
        horiz_shift = (j // 3) * 3 + i1 % 3     # высчитываем проверяемую позицию в блоке 3х3
        vert_shift = (i // 3) * 3 + i1 // 3
        if ((i != vert_shift) or (j != horiz_shift)) and (field[vert_shift][horiz_shift] == '0'): # если это не проверяемая и пустая клетка
            res = test_not(vert_shift,horiz_shift)
            if k in res: block_alternative = False  # если в ней может быть K, проверка блока не пройдена
    if column_alternative or line_alternative or block_alternative:
        result = True  # если пройдена хотя ббы одна проверка на уникальность, вернем True
    return result

# для клетки с координатами [i,j] определяет возможные значения
def test_not(i, j):
    cur = list('123456789')
    for k in range(9):
        if (field[i][k] != '0'): cur[ord(field[i][k]) - 49] = '0'  # проход по вертикали
        if (field[k][j] != '0'): cur[ord(field[k][j]) - 49] = '0'  # проход по горизонтали
        # вычисление и проход по текущему квадрату 3х3
        horiz_shift = (j // 3) * 3 + k % 3
        vert_shift = (i // 3) * 3 + k // 3
        if (field[vert_shift][horiz_shift] != '0'): cur[ord(field[vert_shift][horiz_shift]) - 49] = '0'
    return ''.join(sorted(cur))

f = start_found = total_found()
prev_found = 0
while f < 81:
    for i in range (9):
        for j in range (9):
            if field[i][j] == '0':  # если клетка пустая, анализируем варианты
                cur = test_not(i, j)
                if cur.count('0') == 8: field[i][j] = cur[8]
                else:
                    for p in range(7,-1,-1):
                       if cur[p] != '0':
                            if test_only(i, j, cur[p]):
                                field[i][j] = cur[p]
    # считаем оставшиеся пустые клетки
    f = total_found()
    if f == prev_found:
        print (f'Сдаюсь! Смог заполнить только {f} значений при начально известных {start_found}')
        break
    prev_found = f
for i in range(9):
    print (field[i])

