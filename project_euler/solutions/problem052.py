def get_answer():
    i = 5
    while True:
        for number in range(1 * (10 ** i) + 2, int((10 / 6) * (10 ** i)) + 1, 3):
            if check(number):
                return number
        i += 1


def check(num):
    number_copy = num
    digits = []
    while number_copy > 0:
        digits.append(number_copy % 10)
        number_copy //= 10
    digits.sort()
    for j in range(2, 7):
        number_copy = num * j
        permutation = []
        while number_copy > 0:
            permutation.append(number_copy % 10)
            number_copy //= 10
        permutation.sort()
        if permutation != digits:
            return False
    return True
