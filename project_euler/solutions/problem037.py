from math import sqrt


def get_answer():
    summation = 0
    primes = find_primes(1_000_000)
    count = 0
    i = 10
    while count < 11:
        truncatable_prime = True
        if primes[i]:
            num1 = i // 10
            j = 10
            num2 = i % j
            while num1 > 0:
                if not (primes[num1] and primes[num2]):
                    truncatable_prime = False
                    break
                num1 //= 10
                j *= 10
                num2 = i % j
            if truncatable_prime:
                count += 1
                summation += i
        i += 1
    return summation


def find_primes(limit):
    sieve = [True] * limit
    sieve[0], sieve[1] = False, False
    i = 2
    bound = sqrt(limit) + 1
    while i < bound:
        if sieve[i]:
            j = 2 * i
            while j < limit:
                sieve[j] = False
                j += i
        i += 1
    return sieve
