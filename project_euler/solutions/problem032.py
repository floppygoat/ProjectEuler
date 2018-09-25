def get_answer():
    summation = 0
    products_found = []
    for i in range(1, 10):
        for j in range(1_000, 10_000):
            k = i * j
            num = 100_000_000 * i + 10_000 * j + k
            if len(str(k)) > 4:
                break
            if pandigital(num) and not products_found.__contains__(k):
                summation += k
                products_found.append(k)
    for i in range(10, 100):
        for j in range(100, 1_000):
            k = i * j
            num = 100_000_00 * i + 10_000 * j + k
            if len(str(k)) > 4:
                break
            if pandigital(num) and not products_found.__contains__(k):
                summation += k
                products_found.append(k)
    return summation


def pandigital(num):
    check_digits = [True] * 9
    while num != 0:
        digit = num % 10
        num //= 10
        if check_digits[digit - 1] and digit != 0:
            check_digits[digit - 1] = False
        else:
            return False
    return True
