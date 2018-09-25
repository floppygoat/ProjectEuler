from itertools import permutations
from project_euler.library import list_primes


def get_answer():
    primes = list_primes(7_654_321)
    pandigitals = []
    itr = iter(permutations(range(1, 8)))
    try:
        while True:
            pandigitals.append(int(''.join(map(str, itr.__next__()))))
    except StopIteration:
        pass
    itr_primes = iter(reversed(primes))
    itr_pandigital = iter(reversed(pandigitals))
    next_prime = itr_primes.__next__()
    next_pandigital = itr_pandigital.__next__()
    while True:
        if next_prime > next_pandigital:
            next_prime = itr_primes.__next__()
        elif next_prime < next_pandigital:
            next_pandigital = itr_pandigital.__next__()
        else:
            return next_pandigital
