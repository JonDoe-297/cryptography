import random
import math
from sys import exit
def fastExpMod(b, e, m): 
    result = 1
    e = int(e)
    while e != 0:
        if e % 2 != 0:
            e -= 1
            result = (result * b) % m
            continue
        e >>= 1
        b = (b * b) % m
    return result

def miller_rabin_test(n):  # p为要检验得数
    p = n - 1
    r = 0
    while p % 2 == 0:  # 最后得到为奇数的p(即m)
        r += 1
        p /= 2
    b = random.randint(2, n - 2)  # 随机取b=（0.n）
    # 如果情况1    b得p次方  与1  同余  mod n
    if fastExpMod(b, int(p), n) == 1:
        return True  # 通过测试,可能为素数
    # 情况2  b得（2^r  *p）次方  与-1 (n-1) 同余  mod n
    for i in range(0,7):  # 检验六次
        if fastExpMod(b, (2 ** i) * p, n) == n - 1:
            return True  # 如果该数可能为素数，
    return False  # 不可能是素数

def create_prime_num(keylength):
    while True:
        n = random.randint(0, keylength)
        if n % 2 != 0:
            found = True
            for i in range(0, 10):
                if miller_rabin_test(n):
                    pass
                else:
                    found = False
                    break
            if found:
                return n

def select_E(fn, halfkeyLength):
    while True:
        e = random.randint(0, fn)
        if math.gcd(e, fn) == 1:
            return e

def match_d(e, fn):
    d = 0
    while True:
        if (e * d) % fn == 1:
            return d
        d += 1

def create_keys(keylength):
    p = create_prime_num(keylength / 2)
    q = create_prime_num(keylength / 2)
    n = p * q
    fn = (p - 1)*(q - 1)
    e = select_E(fn, keylength / 2)
    d = match_d(e, fn)
    return (n, e, d)

def encrypt_file(mess):
    n, e, d = create_keys(1024)
    print("n:",n," ,d:",d)
    s = ''
    print(mess)
    for ch in mess:
        c = str(fastExpMod(ord(ch), e, n))
        s += c
    print(s)
    print("Encrypt Done!")

def decrypt_file(mess):
    n, d= map(int, input("输入您的私钥（n,d）:").split())
    s = ''

    for ch in mess:
        c = str(fastExpMod(ord(ch), d, n))
        s += c
    print(s)
    print("Decrypt Done!")

if __name__ =='__main__':
    way = input("1.加密\n2.解密\n")
    while way != '1' and way != '2':
        print("输入格式错误，请重新输入！")
        way = input("1.加密\n2.解密\n")
    if way == '1':
        plaintext = input("请输入明文：")
        encrypt_file(plaintext)
    elif way == '2':
        ciphertext = input("请输入密文：")
        decrypt_file(ciphertext)
