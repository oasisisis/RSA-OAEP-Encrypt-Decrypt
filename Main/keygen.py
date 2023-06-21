from src.prime import get_prime
import src.modular_math as mod
from src.primitives import BASE64Decoding, BASE64Encode, tobytes, totuple, tostr
import random, os, sys

class RSAKey:
    def __init__(self, size=1024, p=0, q=0, e= 0, d = 0, modulus=0):
        #要生成的素数的长度
        self.size = size
        self._e = 0
        self._d = 0
        
        if e == 0 and d == 0:
            #选择两个不相等的质数p和q。
            self.p = get_prime(size)
            self.q = get_prime(size)
            #计算n = pq。
            self._n = self.p * self.q
            #计算欧拉函数
            self.phi = (self.p - 1) * (self.q-1)
            #寻找与n互质的整数e，且1 < e < φ(n)
            self._e = self.__generate_e()
            #计算e对于φ(n)的模反元素d
            self._d = self.__generate_d(self._e)
        


        #私钥由n和d组成
        elif e == 0 and ((d and modulus) != 0):
            self._d = d
            self._n = modulus
        #公钥由n和e组成
        elif d == 0 and ((e and modulus) !=0):
            self._e = e
            self._n = modulus
        

    @property
    def n(self):
        return int(self._n)

    @property
    def e(self):
        return int(self._e)
    @property
    def d(self):
        return int(self._d)

    @property 
    def public_key(self):
        if self._e != 0:
            return RSAKey(e=self._e, modulus=self._n, d =0)
        else:
            raise ValueError("This is a private key, you cant get the public one.")  

    @property 
    def private_key(self):
        if self._d != 0:
            return RSAKey(d=self._d, modulus=self._n, p = self.p, q = self.q, e=0) 
        else:
            raise ValueError("This is a public key, you cant get the private one.")  
 

    def get_key(self):#返回公钥或私钥，形式为(e,n)或(d,n)
        if self.isPublic():
            return (self.e, self.n)
        elif self.isPrivate():
            return (self.d, self.n)
        else:
            return ((self.e, self.n), (self.d, self.n))
    def isPublic(self):#判断是否为公钥
        if self._d == 0:
            return True
        return False
 
    def isPrivate(self):#判断是否为私钥
        if self._e == 0:
            return True
        return False
    
    def _size_in_bits(self):
        #返回n的二进制表示的位数
        return self._n.bit_length()

    def _size_in_bytes(self):
        #返回n的二进制表示的字节数
        return (self._n.bit_length()) // 8   

    
        

    def _encrypt(self, text):
        return pow(text, self.c, self.n)
    def _decrypt(self, cipher):
        if cipher > self.n:
            raise ValueError("Cipher too large")
        return pow(cipher, self.d, self.n)
    
    
    #生成新的密钥
    def __generate_e(self):
        while True:
            e = random.randrange(2**(self.size - 1), 2**(self.size))
            if mod.is_coprime(e, self.phi) and mod.is_coprime(e, self.n):
                return e
    def __generate_d(self, e): 
        return mod.find_mod_inverse(e, self.phi)

    def export_key(self):
        if not self.isPublic():            
            key_type = 'PRIVATE KEY'
            str = BASE64Encode(self.get_key(), key_type)
        else:
            key_type = "PUBLIC KEY"
            str = BASE64Encode(self.get_key(), key_type)
            

        return tobytes(str).decode('ascii')



def import_key(path) -> RSAKey:
    with open(path, 'r') as f:
        extern_key = f.read()
    
    key_type = get_key_type(extern_key)
    keys_string = BASE64Decoding(extern_key, key_type) 
    key = totuple(keys_string)
    if key_type == "PUBLIC KEY":
        e, modulus = key
        return RSAKey(e=e, modulus=modulus)
    else:
        d, modulus = key
        return RSAKey(d=d, modulus=modulus)

def get_key_type(extern_key):
    if "PUBLIC KEY" in extern_key:
        return "PUBLIC KEY"
    else:
        return "PRIVATE KEY"

def generate_key():
    bit_size = 1024
    bit_size =  int(bit_size)

    key_pairs = RSAKey(bit_size)
    pub_key = key_pairs.public_key
    prv_key = key_pairs.private_key
    
    return pub_key.get_key(), prv_key.get_key()

