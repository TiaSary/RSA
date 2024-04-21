# factorizing n

import math
import random
import time

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



bit_length= 8
e = int(input("Enter e: "))
n = int(input("Enter n: "))


start_time = time.time()

for i in range (2, n):
    if n % i == 0 and is_prime(i):
        p = i
        q = n//p
        
print("p: ", p)
print("q: ", q)


phi_n = (p-1)*(q-1)

d = pow(e, -1, phi_n)


end_time = time.time()
time_taken = (end_time - start_time) * 1000

print ("d: ", d)
print("Time taken: ", time_taken, " milliseconds")