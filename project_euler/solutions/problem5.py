from functools import reduce
from project_euler.library import lcm


def get_answer(largest_divisor=20):
    """
    Essentially, you are looking for lcm(1, 2, 3, ..., largest_divisor).
    :return: The smallest number evenly divisible by all numbers in range(1, largest_divisor)
    """
    return reduce(lambda i, j: lcm(i, j), range(2, largest_divisor))
