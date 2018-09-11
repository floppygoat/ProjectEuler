def get_answer(factorial_base=100):
    """
    Using Python's arbitrary precision, calculates the factorial of <factorial_base>
    before summing up the digits of the number.
    :return:
    """
    factorial = 1
    for i in reversed(range(2, factorial_base + 1)):
        factorial *= i
    summation = 0
    while factorial > 0:
        summation += factorial % 10
        factorial //= 10
    return summation
