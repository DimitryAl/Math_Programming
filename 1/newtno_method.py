from prettytable import PrettyTable

from functions import gradient, norm, function

table = PrettyTable()
table.field_names = ["k", "x", "f(x)", "||gradient(f(x))||"]

def matrix_multi(x, y):  # умножение гессиана на градиент
    res = [0, 0, 0]
    res[0] = x[0][0] * y[0] + x[0][1] * y[1] + x[0][2] * y[2]
    res[1] = x[1][0] * y[0] + x[1][1] * y[1] + x[1][2] * y[2]
    res[2] = x[2][0] * y[0] + x[2][1] * y[1] + x[2][2] * y[2]
    return res


def method_newton():
    step = 0
    eps = 0.001
    grad = []        # значение градиента
    invert_h = [[0.174, 0.0449, -0.0112],        # обратная матрица гесса
         [0.0449, 0.27, -0.0674],
         [-0.0112, -0.0674, 0.517]]

    x0 = [0, 0, 0]          # начальное приближение
    x = [0, 0, 0]
    # ищем градиент от начального приближения
    grad = gradient(x0)
    table.add_row([step, x.copy(), function(x), norm(grad)])

    multi = matrix_multi(invert_h, grad)
    for i in range(3):
        x[i] = x0[i] - multi[i]
    step += 1
    grad = gradient(x)
    table.add_row([step, x, function(x), norm(grad)])
    while norm(gradient(x)) >= eps:
        x0 = x.copy()
        grad = gradient(x0)
        multi = matrix_multi(invert_h, grad)
        for i in range(3):
            x[i] = x0[i] - multi[i]
        step += 1
        table.add_row([step, x.copy(), function(x), norm(gradient(x))])
    print(table)
    return
