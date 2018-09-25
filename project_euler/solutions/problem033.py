def get_answer():
    numerator, denominator = 1, 1
    for x in range(1, 8):
        for y in range(x + 1, 9):
            for z in range(y + 1, 10):
                if 9 * x * (y - z) == z * (x - y):
                    numerator *= x
                    denominator *= y
    return denominator // find_gcd(denominator, numerator)


def find_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    if a == 0:
        return b
    else:
        return a