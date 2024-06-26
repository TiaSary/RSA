# RSA KEY GENERATION

import random
import math

def generate_rsa_keys(bit_length):
    
    p = generate_prime_number(bit_length // 2)
    q = generate_prime_number(bit_length // 2)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = choose_public_exponent(phi_n)
    d = pow(e, -1, phi_n)

    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

def generate_prime_number(bit_length):
    while True:
        candidate = random.getrandbits(bit_length)
        if is_prime(candidate):
            return candidate

def is_prime(n, k=5):
   
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
   
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    
    def miller_rabin_test(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False
    
    for _ in range(k):
        a = random.randrange(2, n - 1)
        if not miller_rabin_test(a):
            return False
    
    return True

def choose_public_exponent(phi_n):
 
    e = random.randrange(2, phi_n)
    while math.gcd(e, phi_n) != 1:
        e = random.randrange(2, phi_n)
    return e



bit_length = int(input("Enter bit length: "))
public_key, private_key = generate_rsa_keys(bit_length)
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)


