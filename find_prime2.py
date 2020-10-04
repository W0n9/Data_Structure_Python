import math


def find_prime_2(num):
    primes_bool = [False, False] + [True] * (num - 1)
    for i in range(3, len(primes_bool)):
        # 将数组下标是偶数的数字全部置为否定状态
        if i % 2 == 0:
            primes_bool[i] = False
    for i in range(3, int(math.sqrt(num)) + 1):
        # 如果当前数字处于被肯定的状态，则将其倍数的数字状态置为否定
        # 大小相辅，取根号可以令判断次数折半
        if primes_bool[i] is True:
            for j in range(i + i, num + 1, i):
                primes_bool[j] = False
    prims = []
    # enumerate 将 primes_bool 组合成一个索引序列，i 是索引，v 是元素
    for i, v in enumerate(primes_bool):
        #　将判断为 True 的元素添加进 prims
        if v is True:
            prims.append(i)
    return prims


print(find_prime_2(100))