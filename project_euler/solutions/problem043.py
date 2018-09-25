from itertools import permutations


def get_answer():
    summation = 0
    divisors = [1, 2, 3, 5, 7, 11, 13, 17]
    itr = iter(permutations(range(10)))
    for digits in itr:
        check = True
        for i in reversed(range(len(divisors))):
            num = 100 * digits[i] + 10 * digits[i + 1] + digits[i + 2]
            if (num // divisors[i]) * divisors[i] != num:
                check = False
                break
        if check:
            summation += int(''.join(map(str, digits)))
    return summation
