from project_euler.library import list_primes, is_prime
from itertools import combinations


def get_answer(n=8):
    """
    We first make a list of prime numbers, expanding this list each time we haven't found a solution for digits
    up to the next power of 10.  We then 'process' each prime number to determine if it could be part of this
    8 prime family.
    :param n:
    :return:
    """
    size = 1
    length = 0
    while True:
        p = list_primes(10 ** size)
        primes = p[length:]
        length = len(p)
        for prime in primes:
            if process(prime, n, p):
                return prime
        size += 1


def process(prime, n, primes):
    p = prime
    size = 0
    histogram = [[], [], [], [], [], [], [], [], [], []]
    while p > 0:
        digit, p = p % 10, p // 10
        histogram[digit].append(size)
        size += 1

    # We won't check for digits greater than 10 - n because the number by replacing those digits are either
    # primes we have already processed and found to be not part of the n prime family, or they are not prime.
    del histogram[10 - n:]
    digit = 0
    # iterate through list in histogram
    for hist in histogram:
        # iterate through the length of each list in histogram
        # for n >= 8, we don't have to check for even lengths because one of the numbers must found must be
        # divisible by 3
        # for i in range(1, len(hist) + 1, 2):
        for i in range(1, len(hist) + 1):
            itr = combinations(hist, i)
            temp = prime
            # iterate through each combination
            for comb in itr:
                count = 1   # temp is already a prime
                # iterate switching digits from 'digit' to 10
                for j in range(digit + 1, 10):
                    if n > count + 10 - j:
                        break
                    # iterate through each place we are changing the position
                    for c in comb:
                        temp += 10 ** c
                    if is_prime(temp, primes):
                        count += 1
                    if count == n:
                        return True

        digit += 1
    return False
