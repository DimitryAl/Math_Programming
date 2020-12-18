from prettytable import PrettyTable

def table_output(cons ,b, z, text):
    table = PrettyTable()
    table.field_names = ["y1", "y2", "s1", "s2", "s3", "s4", 'r1', 'r2', "b"]
    print(text)
    for i in range(len(cons)):
        table.add_row([cons[i][0], cons[i][1], cons[i][2], cons[i][3], cons[i][4], cons[i][5], cons[i][6], cons[i][7], b[i]])
    table.add_row([z[0], z[1], z[2], z[3], z[4], z[5], z[6], z[7], b[len(b) - 1]])
    print(table)


def dual(cons, z, b):
    print('Решение двойственной задачи')
    
    for i in range(len(z)):
        z[i] = -z[i]
    
    print('Матрица коэффициентов')
    k = 0
    for i in cons:
        for j in i:
            print(j ,end ='\t') 
        print(b[k])
        k += 1
    for i in z:
        print(i, end ='\t')    
    
    print('\nТранспонированная матрица коэффицентов')
    t_matrix = [[], [], []]
    for i in range(2):
        for j in range(4):
            t_matrix[i].append(cons[i][j])
    for i in range(4):
        t_matrix[2].append(z[i])
    for i in range(3):
        if i >= len(b) - 1:
            t_matrix[i].append(None)
        else:
            t_matrix[i].append(b[i])  
    for i in range(5):
        for j in range(3):
            if t_matrix[j][i] != None:
                print(t_matrix[j][i], end="\t")
        print()
    
    print('\nЦелевая функция: Z = 7y1 + 13y2  -> min')
    print('Ограничения:')
    print('y1 + 2y2 >= 1\ny1 >= -2\ny2 >= 2\ny1 - y2 >= -1\n')
    print('Вводим балансовые переменные:')
    print('y1 + 2y2 - s1 >= 1\n-y1 + s2 <= 2\ny2 - s3 >= 2\n-y1 + y2 +s4 <= 1\n')
    
    print('Базиса нет => вводим искусственные переменные, где нет базисной переменной')
    print('y1 + 2y2 - s1 + r1>= 1\n-y1 + s2 <= 2\ny2 - s3 + r2>= 2\n-y1 + y2 +s4 <= 1')
    print('r1, r2 >= 0')
    print('Z = 7y1 + 13y2 + 0s1 + 0s2 + 0s3 + 0s4 + 0r1 + 0r2')
    print('Начальный базис: s2, s4, r1, r2\n')
    '''
    print('Введем в рассмотрение функцию W и будем искать ее наименьшее значение.\nW = r1 + r2')
    print('W = (1- y1 - 2y2 + s1) + r2 = 1 - y1 - 2y2 + s1 + r2')
    print('W = 1 - x1 -2x2 + s1 + (2 - x2 + s3) = 3 - x1- 3x2 + s1 + s3')
    print('Приравниваем свободные переменные к нулю; Наименьшее W = 3')
    '''
    cons = [[1, 2, -1, 0, 0, 0, 1, 0],
            [-1, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, -1, 0, 0, 1],
            [-1, 1, 0, 0, 0, 1, 0, 0]
            ]
    b = [1, 2, 2, 1, -3]
    z = [-1, -3, 1, 0, 1, 0, 0, 0]

    table_output(cons, b, z, 'Начальная симплекс таблица:')

    basis = [False] * len(z)
    basis[3] = True
    basis[5] = True
    basis[6] = True
    basis[7] = True
    letters = ['y1', 'y2', 's1', 's2', 's3', 's4','r1', 'r2',]
    print('Текущий базис:', end='\t')
    for i in range(len(basis)):
        if basis[i]:
            print(letters[i], end=' ')
    print()
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
        # ищем опорную столбец
        min_number = z[0]
        min_column = 0
        for i in range(len(z)):
            if z[i] < min_number:
                min_number = z[i]
                min_column = i
        # ищем опорный строку
        min_row = -1
        for i in range(len(cons)):
            xi = cons[i][min_column]
            if xi == 0:
                continue
            if xi < 0:
                continue
            if min_row == -1:
                b_min = b[i] / xi
                min_row = i
            else:
                if (b[i] / xi) < b_min:
                    b_min = b[i] / xi
                    min_row = i
        #меняем базиз
        basis[min_column] = True
        for i in range(len(cons[min_row])):
            if cons[min_row][i] == 1 and basis[i] == True and i != min_column:
                basis[i] = False

        # делаем так чтобы опорный элемент равнялся единице
        divider = cons[min_row][min_column]
        for i in range(len(cons[min_row])):
            cons[min_row][i] = cons[min_row][i] / divider
        b[min_row] = b[min_row] / divider
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
        # вывод базиса
        print('Текущий базис:', end='\t')
        for i in range(len(basis)):
            if basis[i]:
                print(letters[i], end=' ')
        print()

    table_output(cons, b, z, 'Конечная симплекс таблица:')
    print('Конечный базис:', end='\t')
    for i in range(len(basis)):
        if basis[i]:
            print(letters[i], end=' ')
    print()
    for i in range(len(cons)):
        for j in range(len(cons[min_row])):
            if cons[i][j] == 1 and basis[j] == True:
                basis[j] = b[i]
    for i in range(len(basis)):
        if basis[i]:
            print(letters[i], '=', basis[i])
    print('\nОтвет: ', end="")
    print(f'Z = {7*basis[0]+13*basis[1]}')
    print('\n')
