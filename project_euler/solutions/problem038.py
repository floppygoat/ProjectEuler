LIMIT = 9999


class DigitNotAvailable(Exception):
    pass


def get_answer():
    largest_pandigital = 1
    for i in range(1, LIMIT + 1):
        digit_available = [True] * 9
        j = 1
        pandigital = 0
        try:
            while True:
                if len(str(pandigital)) == 9:
                    if pandigital > largest_pandigital:
                        largest_pandigital = pandigital
                    break
                num = i * j
                while num > 0:
                    digit = num % 10
                    num //= 10
                    if digit_available[digit - 1]:
                        digit_available[digit - 1] = False
                    else:
                        raise DigitNotAvailable
                pandigital = pandigital * (10 ** len(str(i * j))) + (i * j)
                j += 1
        except DigitNotAvailable:
            pass
    return largest_pandigital
