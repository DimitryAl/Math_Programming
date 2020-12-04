import copy


def check(i, j, stocks, needs, new_tar):
    cnt = 0
    for k in range(len(new_tar[i])):
        if new_tar[i][k] == 0:
            if needs[k] != 0:
                if stocks[i] != 0:
                    if stocks[i] >= needs[k]:
                        c = needs[k]
                        stocks[i] = stocks[i] - needs[k]
                        needs[k] = 0
                        new_tar[i][k] = c
                    else:
                        c = stocks[i]
                        needs[k] = needs[k] - stocks[i]
                        stocks[i] = 0
                        new_tar[i][k] = c
        if (i, k) != (i, j):
            cnt += 1
    for k in range(len(new_tar[k])):
        if new_tar[k][j] == 0:
            if needs[j] != 0:
                if stocks[k] != 0:
                    if stocks[k] >= needs[j]:
                        c = needs[j]
                        stocks[k] = stocks[k] - needs[j]
                        needs[j] = 0
                        new_tar[k][j] = c
                    else:
                        c = stocks[k]
                        needs[j] = needs[j] - stocks[k]
                        stocks[k] = 0
                        new_tar[k][j] = c 
        if (k, j) != (i, j):
            cnt += 1

def nwangle(tariffs, stocks, needs, n):
    step = 0
    new_tar = copy.deepcopy(tariffs)
    for i in range(n):
        for j in range(n):
            new_tar[i][j] = 0
    new_stocks = stocks.copy()
    new_needs = needs.copy()

    #while True:
    # начальное заполнение 
    for i in range(n):
        for j in range(n):
            if i == j:
            #if new_tar[i][j] == None:
                if new_stocks[i] - new_needs[j] >= 0:
                    c = new_needs[j]
                    new_stocks[i] = new_stocks[i] - new_needs[j]
                    new_needs[j] = 0
                else:
                    c = new_stocks[i]
                    new_needs[j] = new_needs[j] - new_stocks[i]
                    new_stocks[i] = 0
                new_tar[i][j] = c 
                check(i, j, new_stocks, new_needs, new_tar)
    # проверка на оптимальность методом потенциалов
    while True:
        step += 1
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
        # оценка незадействованных маршрутов
        min_delta = 0
        # мб  не искать минимальную, а брать первую
        for i in range(n):
            for j in range(n):
                if new_tar[i][j] == 0:
                    delta = tariffs[i][j] - (u[i] + v[j])
                    if min_delta == 0 and delta < 0:
                        min_delta = delta
                        delta_i = i
                        delta_j = j
                    if delta < min_delta :
                        min_delta = delta
                        delta_i = i
                        delta_j = j
        if min_delta == 0:
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

    for i in new_tar:
        print(i)
    


    print('done')
