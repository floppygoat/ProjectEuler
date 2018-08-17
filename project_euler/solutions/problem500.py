import heapq
from project_euler.library import list_n_primes


def get_answer(exponent=500500, mod=500500507):
    primes = list_n_primes(exponent)
    heap = []
    prime_itr = iter(primes)
    for i in range(exponent):
        heapq.heappush(heap, -prime_itr.__next__())
    prime_itr = iter(primes)
    cont = True
    while cont:
        next_prime = prime_itr.__next__()
        pw = 2
        x = -pow(next_prime, pw)
        while x > heap[0]:
            heapq.heappushpop(heap, x)
            pw *= 2
            x = -pow(next_prime, pw)
        if pw == 2:
            cont = False
    smallest_prime_factor = 1
    try:
        while True:
            smallest_prime_factor *= -heapq.heappop(heap)
            smallest_prime_factor %= mod
    except IndexError:
        return smallest_prime_factor
