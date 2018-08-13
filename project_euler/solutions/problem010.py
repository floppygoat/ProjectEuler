from math import sqrt


def get_answer(limit=2_000_000):
    """
    Uses the Sieve of Eratosthenes with only odd numbers to find all primes less than limit
    :type limit: int
    :return: the summation prime numbers less than limit (and greater than one)
    """
    if limit < 2:
        return []

    # To account for the number 2
    summation = 2

    # A sieve that only contains odd numbers (the only even prime number is 2).
    # Sieve indices i correspond to the number (i * 2) + 1
    sieve = [True] * (limit // 2)

    # 1 is not a prime number
    sieve[0] = False

    # Make the sieve and find all primes less than sqrt(limit)
    # It is only possible only numbers less than or equal sqrt(limit) to contribute to the sieve
    for i in range((int(sqrt(limit)) // 2) + 1):
        if sieve[i]:
            summation += i * 2 + 1
            for j in range((i * 3) + 1, limit // 2, (i * 2) + 1):
                sieve[j] = False

    # Find all remaining prime numbers in the sieve that are greater than sqrt(limit)
    for i in range((int(sqrt(limit)) // 2) + 1, len(sieve)):
        if sieve[i]:
            summation += i * 2 + 1

    return summation
