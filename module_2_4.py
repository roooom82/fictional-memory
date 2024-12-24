numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(2, 16):
    if (i % 2 == 0 and i / 2 != 1) or (i % 3 == 0 and i / 3 != 1):
        is_prime = True
        not_primes.append(i)
    else:
        is_prime = False
        primes.append(i)
print('Primes:', primes)
print('Not Primes:', not_primes)
