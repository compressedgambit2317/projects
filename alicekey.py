import random
import math
import sympy

def generate_prime_number(size):
    while True:
        number = random.randint(2**(size-1), 2**size)
        if sympy.isprime(number):
            return number
        

def totient(p, q):
    return (p-1)*(q-1)


def generate_e(totient):
    while True:
        e = random.randint(2, totient)
        if math.gcd(e, totient) == 1:
            return e

def generate_d(totient, e):
    d = sympy.mod_inverse(e, totient)
    return d


print("Enter the number of bits of the prime numbers: ")
size = int(input())
p = generate_prime_number(size)
q = generate_prime_number(size)
n = p*q
t = totient(p, q)
e = generate_e(t)
d = generate_d(t, e)

print("Public key: ", (n, e))

print("Private key: ", d)

with open("public_key.txt", "w") as file:
    file.write(str(n) + "\n")
    file.write(str(e))

with open("private_key.txt", "w") as file:
    file.write(str(d) + "\n")
    file.write(str(n))

    





