import random

class RSA():
    publicKey = []
    privateKey = 0

    def __init__(self):
        p = self.genPrime()
        q = self.genPrime()

        n = q * p
        r = (p - 1) * (q - 1)
        e = self.findE(r)

        self.privateKey = self.findMultInv(e, r)
        self.publicKey = [e, n]

    def stringToBits(self, string):
        # 08b adds bitts at the start so that 1 is 00000001
        return ''.join(f'{ord(char):08b}' for char in string)

    def findE(self, r):
        e = 3
        while self.gcd(e, r) != 1:
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
        stringBits = int(self.stringToBits(string), 2)
        encryptedString = pow(stringBits, self.publicKey[0], self.publicKey[1])

        return encryptedString


    def decrypt(self, encryptedStringAsNum):
        decryptedNum = pow(encryptedStringAsNum, self.privateKey, self.publicKey[1])
        # apparently for big nums you have to specify the amount of space the thing takes
        # +7 makes sure that the string is rounded to the next byte and // 8 computes the num of bytes
        decryptedString = decryptedNum.to_bytes((decryptedNum.bit_length() + 7) // 8, byteorder='big').decode('ascii')

        return decryptedString

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
encryptedString = rsa.encrypt("Hello World!")
print(encryptedString)
decryptedString = rsa.decrypt(encryptedString)
print(decryptedString)
