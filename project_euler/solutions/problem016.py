def get_answer(base=2, exponent=1_000):
    """
    With Python's arbitrary precision, you can just calculate 2^{1_000},
    and then modulo/integer_divide by 10 to sum up the digits of 2^{1_000}.
    :return: The sum of the digits of base^{exponent}.
    """
    power = base ** exponent
    summation = 0
    while power > 0:
        summation += power % 10
        power //= 10
    return summation
