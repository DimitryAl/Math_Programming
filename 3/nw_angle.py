import copy


def check(i, j, stocks, needs, new_tar):
    cnt = 0
    for k in range(len(new_tar[i])):
        if new_tar[i][k] == None:
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
        #if new_tar[i][k] == None:
        #    new_tar[i][k] = 'Seen'
        if (i, k) != (i, j):
            cnt += 1
    for k in range(len(new_tar[k])):
        if new_tar[k][j] == None:
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
        #if new_tar[k][j] == None:
        #    new_tar[k][j] = 'Seen'
        if (k, j) != (i, j):
            cnt += 1
    return cnt

def nwangle(tariffs, stocks, needs, n):
    
    cnt = 0                 # счетчик пройденных клеток
    #min_tariff = 1          
    step = 0
    new_tar = copy.deepcopy(tariffs)
    for i in range(n):
        for j in range(n):
            new_tar[i][j] = None
    new_stocks = stocks.copy()
    new_needs = needs.copy()

    while True:
        # заполнение 
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
                    cnt += check(i, j, new_stocks, new_needs, new_tar)
                    cnt += 1
        # проверка на оптимальность методом потенциалов
        u = [None for i in range(n)]
        v = [None for i in range(n)]
        u[0] = 0            # задаем начальное значение одному из потенциалов
        for i in range(n):
             for j in range(n):
                if new_tar[i][j] != None:
                    if u[i] != None:
                        v[j] = tariffs[i][j] - u[i]
                    else:
                        u[i] = tariffs[i][j] - v[j]


        if (i, j) == (n-1, n-1):
            break

    print('done')
#nwangle([],[],[],4)