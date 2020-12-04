#http://cyclowiki.org/wiki/%D2%F0%E0%ED%F1%EF%EE%F0%F2%ED%E0%FF_%E7%E0%E4%E0%F7%E0#.D0.A0.D0.B5.D1.88.D0.B5.D0.BD.D0.B8.D0.B5_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BF.D0.BE.D1.80.D1.82.D0.BD.D0.BE.D0.B9_.D0.B7.D0.B0.D0.B4.D0.B0.D1.87.D0.B8_.D0.BC.D0.B5.D1.82.D0.BE.D0.B4.D0.BE.D0.BC_.D0.BF.D0.BE.D1.82.D0.B5.D0.BD.D1.86.D0.B8.D0.B0.D0.BB.D0.BE.D0.B2
#https://math.semestr.ru/transp/index.php



# начальное условие
#           40  85  105 .
#       75  5   11  3   7
#       80  4   2   15  3
# c =   60  3   14  5   11
#       130 9   4   6   2

from prettytable import PrettyTable
from nw_angle import nwangle

n = 4                           # размерность матрицы тарифов
stocks = [75, 80, 60, 130]      # запасы
needs = [40, 85, 105, '.']     # потребности
tariffs = [  [5, 11, 3, 7],     # матрица тарифов
            [4, 2, 15, 3],
            [3, 14, 5, 11],
            [9, 4, 6, 2]]

table = PrettyTable()
table.field_names = [" ", "B1", "B2", "B3", "B4", "Запасы"]
print('Матрица тарифов')
for i in range(n):
    table.add_row(['A' + str(i + 1), tariffs[i][0], tariffs[i][1], tariffs[i][2], tariffs[i][3], stocks[i]])
table.add_row(['Потребности', needs[0], needs[1], needs[2], needs[3], ''])
print(table)

# делаем задачу закрытой
A = 0
B = 0
for i in range(n):
    if stocks[i] != '.':
        A += stocks[i]
    if needs[i] != '.':
        B += needs[i]
if A != B:
    needs[needs.index('.')] = A - B
print('ΣA =', A, 'ΣB =', B, 'ΣA - ΣB =', A-B)
print('Вместо точки в условии подставляем ', A-B)

print('1)Метод северо-западного угла')
print('2)Метод наименьшей стоимости')

m = input('Выберете метод:\t')

if m == '1':
    nwangle(tariffs, stocks, needs, n)
#if m == '2':
    #min_elem(tariffs, stocks, needs)