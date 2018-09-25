# TODO use dynamic programming
from math import sqrt


def get_answer(limit=1_000_000):
    primes = find_primes(limit)
    largest_prime = primes[0]
    longest_count = 1
    for i in range(0, len(primes)):
        summation = 0
        count = 0
        for j in range(i, len(primes)):
            summation += primes[j]
            if summation > limit:
                break
            count += 1
            if primes.count(summation) == 1 and longest_count < count:
                longest_count = count
                largest_prime = summation
    return largest_prime


def find_primes(limit):
    sieve = [True] * (limit // 2)
    i = 1
    bound = sqrt(limit)
    while (2 * i) < bound:
        if sieve[i]:
            j = (3 * i) + 1
            while (2 * j) + 1 < limit:
                sieve[j] = False
                j += (2 * i) + 1
        i += 1
    i = 1
    primes = [2]
    while i < len(sieve):
        if sieve[i]:
            primes.append((i * 2) + 1)
        i += 1
    return primes
