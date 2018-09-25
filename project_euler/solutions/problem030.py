from itertools import combinations_with_replacement


def get_answer(power=5):
    digit_power = []
    for i in range(10):
        digit_power.append(i ** power)
    digit_combs = set()
    for i in range(2, upper_bound(power) + 1):
        itr = combinations_with_replacement(digit_power, i)

        # We don't need 0 or 1
        itr.__next__()
        itr.__next__()

        for digits in itr:
            s = 0
            for digit in digits:
                s += digit
            digit_combs.add(s)

    summation = 0
    for number in digit_combs:
        s = 0
        n = number
        while n > 0:
            s += digit_power[n % 10]
            n //= 10
        if s == number:
            summation += number
    return summation


def upper_bound(power):
    i = 1
    bound = 9 ** power
    while True:
        if len(str(bound)) <= i:
            return i
        i += 1
        bound += 9 ** power
