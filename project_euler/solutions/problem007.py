from project_euler.library import list_n_primes


def get_answer(nth=10_00):
    """
    The sieve of Eratosthenes is the best algorithm for finding prime numbers.
    Thus we want to utilize this algorithm to find the nth prime.
    However we need to have a maximum bound of the nth prime to use the sieve algorithm effectively.
    The maximum bound for the nth prime for all primes greater than or equal to:
    int(nth * (log(nth) + log(log(nth)))) + 1.
    :return: The nth prime number
    """
    return list_n_primes(nth)[nth - 1]
