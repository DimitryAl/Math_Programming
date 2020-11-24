import math


def function(x):    # возвращает значение функции в точке
    res = 3*x[0]**2 + 2*x[1]**2 + x[2]**2 - x[0]*x[1] + (x[1]*x[2])/2 + 6*x[1]
    return res


def gradient(x):    # возвращает грандент функции в точке
    g1 = 6*x[0] - x[1]
    g2 = 4*x[1] - x[0] + x[2]/2 + 6
    g3 = 2*x[2] + x[1]/2
    return [g1, g2, g3]


def norm(p):    # возвращает значение нормы вектора
    n = 0
    for i in range(3):
        n += p[i]**2
    n = math.sqrt(n)
    return n


def g(x, alpha):
    new_x = [0, 0, 0]
    grad = gradient(x)
    for i in range(3):
        new_x[i] = x[i] - alpha * grad[i]
    res = function(new_x)
    return res


def mint(a0, b0, eps, x):   # поиск минимального шага методом половинного деления
    k = 0
    lk = 0
    mk = 0
    delta = 0.5*eps
    x_ = 0
    ak = a0
    bk = b0
    k = 1

    lk = (ak + bk - delta) / 2
    mk = (ak + bk + delta) / 2
    k += 1
    if g(x, lk) <= g(x, mk):
        bk = mk
    else:
        ak = lk

    while (bk - ak) >= eps:
        lk = (ak + bk - delta) / 2
        mk = (ak + bk + delta) / 2
        k += 1
        if g(x, lk) <= g(x, mk):
            bk = mk
        else:
            ak = lk
    x_ = (ak + bk)/2
    return x_


def der1(x):    # Возвращает значение производной по x1
    return 6*x[0] - x[1]


def der2(x):    # Возвращает значение производной по x2
    return 4*x[1] - x[0] + 0.5*x[2] + 6


def der3(x):    # Возвращает значение производной по x3
    return 2*x[2] + 0.5*x[1]


def derivatives(x, k):
    derivative = {0: der1(x), 1: der2(x), 2: der3(x)}
    der = derivative[k]
    return der


def seidel(x, alpha, e, k):
    new_x = [0, 0, 0]
    der = derivatives(x, k)
    for i in range(3):
        new_x[i] = x[i] - alpha * der * e[i]
    res = function(new_x)
    return res


def mint2(a0, b0, eps, x, e, k):    # поиск минимального шага в методе гаусса - зейделя
    k = 0
    lk = 0
    mk = 0
    delta = 0.5*eps
    x_ = 0
    ak = a0
    bk = b0
    k = 1

    lk = (ak + bk - delta) / 2
    mk = (ak + bk + delta) / 2
    k += 1
    if seidel(x, lk, e, k) <= seidel(x, mk, e, k):
        bk = mk
    else:
        ak = lk

    while (bk - ak) >= eps:
        lk = (ak + bk - delta) / 2
        mk = (ak + bk + delta) / 2
        k += 1
        if g(x, lk) <= g(x, mk):
            bk = mk
        else:
            ak = lk

    x_ = (ak + bk)/2
    return x_