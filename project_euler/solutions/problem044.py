from math import sqrt, inf


def get_answer():
    pentagonal_numbers = [1]
    difference = inf
    n = 2
    while True:
        next_pentagonal_number = n * (3 * n - 1) // 2
        for pentagonal_number in pentagonal_numbers:
            if is_pentagonal(next_pentagonal_number - pentagonal_number):
                if is_pentagonal(next_pentagonal_number + pentagonal_number):
                    return next_pentagonal_number - pentagonal_number
        pentagonal_numbers.append(next_pentagonal_number)
        n += 1


def is_pentagonal(number):
    n = int(((1 / 2) + sqrt(1 / 4 + 6 * number)) // 3)
    return number == (n * (3 * n - 1)) // 2
