from sympy import symbols
from sympy.core.function import diff


def f(x):
    return x**3 - 2 * x - 5


def f1(func):
    x = symbols("x")
    return diff(func, x)


def newton(function, function1, start):
    x_n = start
    while True:
        x_n1 = x_n - function(x_n) / function1(function).evalf(
            subs={'x': x_n})  # 递归式
        if abs(x_n - x_n1) < 10**-5:
            return x_n1
        x_n = x_n1


if __name__ == "__main__":
    print(newton(f, f1, 3))
