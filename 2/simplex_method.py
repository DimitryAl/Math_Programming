from prettytable import PrettyTable

def table_output(cons ,b, z, text):
    table = PrettyTable()
    table.field_names = ["x1", "x2", "x3", "x4", "x5", "x6", "b"]
    print(text)
    for i in range(len(cons)):
        table.add_row([cons[i][0], cons[i][1], cons[i][2], cons[i][3], cons[i][4], cons[i][5], b[i]])
    table.add_row([z[0], z[1], z[2], z[3], z[4], z[5], b[len(b) - 1]])
    print(table)

def simplex(cons, z, b):
    #print('Решение задачи симплекс методом\n')
    #print('Будем искать max')

    cons[0].append(1)
    cons[0].append(0)
    cons[1].append(0)
    cons[1].append(1)
    z.append(0)
    z.append(0)
    
    '''
    print('Задача в канонической форме:')
    print('x1 + x2 + x4 + x5 = 7')
    print('2x1 + x3 - x4 + x6 = 13')
    print('z - x1 + 2x2 - 2x3 + x4 = 0')
    print('xi >= 0')
    '''

    table_output(cons, b, z, 'Начальная симплекс таблица:')
    step = 0
    while True:
        step += 1
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
            if b[i] / xi < 0:
                continue
            if min_row == -1:
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
        for i in range(len(cons)):
            if i == min_row:
                continue
            factor = cons[i][min_column] / cons[min_row][min_column]
            for j in range(len(cons[min_row])):
                a = cons[min_row][j] * factor
                cons[i][j] = cons[i][j] - a
            b[i] = b[i] - b[min_row] * factor
        factor = z[min_column] / cons[min_row][min_column]
        for i in range(len(z)):
            z[i] = z[i] - cons[min_row][i] * factor
        b[len(b) - 1] = b[len(b) - 1] - b[min_row] * factor
        table_output(cons, b, z, 'Шаг {}:'.format(step))


    basis = [0] * len(z)
    for i in range(len(z)):
        if z[i] == 0:
            basis[i] = True
    for i in range(len(cons)):
        for j in range(len(cons[min_row])):
            if cons[i][j] == 1 and basis[j] == True:
                basis[j] = b[i]
    table_output(cons, b, z, 'Конечная симплекс таблица:')
    print('Базис:')
    print('Ответ: ', end="")
    print('z(max) = z({},{},{},{}) = {}'.format(basis[0], basis[1], basis[2], basis[3], b[len(b) - 1]))
    print('\n')
