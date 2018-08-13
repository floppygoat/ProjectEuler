def get_answer(bound=100):
    """
    A sum of numbers equals n(n + 1)/2.  A sum of (numbers)^2 = (2n + 1)(n + 1)n/6.
    Subtracting the latter from the square of the first gives you the answer.
    :return: The difference between the sum of the squares and the square of the sum.
    """
    return pow(bound * (bound + 1) // 2, 2) - ((2 * bound + 1) * (bound + 1) * bound) // 6
