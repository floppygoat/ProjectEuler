from math import sqrt


def get_answer(limit=1_000_000):
    count = 1
    primes = find_primes(limit)
    for i in range(3, limit, 2):
        number = i
        if primes[number // 2]:
            circular_prime = True
            size = len(str(number))
            digit = number % 10
            number //= 10
            number += digit * (10 ** (size - 1))
            while number != i:
                if not primes[number // 2] or number % 2 == 0:
                    circular_prime = False
                    break
                digit = number % 10
                number //= 10
                number += digit * (10 ** (size - 1))
            if circular_prime:
                primes[number // 2] = False
                count += 1
                digit = number % 10
                number //= 10
                number += digit * (10 ** (size - 1))
                while number != i:
                    if primes[number // 2]:
                        primes[number // 2] = False
                        count += 1
                    digit = number % 10
                    number //= 10
                    number += digit * (10 ** (size - 1))
    return count


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
