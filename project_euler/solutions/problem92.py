from itertools import combinations_with_replacement
from math import factorial


def get_answer(power=7):
    count = 0
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    sequences = [0] * (81 * power + 1)
    sequences[1] = 1
    sequences[89] = 89
    for i in range(1, 81 * power + 1):
        seq = []
        while True:
            if sequences[i] == 89:
                for k in seq:
                    sequences[k] = 89
                break
            elif sequences[i] == 1:
                for k in seq:
                    sequences[k] = 1
                break
            else:
                seq.append(i)
                j = 0
                while i > 0:
                    j += pow(i % 10, 2)
                    i //= 10
                i = j
    itr = combinations_with_replacement(range(0, 10), power)
    itr.__next__()
    for digits in itr:
        summation = 0
        for digit in digits:
            summation += squares[digit]
        if sequences[summation] == 89:
            count += permutations(digits)
    return count


def permutations(digits):
    count = [0] * 10
    for digit in digits:
        count[digit] += 1
    divisor = 1
    numerator = len(digits)
    for i in count:
        divisor *= factorial(i)
    return factorial(numerator) // divisor
