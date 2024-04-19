# RSA KEY GENERATION

import math
import random

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_prime_number(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def generate_rsa_key_pair(bits):
    # Generate random prime numbers
    p = generate_prime_number(bits//2)
    q = generate_prime_number(bits//2)

    # Calculate n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose a random e that is coprime with phi(n)
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Calculate d as the modular inverse of e
    d = pow(e, -1, phi_n)

    # Return the public and private keys
    return ((e, n), (d, n))

# Generate RSA key pair
bits = int(input("Enter bit length: "))
public_key, private_key = generate_rsa_key_pair(bits)
while public_key == private_key:
    public_key, private_key = generate_rsa_key_pair(bits)

# Print the keys
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)