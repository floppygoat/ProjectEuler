from math import sqrt


def get_answer():
    primes = find_primes(1_000_000)
    twice_the_squares = find_twice_the_squares(1_000_000)
    it = iter(primes)
    number = 3
    prime = it.__next__()
    while True:
        while prime < number:
            prime = it.__next__()
        if number != prime:
            class Found(Exception):
                pass
            try:
                it_squares = iter(twice_the_squares)
                next_square = it_squares.__next__()
                while next_square < number:
                    it_primes = iter(primes)
                    next_prime = it_primes.__next__()
                    if next_prime + next_square == number:
                        raise Found
                    while next_prime + next_square < number:
                        next_prime = it_primes.__next__()
                        if next_prime + next_square == number:
                            raise Found
                    next_square = it_squares.__next__()
                return number
            except Found:
                pass
        number += 2


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


def find_twice_the_squares(limit):
    squares = []
    for i in range(1, int(sqrt(limit)) + 1):
        squares.append(2 * (i ** 2))
    return squares
