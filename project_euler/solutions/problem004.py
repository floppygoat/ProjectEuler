from project_euler.library import is_palindrome


def get_answer(bound=1_000):
    """
    This algorithm goes through the product of two numbers less than bound in decreasing order.
    This way, the first instance we hit a palindrome must be the largest palindrome we will encounter,
    and we can immediately terminate the function.
    :return: The largest palindrome made up of the product of two numbers below bound
    """
    for x in reversed(range(bound)):
        for y, z in zip(range(x, 2 * x - bound, -1), range(x, bound)):
            if is_palindrome(z * y):
                return z * y
        for y, z in zip(range(x - 1, 2 * x - bound - 1, -1), range(x, bound)):
            if is_palindrome(z * y):
                return z * y
