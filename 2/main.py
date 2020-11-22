# 9 вариант
# z = x1 - 2x2 + 2x3 - x4 -> extr
# x1 + x2 + x4 = 7
# 2x1 + x3 - x4 = 13
# xi >= 0

print('Исходные данные:')
print('z = x1 -2x2 + 2x3 - x4 -> extr')
print('x1 + x2 + x4 = 7\n2x1 + x3 - x4 = 13\nxi >= 0')


cons = [[1, 1, 0, 1], [2, 0, 1, -1]] # initial ogranicheniya table
z = [-1, 2, -2, 1, 0, 0]  # initial function
b = [7, 13, 0]  # правые части

cons[0].append(1)
cons[0].append(0)
cons[1].append(0)
cons[1].append(1)

while True:
    # проверяем надо ли что-то делать
    sign = 1
    for i in range(len(z)): 
        if z[i] < 0:
            sign = -1
    if sign > 0:    
        break
    # ищем опорный столбец
    min_number = z[0]
    min_column = 0
    for i in range(len(z)):     
        if z[i] < min_number:
            min_number = z[i]
            min_column = i
    # ищем опорный элемент
    min_row = -1
    for i in range(len(cons)):        
        xi = cons[i][min_column]
        if xi == 0:
            continue
        if min_row == -1:
            if b[i] / xi < 0:
                continue
            b_min = b[i] / xi
            min_row = i
        else:
            if (b[i] / xi) < b_min:
                b_min = b[i] / xi
                min_row = i
    # делаем так чтобы опорный элемент равнялся нулю
    divider = cons[min_row][min_column]
    for i in range(len(cons[min_row])):
        cons[min_row][i] = cons[min_row][i] / divider
    # делаем так чтобы в опорном столбце были все нули кроме опорного элемента
    # ДОБАВИТЬ ВЕКТОР b И z
    for i in range(len(cons)):
        if i == min_row:
            continue
        factor = cons[i][min_column] / cons[min_row][min_column]
        for j in range(len(cons[min_row])):
            a = cons[min_row][j] * factor
            cons[i][j] = cons[i][j] - a
            z[i] = z[i] - a
        for k in range(len(b)):
            b[i] = b[i] - factor * b[min_row]
            

print(z)
print('done')