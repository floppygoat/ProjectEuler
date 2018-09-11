def get_answer(number_of_digits=1_000):
    """
    Brute-force.
    Continues iterating through the Fibonacci sequence until it finds a number of length <number_of_digits>.
    :return: Index of first Fibonacci number to contain <number_of_digits> digits.
    """
    a, b, index = 1, 1, 2
    while True:
        if len(str(a)) == number_of_digits:
            return index
        a, b, index = a + b, a, index + 1
