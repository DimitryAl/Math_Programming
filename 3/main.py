#http://cyclowiki.org/wiki/%D2%F0%E0%ED%F1%EF%EE%F0%F2%ED%E0%FF_%E7%E0%E4%E0%F7%E0#.D0.A0.D0.B5.D1.88.D0.B5.D0.BD.D0.B8.D0.B5_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BF.D0.BE.D1.80.D1.82.D0.BD.D0.BE.D0.B9_.D0.B7.D0.B0.D0.B4.D0.B0.D1.87.D0.B8_.D0.BC.D0.B5.D1.82.D0.BE.D0.B4.D0.BE.D0.BC_.D0.BF.D0.BE.D1.82.D0.B5.D0.BD.D1.86.D0.B8.D0.B0.D0.BB.D0.BE.D0.B2
#https://math.semestr.ru/transp/index.php

#           40  85  105 .
#       75  5   11  3   7
#       80  4   2   15  3
# c =   60  3   14  5   11
#       130 9   4   6   2
n = 4
stocks = [75, 80, 60, 130]
needs = [40, 85, 105, None]
matrix = [  [5, 11, 3, 7], 
            [4, 2, 15, 3],
            [3, 14, 5, 11],
            [9, 4, 6, 2]]

# проверка на открытость или закрытость
A = 0
B = 0
for i in range(n):
    if stocks[i] != None:
        A += stocks[i]
    if needs[i] != None:
        B += needs[i]

if A == B:
    print('Задача закрытая')
else:
    print('Задача открытая')
