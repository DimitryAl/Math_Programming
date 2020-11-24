from prettytable import PrettyTable

from functions import gradient, norm, function
from functions import mint, derivatives



table = PrettyTable()
table.field_names = ["k", "x", "f(x)", "||gradient(f(x))||"]

def gauss_seidel():
    n = 3
    eps = 0.001
    e = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    x = [0, 0, 0]
    j = 0
    table.add_row([j, x.copy(), function(x), norm(gradient(x))])
    while True:
        k = 0
        print(x)
        while k <= n - 1:
            grad = gradient(x)
            if norm(grad) < eps:
                print(table)
                return
            else:
                t = mint(-10, 10, eps, x.copy())
                for i in range(3):
                    x[i] = x[i] - t * derivatives(x,k)*e[k][i]
                k = k + 1 
        j = j + 1
        table.add_row([j, x.copy(), function(x), norm(gradient(x))])