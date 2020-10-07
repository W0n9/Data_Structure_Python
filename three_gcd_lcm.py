from math import gcd


def three_gcd(a, b, c):
    return gcd(gcd(a, b), c)


def lcm(a, b):
    return a * b // gcd(a, b)


def three_lcm(a, b, c):
    return lcm(lcm(a, b), c)


if __name__ == "__main__":
    print(three_gcd(2, 7, 6))
    print(three_lcm(2, 7, 6))
