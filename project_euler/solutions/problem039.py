def get_answer(max_perimeter=1_000):
    count = [0] * max_perimeter
    for n in range(1, max_perimeter):
        for m in range(n + 1, max_perimeter):
            if (2 * (m ** 2)) + (2 * m * n) > max_perimeter:
                break
            if find_gcd(m, n) == 1:
                k = 1
                while k * ((2 * (m ** 2)) + (2 * m * n)) <= max_perimeter:
                    count[k * (2 * (m ** 2)) + k * (2 * m * n) - 1] += 1
                    k += 1
    maximum = 1
    max_solutions = 1
    for i in range(len(count)):
        if count[i] > max_solutions:
            maximum = i + 1
            max_solutions = count[i]
    return maximum


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
