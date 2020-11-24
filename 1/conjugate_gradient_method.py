from prettytable import PrettyTable
import math
from functions import  norm, mint, function, gradient


table = PrettyTable()
table.field_names = ["k", "x", "f(x)", "||gradient(f(x))||"]

def func(q, w):
    for i in range(3):
        q[i] = q[i] - w[i]
    return q


def con_grad():
    eps = 0.001
    x = [0, 0, 0]
    x_prev = x.copy()
    k = 0
    d = [0, 0, 0]
    grad = gradient(x)
    
    table.add_row([k, x.copy(), function(x), norm(grad)])
    while norm(grad) >= eps:
        if k == 0:
           d[0] = -grad[0]
           d[1] = -grad[1]
           d[2] = -grad[2]  
        else:
            b = norm(gradient(x)) / norm(gradient(x_prev))
            
            for i in range(3):
                d[i] = -grad[i] + b * d[i]
        #t = mint(-10, 10, eps, func(x.copy(), d))
        t = mint(-10, 10, eps, x.copy())
        x_prev = x.copy()
        for i in range(3):
            x[i] = x[i] + t * d[i]
        grad = gradient(x)
        k = k + 1
        table.add_row([k, x.copy(), function(x), norm(grad)])
    print(table)
'''
def con_grad():
    step = 0
    eps = 0.001
    d = [0, 0, 0]
    x_prev = [10, 10, 10]
    x = [0, 0, 0]  # начальное приближение
    grad = gradient(x)   # считаем начальный градиент
    table.add_row([step, x.copy(), function(x), norm(grad)])

    t = mint(-10, 10, eps, x.copy())

    x_prev = x.copy()
    for i in range(3):
        d[i] = -grad[i]
        x[i] = x[i] + t * d[i]
    step += 1
    table.add_row([step, x.copy(), function(x), norm(grad)])
    while norm(gradient(x)) >= eps:
    #while math.fabs(function(x_prev) - function(x)) >= eps:
        # x_prev = x.copy()
        t = mint(-10, 10, eps, x.copy())

        grad = gradient(x)
        if step != 0:
            beta = norm(gradient(x))/norm(gradient(x_prev))
            d_prev = d.copy()
            for i in range(3):
                d[i] = -grad[i] + beta * d_prev[i]
            x_prev = x.copy()
            for i in range(3):
                x[i] = x[i] + t * d[i]
       
        step += 1
        table.add_row([step, x.copy(), function(x), norm(gradient(x))])
    print(table)
    return
'''

