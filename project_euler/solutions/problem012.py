from project_euler.library import list_primes


def get_answer(divisor_count=500):
    """
    Triangle numbers are in the form of n(n+1)/2.
    Since n and n+1 must be coprime, if we calculate the number of divisors n and n+1 have,
    they can be multiplied together (and divided by two),
    to determine the amount of divisors the corresponding triangle number has.
    :return: The first triangle number with over divisor_count divisors (including itself and 1)
    """
    # I'm not too sure of a function that would determine an upper bound of how many
    # primes I need based on the divisor_count.  This seems to work.
    primes = list_primes(pow(10, len(str(divisor_count))))
    num_divisors = [0, 1]
    i = 1
    while True:
        if divisor_count < num_divisors[i] * num_divisors[(i + 1) // 2]:
            return i * (i + 1) // 2
        i += 1
        num_divisors.append(number_of_divisors(i, primes, num_divisors))
        num_divisors.append(number_of_divisors(i + 1, primes, num_divisors))
        if divisor_count < num_divisors[i // 2] * num_divisors[i + 1]:
            return i * (i + 1) // 2
        i += 1


def number_of_divisors(num, primes, divisors):
    """
    :type num: int
    :param primes: list of primes with at least all positive prime numbers less than (number // 2 + 1)
    :type primes: list
    :param divisors: list of numbers which correspond to the number of divisors its index has
    :type divisors: list
    :return: the number of divisors num has, including itself and 1
    :rtype: int
    """
    itr = iter(primes)
    divisor_count = 1
    while num > 1:
        next_prime = itr.__next__()
        count = 0
        while num % next_prime == 0:
            count += 1
            num //= next_prime
        if count != 0:
            divisor_count *= count + 1
            return divisor_count * divisors[num]
        if num < next_prime * next_prime:
            return divisor_count * 2
    return divisor_count
