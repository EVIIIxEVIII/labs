import random
import math

class RSA():
    def __init__(self):
        self.p = self.genPrime()
        self.q = self.genPrime()
        self.n = self.q * self.p
        self.r = (self.p - 1) * (self.q - 1)
        self.e = self.findE()
        self.d = self.findMultInv(self.e, self.r)

    def findE(self):
        e = 3
        while self.gcd(e, self.r) != 1:
            e += 2

        return e

    def gcd(self, a, b):
        while True:
            rem = a % b
            if rem == 0:
                return b
            a = b
            b = rem

    def findMultInv(self, a, b):
        x0, y0 = 1, 0
        x1, y1 = 0, 1
        modulus = b

        while b != 0:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1

        return (x0 % modulus + modulus) % modulus

    def encrypt(self, string):
        pass

    def decrypt(self, string):
        pass

    def isPrime(self, n, k=100):
        d = n - 1
        s = 0

        while d % 2 == 0:
            d //= 2
            s += 1

        for _ in range(k):
            a = random.randrange(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue

            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break

            else:
                return False

        return True


    def genPrime(self):
        while True:
            n = random.getrandbits(96)
            n |= 1

            if self.isPrime(n):
                return n



rsa = RSA()

print(rsa.genPrime())
