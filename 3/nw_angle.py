import copy


def check(i, j, stocks, needs, new_tar):
    cnt = 0
    '''
    if stocks[i] == 0:
        for k in new_tar[i]:
             if k == None:
                 k = 0
                 cnt += 1
    if needs[j] == 0:
        for k in range(len(new_tar)):
            if new_tar[k][j] == None:
                new_tar[k][j] = 0
                cnt += 1
    '''
    for k in range(len(new_tar[i])):
        if new_tar[i][k] == None:
            if needs[k] != 0:
                if stocks[i] != 0:
                    if stocks[i] >= needs[k]:
                        c = stocks[i] - needs[k]
                        stocks[i] = stocks[i] - needs[k]
                        needs[k] = 0
                        new_tar[i][k] = c
                    else:
                        c = needs[k] - stocks[i]
                        needs[k] = needs[k] - stocks[i]
                        stocks[i] = 0
                        new_tar[i][k] = c
    
    
    return cnt

def nwangle(tariffs, stocks, needs, n):
    
    cnt = 0                 # счетчик пройденных клеток
    min_tariff = 1          
    step = 0
    new_tar = copy.deepcopy(tariffs)
    for i in range(n):
        for j in range(n):
            new_tar[i][j] = None
    new_stocks = stocks.copy()
    new_needs = needs.copy()

    # составляем начальный план перевозок
    # заполняем северо-западный угол
    if new_stocks[0] - new_needs[0] >= 0:
        c = new_needs[0]
        new_stocks[0] = new_stocks[0] - new_needs[0]
        new_needs[0] = 0
    else:
        c = new_stocks[0]
        new_needs[0] = new_needs[0] - new_stocks[0]
        new_stocks[0] = 0
    new_tar[0][0] = c
    cnt += check(0, 0, new_stocks, new_needs, new_tar)
    cnt += 1
    step += 1
    # заполняем все остальное
    while True:
        while cnt != n*n:
            for i in range(n):
                for j in range(n):
                    if tariffs[i][j] == min_tariff:
                        if new_tar[i][j] == None:
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
            min_tariff += 1



#nwangle([],[],[],4)