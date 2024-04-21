# BRUTE FORCING D

import math
import time


def decrypt_message(ciphertext, d, n):
    decrypted_message = pow(ciphertext, d, n)
    return decrypted_message



e = int(input("Enter e: "))
n = int(input("Enter n: "))


original_message1 = 15
encrypted_message1 = pow(original_message1, e, n)
original_message2 = 14
encrypted_message2 = pow(original_message2, e, n)


start_time = time.time()

d1 = 1
calculated_message1 = decrypt_message(encrypted_message1, d1, n)

while calculated_message1 != original_message1:
    d1 += 1
    calculated_message1 = decrypt_message(encrypted_message1, d1, n)



d2 = 1
calculated_message2 = decrypt_message(encrypted_message2, d2, n)

while calculated_message2 != original_message2:
    d2 += 1
    calculated_message2 = decrypt_message(encrypted_message2, d2, n)



while d1 != d2 or calculated_message1 != original_message1 or calculated_message2 != original_message2:
    if d1 < d2:
        d1 += 1
        calculated_message1 = decrypt_message(encrypted_message1, d1, n)
    elif d2 < d1:
        d2 += 1
        calculated_message2 = decrypt_message(encrypted_message2, d2, n)
    else:
        d1 += 1
        d2 += 1
        calculated_message1 = decrypt_message(encrypted_message1, d1, n)
        calculated_message2 = decrypt_message(encrypted_message2, d2, n)


end_time = time.time()
time_taken = (end_time - start_time) * 1000


print("Brute forced d: ", d1)
print("Time taken: ", time_taken, " milliseconds")

print(original_message1)
print(calculated_message1)
print(original_message2)
print(calculated_message2)