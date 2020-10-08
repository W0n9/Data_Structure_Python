flex = 10**-7


def function(x):
    return x**3 - 2 * x - 5


def function_slove(function, a, b):
    return function(a) * function(b)


def bisection(function, a, b):
    if abs(a - b) < flex:
        return a
    else:
        if function(a) == 0:
            return a
        elif function(b) == 0:
            return b
        elif function_slove(function, a, b) > 0:
            raise ValueError
        elif function_slove(function, a, (b + a) / 2) < 0:
            return bisection(function, a, (b + a) / 2)
        elif function_slove(function, (b + a) / 2, b) < 0:
            return bisection(function, (b + a) / 2, b)


print(bisection(function, 1, 1000))


# import math


# def bisection(function, a, b):  # 指定函数function,指定区间[a,b]
#     start = a
#     end = b
#     if function(a) == 0:  # a即为零点
#         return a
#     elif function(b) == 0:  # b即为零点
#         return b
#     elif function(a) * function(b) > 0:  # 二分法无法在该区间找到零点
#         print("couldn't find root in [a,b]")
#         return
#     else:  # f(a)*f(b)<0 的情况
#         mid = (start + end) / 2
#         while abs(start - mid) > 10**-7:  # 精确度设置为10**-7
#             if function(mid) == 0:
#                 return mid
#             elif function(mid) * function(start) < 0:
#                 end = mid
#             else:
#                 start = mid
#             mid = (start + end) / 2
#         return mid


# def f(x):
#     return math.pow(x, 3) - 2 * x - 5


# if __name__ == "__main__":
#     print(bisection(f, 1, 1000))