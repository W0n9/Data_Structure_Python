def newton(function, function1, start):
    x_n = start
    while True:
        x_n1 = x_n - function(x_n) / function1(x_n)  # 递归式
        if abs(x_n - x_n1) < 10**-5:
            return x_n1
        x_n = x_n1


def f(x):
    return (x**3) - 2 * x - 5


def f1(x):
    return 3 * (x**2) - 2


def intersection(function, start1, start2):
    # function 是 f(x),start1,start2 是区间端点
    x_n = start1
    x_n1 = start2
    while True:
        x_n2 = x_n1 - (function(x_n1) / ((function(x_n1) - function(x_n)) /
                                         (x_n1 - x_n)))  # 导数定义
        if abs(x_n2 - x_n1) < 10**-5:
            return x_n2
        x_n = x_n1
        x_n1 = x_n2


if __name__ == "__main__":
    print(newton(f, f1, 3))
    print(intersection(f, 3, 3.5))
