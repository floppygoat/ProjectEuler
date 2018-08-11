from math import log
from project_euler.library import list_primes


def get_answer(nth=10_001):
    """
    The sieve of Eranthoses is the best algorithm for finding prime numbers.
    Thus we want to utilize this algorithm to find the nth prime.
    However we need to have a maximum bound of the nth prime to use the sieve algorithm effectively.
    The maximum bound for the nth prime for all primes greater than or equal to:
    int(nth * (log(nth) + log(log(nth)))) + 1.
    :return: The nth prime number
    """
    if nth < 6:
        primes = {
            1: 2,
            2: 3,
            3: 5,
            4: 7,
            5: 11
        }
        return primes[nth]
    else:
        return list_primes(int(nth * (log(nth) + log(log(nth)))) + 1)[nth - 1]
