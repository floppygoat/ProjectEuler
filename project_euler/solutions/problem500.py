import heapq
from project_euler.library import list_n_primes


def get_answer(exponent=500500, mod=500500507):
    """
    You want to find the smallest number that has 2^exponent divisors
    The least number that has 2^exponent will be the product of all elements in the set S,
    where S is the least set with numbers in the form p^2^k, where p are prime numbers and k is an integer.

    To figure out how many divisors a number has, you can find the prime divisors of the number,
    then multiply all (exponents + 1) to each other.  Using this fact, you can then prove why
    the product of S sized exponent gives the desired.

    :return: The smallest number that has 2^exponent divisors
    """
    primes = list_n_primes(exponent)
    heap = []
    prime_itr = iter(primes)

    # Note: Since this heap package only supports min-heaps,
    # all numbers are multiplied by -1 when put into and taken out of the heap
    for i in range(exponent):
        heapq.heappush(heap, -prime_itr.__next__())

    # Finding the least set S which contains 'exponent' (500500) numbers in the form of p^2^k,
    # where k is an element of integers, and p is an element of prime numbers
    prime_itr = iter(primes)
    while True:
        next_prime = prime_itr.__next__()
        pw = 2
        x = -pow(next_prime, pw)
        while x > heap[0]:
            heapq.heappushpop(heap, x)
            pw *= 2
            x = -pow(next_prime, pw)
        if pw == 2:
            break

    # Multiplying and returning all numbers in found set S
    smallest_prime_factor = 1
    for i in heap:
        smallest_prime_factor *= i
        smallest_prime_factor %= mod
    return smallest_prime_factor
