# 9 вариант
# z = x1 - 2x2 + 2x3 - x4 -> extr
# x1 + x2 + x4 = 7
# 2x1 + x3 - x4 = 13
# xi >= 0

from simplex_method import simplex
from dual_linear import dual
print('Исходные данные:')
print('z = x1 -2x2 + 2x3 - x4 -> extr')
print('x1 + x2 + x4 = 7\n2x1 + x3 - x4 = 13\nxi >= 0')

cons = [[1, 1, 0, 1], 
        [2, 0, 1, -1]]  # initial ogranicheniya table
z = [-1, 2, -2, 1]  # initial function
b = [7, 13, 0]  # правые части

print('\n1)Симплекс метод')
print('2)Двойственная задача\n')



while True:
    n = int(input())
    if n == 1:
        simplex(cons, z, b)
        break
    if n == 2:
        dual(cons, z, b)
        break
    if n == 12:
        simplex(cons, z, b)
        #dual()
        break
    print('Wrong number, try again')
print('\ndone')
