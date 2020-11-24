from prettytable import PrettyTable

from functions import gradient, norm, function

table = PrettyTable()
table.field_names = ["k", "x", "f(x)", "||gradient(f(x))||"]

def droblenie():
    eps = 0.001
    c = 0.25
    x = [0, 0, 0]
    x_new = x.copy()
    step = 0
    t = 2
    grad = gradient(x)
    table.add_row([step, x.copy(), function(x), norm(grad)])

    while norm(grad) >= eps:
        for i in range(3):
            x_new[i] = x[i] - t * grad[i]
        while function(x_new) >= function(x):
            t = c * t
            for i in range(3):
                x_new[i] = x[i] - t * grad[i]
        step += 1
        grad = gradient(x_new)
        x = x_new.copy()
        table.add_row([step, x.copy(), function(x), norm(grad)])
    print(table)
    return
