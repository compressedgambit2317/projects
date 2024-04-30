
import random
import math



def isPrime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    sqrt = math.sqrt(number)
    sqrt = int(sqrt)
    for i in range(3, sqrt + 1, 2):
        if number % i == 0:
            return False
    return True



def generatePrime():
    num = random.randint(10, 1000)
    while not isPrime(num):
        num = random.randint(10, 1000)
    return num



def primitiveRoot(prime):
    for i in range(2, prime):
        powers = []
        for j in range(1, prime):
            power = (i ** j) % prime
            if power in powers:
                break
            powers.append(power)
        if len(powers) == prime - 1:
            return i
    return None

p = generatePrime()
g = primitiveRoot(p)

a = random.randint(1, p - 1)
A = (g ** a) % p
b = random.randint(1, p - 1)
B = (g ** b) % p
shared_secret_key_A = (B ** a) % p
shared_secret_key_B = (A ** b) % p
print("DH Key Exchange Protocol:")
if shared_secret_key_A == shared_secret_key_B:
    print("Shared secret keys match!")

else:
    print("Shared secret keys do not match!")


def printTable(a, b, A, B, Sa, Sb):
    print("Alice\tBob\t\tEve")

    print(str(a) + "\t\t" + str(b) + "\t\t" + "Nothing")
    print(str(A) + "\t\t" + str(B) + "\t\t" + "Alice and Bob's public keys")
    print(str(Sa) + "\t\t" + str(Sb) + "\t\t" + str((A ** B) % p))

printTable(a, b, A, B, shared_secret_key_A, shared_secret_key_B)
