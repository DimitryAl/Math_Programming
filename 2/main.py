# 9 вариант
# z = x1 - 2x2 + 2x3 - x4 -> extr
# x1 + x2 + x4 = 7
# 2x1 + x3 - x4 = 13
# xi >= 0

from simplex_method import simplex

print('Исходные данные:')
print('z = x1 -2x2 + 2x3 - x4 -> extr')
print('x1 + x2 + x4 = 7\n2x1 + x3 - x4 = 13\nxi >= 0')


print('\n1)Симплекс метод')
print('2)Двойственная задача\n')

n = int(input())

if n == 1:
    print('Решение задачи симплекс методом\n')
    simplex()


print('done')