from prettytable import PrettyTable

#https://cbom.atozmath.com/CBOM/Simplex.aspx?q=pd&q1=4%602%60MAX%60Z%60x1%2cx2%2cx3%2cx4%601%2c-2%2c2%2c-1%601%2c1%2c0%2c1%3b2%2c0%2c1%2c-1%60%3d%2c%3d%607%2c13%60%60D%60false%60true%60false%60true%60false%60false%60true&do=1#PrevPart
#https://math.semestr.ru/simplex/msimplex.php
#https://math.semestr.ru/simplex/lec_dvoistven.php
# https://linprog.com/en/main-dual-simplex/result;queryParams=%7B%22n%22:2,%22m%22:4,%22max_min%22:1,%22values%22:%5B%5B%221%22,%222%22,%220%22,%221%22,%227%22%5D,%5B%222%22,%220%22,%221%22,%22-1%22,%2213%22%5D%5D,%22function%22:%5B%221%22,%22-2%22,%222%22,%22-1%22%5D,%22equalSign%22:%5B1,1%5D%7D


def table_output(cons ,b, z, text):
    table = PrettyTable()
    table.field_names = ["y1", "y2", "s1", "s2", "s3", "s4", "b"]
    print(text)
    for i in range(len(cons)):
        table.add_row([cons[i][0], cons[i][1], cons[i][2], cons[i][3], cons[i][4], cons[i][5], b[i]])
    table.add_row([z[0], z[1], z[2], z[3], z[4], z[5], b[len(b) - 1]])
    print(table)


def simplex(cons, z, b):

    cons[0].append(1)
    cons[0].append(0)
    cons[0].append(0)
    cons[0].append(0)
    cons[1].append(0)
    cons[1].append(1)
    cons[1].append(0)
    cons[1].append(0)
    cons[2].append(0)
    cons[2].append(0)
    cons[2].append(1)
    cons[2].append(0)
    cons[3].append(0)
    cons[3].append(0)
    cons[3].append(0)
    cons[3].append(1)
    z.append(0)
    z.append(0)
    z.append(0)
    z.append(0)

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
    print('Базис: ', end ='')
    for i in range(len(basis)):
        if basis[i] != 0:
            print(f'x{i+1}', end = ',')
    print('\nОтвет: ', end="")
    print('z(min) = z({},{},{},{}) = {}'.format(basis[0], basis[1], basis[2], basis[3], b[len(b) - 1]))
    print('\n')



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
    
    cons = [[1,1], [-1, 0], [0, 1], [-1, 1]]
    z = [-7, -13]
    b =[1, 2, 2, 1, 0]
    simplex(cons, z, b)

