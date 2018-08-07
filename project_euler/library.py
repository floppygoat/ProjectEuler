from math import sqrt
from functools import reduce


def gcd(a, b):
    """
    This algorithm uses Euclid's algorithm with modulation to determine gcd(a,b)
    :type a: int
    :type b: int
    :return: the greatest common denominator of a and b
    :rtype: int
    """
    a, b = abs(a), abs(b)
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    if a == 0:
        return b
    else:
        return a


def lcm(a, b):
    """
    :type a: int
    :type b: int
    :return: the least common multiple of a and b
    :rtype int
    """
    try:
        return abs(a * b) // gcd(a, b)
    except ZeroDivisionError:
        return 0


def is_palindrome(number):
    """
    :type number: int
    :return: True if number is a palindrome in base 10, False otherwise
    :rtype: bool
    """
    palindrome = 0
    temp = number

    # Reverse the number
    while temp > 0:
        palindrome = (palindrome * 10) + (temp % 10)
        temp //= 10

    return number == palindrome


def list_primes(limit):
    """
    Uses the Sieve of Eratosthenes with only odd numbers to find all primes less than limit
    :type limit: int
    :return: prime numbers less than limit (and greater than one)
    :rtype: list
    """
    if limit < 2:
        return []

    # To account for the number 2
    primes = [2]

    # A sieve that only contains odd numbers (the only even prime number is 2).
    # Sieve indices i correspond to the number (i * 2) + 1
    sieve = [True] * (limit // 2)

    # 1 is not a prime number
    sieve[0] = False

    # Make the sieve and find all primes less than sqrt(limit)
    # It is only possible only numbers less than or equal sqrt(limit) to contribute to the sieve
    for i in range((int(sqrt(limit)) // 2) + 1):
        if sieve[i]:
            primes.append((i * 2) + 1)
            for j in range((i * 3) + 1, limit // 2, (i * 2) + 1):
                sieve[j] = False

    # Find all remaining prime numbers in the sieve that are greater than sqrt(limit)
    for i in range((int(sqrt(limit)) // 2) + 1, len(sieve)):
        if sieve[i]:
            primes.append((i * 2) + 1)

    return primes


def number_of_divisors(num, primes=None):
    """
    :type num: int
    :param primes: list of primes with at least all positive prime numbers less than (number // 2 + 1)
    :type primes: list
    :return: the number of divisors num has, including itself and 1
    :rtype: int
    """
    if primes is None:
        primes = list_primes((num // 2) + 1)
    itr = iter(primes)
    divisor_count = 1
    while num > 1:
        next_prime = itr.__next__()
        if num < next_prime * next_prime:
            return divisor_count * 2
        count = 0
        while num % next_prime == 0:
            count += 1
            num //= next_prime
        if count != 0:
            divisor_count *= count + 1
    return divisor_count


def n_choose_k(n, k):
    """
    Use the multiplicative formula to compute the binomial coefficient of (n, k)^{T}
    :type n: int
    :type k: int
    :return: n_choose_k
    :rtype: int
    """
    return reduce(lambda i, j: i * j, range(n - k + 1, n + 1)) // reduce(lambda i, j: i * j, range(1, k + 1))
