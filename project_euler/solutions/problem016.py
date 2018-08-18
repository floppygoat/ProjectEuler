def get_answer(base=2, exponent=1_000):
    power = base ** exponent
    summation = 0
    while power > 0:
        summation += power % 10
        power //= 10
    return summation
