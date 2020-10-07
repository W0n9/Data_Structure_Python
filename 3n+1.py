def function(num):
    if num == 1:
        mylist.append(num)
        return mylist, len(mylist) - 1
    if (num % 2 == 0):
        mylist.append(num)
        return function(num // 2)
    else:
        mylist.append(num)
        return function(3 * num + 1)


if __name__ == "__main__":
    mylist = []
    print(function(43))

# def function(num):
#     mylist = [num]
#     while num != 1:
#         # 如果为奇数
#         if num % 2 == 1:
#             num = 3 * num + 1
#             mylist.append(num)
#         # 为偶数
#         else:
#             num = num // 2
#             mylist.append(num)
#     return mylist, len(mylist) - 1

# print(function(43))