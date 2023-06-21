import random
import binascii
import md4gen

def gcd(a, b):  
    while a != 0:
        a, b = b % a, a
    return b

def findModReverse(e, n):#扩展欧几里得算法
    if gcd(e, n) != 1:
        return None
    u1, u2, u3 = 1, 0, e
    v1, v2, v3 = 0, 1, n
    while v3 != 0:
        q = u3 // v3  
        u1, u2, u3, v1, v2, v3 = v1, v2, v3, (u1 - q * v1), (u2 - q * v2), (u3 - q * v3)
    return u1 % n

def rsa_oaep_encrypt(plaintext, public_key, n):#OAEP加密
    
    r = ""
    for i in range(1024):
        r += str(random.randint(0, 1))

    pad_paintext = binascii.hexlify(plaintext.encode('utf8'))#将明文转换为16进制

    mark_r = str(hex(int(r, 2)))#将随机数r转换为16进制
    P1 = md4gen.MD4(mark_r.encode()).hexdigest()#MD4哈希
    P1 = str(hex(int(P1, 16) ^ int(pad_paintext, 16)))#异或运算,进行填充

    mark_r = P1
    P2 = md4gen.MD4(mark_r.encode()).hexdigest()#MD4哈希
    P2 = str(hex(int(P2, 16) ^ int(r, 2)))#异或运算
    P1 = P1 + P2[2:]#拼接
    xx = int(P1, 16)#转换为10进制
    
    mul_pq = n
    Ey = int(pow(xx, public_key, mul_pq))#使用pow函数进行快速幂运算
    return hex(Ey)
'''
    将密文ciphertext转换为十进制形式。
    使用RSA私钥指数private_key对密文进行快速幂运算，并对结果取模n，得到解密结果Ex。
    将解密结果Ex转换为二进制形式。
    从二进制结果中分别取出后1024位和前1024位，表示为deP2和deP1。
    将deP1作为标记值，使用MD4哈希函数进行哈希运算，得到哈希值demark_P1。
    将demark_P1和deP2进行异或运算，得到demark_r。
    将demark_r作为新的标记值，再次使用MD4哈希函数进行哈希运算，得到哈希值demark_P1。
    将deP1和demark_P1进行异或运算，得到最终的明文。
    将最终的明文转换为UTF-8编码形式的字符串。
    返回解密结果。
'''
def rsa_oaep_decrypt(ciphertext,private_key,n):#OAEP解密
    Ex = int(pow(int(ciphertext,16), private_key, n))#使用pow函数进行快速幂运算
    deS = bin(Ex)#转换为二进制
    deP2 = hex(int(deS[len(deS) - 1024:], 2))#取后1024位
    deP1 = hex(int(deS[:len(deS) - 1024], 2))#取前1024位

    demark_r = deP1
    demark_P1 = md4gen.MD4(demark_r.encode()).hexdigest()#MD4哈希
    demark_r = str(hex(int(demark_P1, 16) ^ int(deP2, 16)))#异或运算
    demark_P1 = md4gen.MD4(demark_r.encode()).hexdigest()#MD4哈希
    Last_M = str(hex(int(deP1, 16) ^ int(demark_P1, 16)))#异或运算
    #返回解密结果
    return binascii.a2b_hex(Last_M[2:]).decode("utf8")#将16进制转换为明文



