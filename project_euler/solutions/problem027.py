from math import sqrt
from project_euler.library import list_primes


def get_answer(limit=1_000):
    sieve = find_primes(100_000)
    primes = list_primes(limit)
    product, sequence_length = 0, 0
    for a in range(-limit + 1, limit, 2):
        for b in primes:
            n = 0
            count = 0
            while True:
                next_number = n * n + a * n + b
                if sieve[next_number // 2]:
                    count += 1
                    n += 1
                else:
                    break
            if count > sequence_length:
                sequence_length = count
                product = a * b
    return product


def find_primes(limit):
    sieve = [True] * (limit // 2)
    sieve[0] = False
    i = 1
    bound = sqrt(limit)
    while (2 * i) < bound:
        if sieve[i]:
            j = (3 * i) + 1
            while (2 * j) + 1 < limit:
                sieve[j] = False
                j += (2 * i) + 1
        i += 1
    return sieve
