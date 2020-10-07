import hashlib
# hashlib简单使用


def md5(arg):
    # 这是加密函数，将传进来的函数加密
    md5_pwd = hashlib.md5(bytes('abd', encoding='utf-8'))
    md5_pwd.update(bytes(arg, encoding='utf-8'))
    # 返回加密的数据
    return md5_pwd.hexdigest()


def log(user, pwd):
    # 登录时候时候的函数，由于md5不能反解，因此登录的时候用正解
    with open('db', 'r', encoding='utf-8') as f:
        for line in f:
            u, p = line.strip().split('|')
            # 登录时候时候的函数，由于md5不能反解，因此登录的时候用正解
            if u == user and p == md5(pwd):
                return True


def register(user, pwd):
    # 注册的时候把用户名和加密的密码写进文件，保存起来
    with open('db', 'a', encoding='utf-8') as f:
        temp = user + '|' + md5(pwd)
        f.write(temp)


i = input('1表示登录，2表示注册：')
if i == '2':
    user = input('用户名：')
    pwd = input('密码：')
    register(user, pwd)
elif i == '1':
    user = user = input('用户名：')
    pwd = input('密码：')
    # 验证用户名和密码
    r = log(user, pwd)
    if r == True:
        print('登录成功')
    else:
        print('登录失败')
else:
    print('账号不存在')