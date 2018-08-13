from math import sqrt
from project_euler.library import gcd


def get_answer(perimeter=1_000):
    """
    All pythagorean triples can be parameterized as:
        a = k * (m * m - n * n)
        b = k * (2 * m * n)
        c = k * (m * m + n * n),
    where m > n > 0, k > 0, m and n are coprime, and exactly 1 of m or n is even.
    :return: The product a * b * c of the first occurring a + b + c = perimeter, if one exists.
                Else, returns None
    """

    for m in range(2, int((-1 + sqrt(1 + 2 * perimeter)) // 2), 2):
        # m is even, so we only test odd values of n.
        for n in range(1, m, 2):
            # Are m and n coprime?
            if gcd(m, n) == 1:
                k = perimeter // (2 * (m * m + m * n))
                # if a + b + c == perimeter
                if 2 * k * (m * m + m * n) == perimeter:
                    # return a * b * c
                    return k * (m * m - n * n) * k * (2 * m * n) * k * (m * m + n * n)

        # So we do not have to test for exactly one of m or n to be even,
        # we repeat the loop, but with m as an odd number and testing only even numbers for n.
        m += 1
        for n in range(2, m, 2):
            # Are m and n coprime?
            if gcd(m, n) == 1:
                k = perimeter // (2 * (m * m + m * n))
                # if a + b + c == perimeter
                if 2 * k * (m * m + m * n) == perimeter:
                    # return a * b * c
                    return k * (m ** 2 - n ** 2) * k * (2 * m * n) * k * (m ** 2 + n ** 2)
    # No a + b + c == perimeter exists
    return None
