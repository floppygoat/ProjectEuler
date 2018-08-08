from project_euler.library import lcm


def get_answer(multiple1=3, multiple2=5, limit=1_000):
    """
    An algebraic solution exists that leads to an O(1) algorithm (assuming all embedded operations are also O(1)).
    :return: The sum of all number that are multiples of multiple1 and/or multiple2 less than limit
    """
    multiple3 = lcm(multiple1, multiple2)
    k = limit - 1
    n1 = k // multiple1
    n2 = k // multiple2
    n3 = k // multiple3
    return (multiple1 * n1 * (n1 + 1) // 2) + \
           (multiple2 * n2 * (n2 + 1) // 2) - \
           (multiple3 * n3 * (n3 + 1) // 2)


def get_answer_alt(multiple1=3, multiple2=5, limit=1_000_000):
    """
    Alternatively, we can iterate and sum all multiples of multiple1 and multiple2 less than limit,
    and then subtract the sum of all multiples of the lowest_common_multiple(multiple1, multiple2) less than limit.
    This gives us an O(n) algorithm that depends on limit.
    :return: The sum of all number that are multiples of multiple1 and/or multiple2 less than limit
    """
    summation = 0
    for x in range(0, limit, multiple1):
        summation += x
    for x in range(0, limit, multiple2):
        summation += x
    for x in range(0, limit, lcm(multiple1, multiple2)):
        summation -= x
    return summation
