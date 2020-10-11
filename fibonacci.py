def fibonacci(num):
    if num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    elif num >= 2:
        l = [1, 1]
        for _ in range(2, num):
            # 将列表最后两项的值求和，将值添加到列表最后
            l.append(l[-2] + l[-1])
        return l


print(fibonacci(4))
