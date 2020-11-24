
from gradient_s_drobleniem import droblenie
from fastest import fastest
from newtno_method import method_newton
from conjugate_gradient_method import con_grad
from gauss_seidel import gauss_seidel


print("Выбор задания:")
print("2)Градиентный спуск с дроблением шага")
print("3)Градиентный спуск с минимизацией по шагу")
print("4)Покоординатный спуск(метод Гаусса-Зейделя)")
print("5)Метод Ньютона")
print("6)Метод сопряженных градиентов(Флетчера - Ривса)")
print("0)exit")

number = int(input())

if number == 0:
    exit(0)
if number == 2:
    print("2)Градиентный спуск с дроблением шага")
    droblenie()
if number == 3:
    print("3)Градиентный спуск с минимизацией по шагу")
    fastest()
if number == 4:
    print("4)Покоординатный спуск(метод Гаусса-Зейделя)")
    gauss_seidel()
if number == 5:
    print("5)Метод Ньютона")
    method_newton()
if number == 6:
    print("6)Метод сопряженных градиентов(Флетчера - Ривса)")
    con_grad()
print('done')
