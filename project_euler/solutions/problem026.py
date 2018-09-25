from project_euler.library import list_primes


def get_answer(limit=1_000):
    """
    The longest reciprocal decimal cycle is going to be a prime number.
    The longest cycle a number can undergo is the number itself.
    Therefore, we work progressively down the list of primes
    until the longest_cycle length is greater than the next prime.
    :return: The number less than <limit> that has the longest reciprocal decimal cycle is.
    """
    primes = list_primes(limit)
    number = 1
    longest_cycle_length = 0
    for i in reversed(primes):
        if i < longest_cycle_length:
            return number
        x = cycle_length(i)
        if longest_cycle_length < x:
            longest_cycle_length = x
            number = i
    return number


def cycle_length(divisor):
    """
    This function does long division on <divisor>.
    It stores the remainder each time in a set and a list.
    If the remainder exists in the list, that means the division has undergone a cycle.
    We go through the list backwards until we encounter the number.
    We then return the length of that cycle.
    :param divisor: The number to determine how long its reciprocal decimal cycle is.
    :return: The length of the repeating decimal cycle.
    """
    dividend = 1
    cycle_list = []
    cycle_set = set()
    while True:
        count = 0
        dividend -= divisor * (dividend // divisor)
        if dividend in cycle_set:
            for i in reversed(cycle_list):
                count += 1
                if i == dividend:
                    return count
        cycle_list.append(dividend)
        cycle_set.add(dividend)
        dividend *= 10
