from math import sqrt, log
from project_euler.library import list_primes


def get_answer(nth=10_001):
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
