from math import sqrt

# TODO use dynamic programing


def get_answer(number_of_distinct_prime_factors=4, consecutive_numbers=4):
    primes, number_prime_factors = find_primes(1_000_000)
    count_consecutive_numbers = 0
    i = 1
    while True:
        number = i
        j = 0
        count_prime_factors = 0
        while number > 1:
            if number_prime_factors[number] != 0:
                count_prime_factors += number_prime_factors[number]
                break
            if number % primes[j] == 0:
                number //= primes[j]
                count_prime_factors += 1
                if number_prime_factors[number] != 0:
                    count_prime_factors += number_prime_factors[number]
                    break
                while number % primes[j] == 0:
                    number //= primes[j]
            j += 1
        number_prime_factors[i] == count_prime_factors
        if count_prime_factors != number_of_distinct_prime_factors:
            count_consecutive_numbers = 0
        else:
            count_consecutive_numbers += 1
            if count_consecutive_numbers == consecutive_numbers:
                return i - consecutive_numbers + 1
        i += 1


def find_primes(limit):
    sieve = [True] * int(limit / 2)
    i = 1
    bound = sqrt(limit)
    while (i * 2) < bound:
        if sieve[i]:
            j = (i * 3) + 1
            while (j * 2) + 1 < limit:
                sieve[j] = False
                j += (i * 2) + 1
        i += 1
    i = 1
    primes = [2]
    while i < len(sieve):
        if sieve[i]:
            primes.append((i * 2) + 1)
        i += 1
    number_prime_factors = [0, 0, 1]
    i = 1
    while i < len(sieve):
        if sieve[i]:
            number_prime_factors.append(1)
        else:
            number_prime_factors.append(0)
        number_prime_factors.append(0)
        i += 1
    return primes, number_prime_factors
