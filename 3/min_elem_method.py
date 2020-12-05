
import copy
from prettytable import PrettyTable


def min_search(n, cur_min, tar):
    new_min = tar[0][0]
    for i in range(n):
        for j in range(n):
            if tar[i][j] > new_min:
                new_min = tar[i][j]
    for i in range(n):
        for j in range(n):
            if (tar[i][j] < new_min and tar[i][j] > cur_min):
                new_min = tar[i][j]
    
    return new_min

def min_elem(tariffs, stocks, needs, n):
    step = 0
    comp = 0
    new_tar = copy.deepcopy(tariffs)
    for i in range(n):
        for j in range(n):
            new_tar[i][j] = 0
    new_stocks = stocks.copy()
    new_needs = needs.copy()

    table = PrettyTable()
    table.field_names = [" ", "B1", "B2", "B3", "B4", "Запасы"]
    print('Матрица тарифов')
    for i in range(n):
        table.add_row(['A' + str(i + 1), tariffs[i][0], tariffs[i][1], tariffs[i][2], tariffs[i][3], stocks[i]])
    table.add_row(['Потребности', needs[0], needs[1], needs[2], needs[3], ''])
    print(table)

    # начальное заполнение
    min_tar = -1
    while True:
        min_tar = min_search(n, min_tar, tariffs)
        for i in range(n):
            for j in range(n):
                if tariffs[i][j] == min_tar:
                    if (new_stocks[i] or new_needs[j]) == 0:
                        continue
                    if new_stocks[i] - new_needs[j] >= 0:
                        c = new_needs[j]
                        new_stocks[i] = new_stocks[i] - new_needs[j]
                        new_needs[j] = 0
                    else:
                        c = new_stocks[i]
                        new_needs[j] = new_needs[j] - new_stocks[i]
                        new_stocks[i] = 0
                    new_tar[i][j] = c
                comp += 1

        print('min =', min_tar)
        table = PrettyTable()
        table.field_names = [" ", "B1", "B2", "B3", "B4", "Запасы"]
        for i in range(n):
            table.add_row(['A' + str(i + 1), new_tar[i][0], new_tar[i][1], new_tar[i][2], new_tar[i][3], new_stocks[i]])
        table.add_row(['Потребности', new_needs[0], new_needs[1], new_needs[2], new_needs[3], ''])
        print(table)

        zero = 0
        for i in range(n):
            zero += new_needs[i]
        if zero == 0:
            break 
    
    # проверка на оптимальность методом потенциалов
    print('\nПроверка на оптимальность методом потенциалов')
    while True:
        step += 1
        print('\nШаг' + str(step))
        u = [None for i in range(n)]
        v = [None for i in range(n)]
        u[0] = 0            # задаем начальное значение одному из потенциалов
        while (None in u) or (None in v):
            for i in range(n):
                for j in range(n):
                    if new_tar[i][j] != 0:
                        if u[i] != None:
                            v[j] = tariffs[i][j] - u[i]
                        elif v[j] != None:
                            u[i] = tariffs[i][j] - v[j]
        
        table = PrettyTable()
        table.field_names = [" ", "B1", "B2", "B3", "B4", "u"]
        for i in range(n):
            table.add_row(['A' + str(i+1), new_tar[i][0], new_tar[i][1], new_tar[i][2], new_tar[i][3], u[i]])
        table.add_row(['v', v[0], v[1], v[2], v[3], ''])
        print(table)

        # оценка незадействованных маршрутов
        min_delta = 0
        print('Оценка незадейственных маршрутов')
        for i in range(n):
            for j in range(n):
                if new_tar[i][j] == 0:
                    delta = tariffs[i][j] - (u[i] + v[j])
                    print('Δ'+str(i+1)+str(j+1), ' = ', delta)
                    if min_delta == 0 and delta < 0:
                        min_delta = delta
                        delta_i = i
                        delta_j = j
                    if delta < min_delta :
                        min_delta = delta
                        delta_i = i
                        delta_j = j
        if min_delta < 0:
            print('Минимальная Δ = ', min_delta, ' в клетке A' + str(delta_i+1)+'B'+str(delta_j+1))
        if min_delta == 0:
            print('Δ меньше нуля нет, следовательно оптимальное решение найдено:')
            table = PrettyTable()
            table.field_names = [" ", "B1", "B2", "B3", "B4"]
            for i in range(n):
                table.add_row(['A' + str(i+1), new_tar[i][0], new_tar[i][1], new_tar[i][2], new_tar[i][3]])
            table.add_row(['Потребности', new_needs[0], new_needs[1], new_needs[2], new_needs[3]])
            print(table)
            break

        # находим цикл для ячейки с отрицательной дельтой
        coordinates = [(-1,-1) for i in range(4)]
        coordinates[0] = (delta_i, delta_j)
        flag = False
        for i in range(n):
            if i != delta_i and new_tar[i][delta_j] != 0:
                for j in range(n):
                    if j != delta_j and new_tar[delta_i][j] != 0:
                        if new_tar[i][j] != 0:
                            coordinates[1] = (i, delta_j)
                            coordinates[2] = (i, j)
                            coordinates[3] = (delta_i, j)
                            flag = True
                    if flag:
                        break
            if flag:
                break
        print('Цикл по клеткам:\t', end='')
        for i in range(n):
            print('A'+str(coordinates[i][0]+1)+'B'+str(coordinates[i][1]), end='')    
            if i != n-1:
                print(', ', end='')
        # находим наимегьшую перевозку
        if new_tar[coordinates[1][0]][coordinates[1][1]] < new_tar[coordinates[3][0]][coordinates[3][1]]:
            min_value = new_tar[coordinates[1][0]][coordinates[1][1]]
        else:
            min_value = new_tar[coordinates[3][0]][coordinates[3][1]]
        for i in range(4):
            if i % 2 == 0:
                new_tar[coordinates[i][0]][coordinates[i][1]] = new_tar[coordinates[i][0]][coordinates[i][1]] + min_value
            if i % 2 == 1:
                new_tar[coordinates[i][0]][coordinates[i][1]] = new_tar[coordinates[i][0]][coordinates[i][1]] - min_value

        print('\nНовое решение:')
        table = PrettyTable()
        table.field_names = [" ", "B1", "B2", "B3", "B4", "u"]
        for i in range(n):
            table.add_row(['A' + str(i+1), new_tar[i][0], new_tar[i][1], new_tar[i][2], new_tar[i][3], u[i]])
        table.add_row(['v', v[0], v[1], v[2], v[3], ''])
        print(table)

    # подсчет минимальной затраты на перевозку
    S = 0
    
    print('Затраты на перевозку:')
    print('S = ', end='')
    for i in range(n):
        for j in range(n):
            if new_tar[i][j] != 0:
                S += new_tar[i][j] * tariffs[i][j] 
                print(str(new_tar[i][j])+'*'+str(tariffs[i][j]), end='')
                if (i, j) != (n-1, n-1):
                    print(' + ',end='')
    print(' =', S)
    print('Проверок на оптимальность на оптимальность = ', step)
    print('Количество сравнений при начальном заполнении = ', comp)