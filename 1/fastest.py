from prettytable import PrettyTable


from functions import gradient, norm, function, mint


table = PrettyTable()
table.field_names = ["k", "x", "f(x)", "||gradient(f(x))||"]


def fastest():
    eps = 0.001
    x = [0, 0, 0]
    step = 0
    grad = gradient(x)
    table.add_row([step, x, function(x), norm(grad)])

    while norm(grad) >= eps:
        t = mint(-10, 10, 0.01, x)
        for i in range(3):
            x[i] = x[i] - t * grad[i]
        step += 1
        grad = gradient(x)
        table.add_row([step, x, function(x), norm(grad)])
    print(table)
    return
