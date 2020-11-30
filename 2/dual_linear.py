
#https://cbom.atozmath.com/CBOM/Simplex.aspx?q=pd&q1=4%602%60MAX%60Z%60x1%2cx2%2cx3%2cx4%601%2c-2%2c2%2c-1%601%2c1%2c0%2c1%3b2%2c0%2c1%2c-1%60%3d%2c%3d%607%2c13%60%60D%60false%60true%60false%60true%60false%60false%60true&do=1#PrevPart
#https://math.semestr.ru/simplex/msimplex.php
#https://math.semestr.ru/simplex/lec_dvoistven.php
# https://linprog.com/en/main-dual-simplex/result;queryParams=%7B%22n%22:2,%22m%22:4,%22max_min%22:1,%22values%22:%5B%5B%221%22,%222%22,%220%22,%221%22,%227%22%5D,%5B%222%22,%220%22,%221%22,%22-1%22,%2213%22%5D%5D,%22function%22:%5B%221%22,%22-2%22,%222%22,%22-1%22%5D,%22equalSign%22:%5B1,1%5D%7D

def dual(cons, z, b):
    print('Решение двойственной задачи')
    
    print('Матрица коэффициентов')
    print(cons[0], b[0])
    print(cons[1], b[1])
    print(z)    
    print('Транспонированная матрица коэффицентов')
    for i in range(len(cons[0])):
        print(cons[0][i], cons[1][i], z[len(z) - 1 - i])
    print(b[0], b[1])
    
    print('Целевая функция: Z = 7y1 + 12y2  -> min')
    print('Ограничения:')
    print('y1 + 2y2 >= 1\ny1 >= -2\ny2 >= 2\ny1 - y2 >= -1\ny1,y2 - любое')
    '''
    print('Составим матрицу из компонентов векторов, входящих в оптимальный базис:')
    print('1\t0\n-1\t1')
    print('Определяем обратную матрицу:')
    print('1\t0\n1\t1')
    '''