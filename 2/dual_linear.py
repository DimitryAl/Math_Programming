
#https://cbom.atozmath.com/CBOM/Simplex.aspx?q=pd&q1=4%602%60MAX%60Z%60x1%2cx2%2cx3%2cx4%601%2c-2%2c2%2c-1%601%2c1%2c0%2c1%3b2%2c0%2c1%2c-1%60%3d%2c%3d%607%2c13%60%60D%60false%60true%60false%60true%60false%60false%60true&do=1#PrevPart
#https://math.semestr.ru/simplex/msimplex.php
#https://math.semestr.ru/simplex/lec_dvoistven.php

def dual():
    print('Решение двойственной задачи')
    
    print('Матрица коэффициентов')
    print('1\t1\t0\t1\t7')
    print('2\t0\t1\t-1\t13')
    print('1\t-2\t2\t-1')
    print('Транспонированная матрица коэффицентов')
    print('1\t2\t1\n1\t0\t-2\n0\t1\t2\n1\t-1\t-1\n7\t13')
    print('Целевая функция: Z = 7y1 + 12y2  -> min')
    print('Ограничения:')
    print('y1 + 2y2 >= 1\ny1 >= -2\ny2 >= 2\ny1 - y2 >= -1\ny1,y2 - любое')
    print('Составим матрицу из компонентов векторов, входящих в оптимальный базис:')
    print('1\t0\n-1\t1')
    print('Определяем обратную матрицу:')
    print('1\t0\n1\t1')