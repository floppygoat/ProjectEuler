from itertools import combinations_with_replacement
from math import factorial


def get_answer(power=7):
    """
    A good optimization to the problem is to calculate for numbers 1 through 9**2 * power
    (the largest possible second number in the sequence) whether the
    sequence converges to 1 or enters the repeating sequence that start with 89.
    You can then, with each possible combination (with replacement) of digits with length <power>,
    calculate how many permutations of those digits are.  You can then calculate the second number in the
    sequence based on the digits themselves, and from previous calculations, determine how many numbers
    enter the repeating sequence with 89.
    """
    count = 0
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    sequences = [0] * (81 * power + 1)
    sequences[1] = 1
    sequences[89] = 89

    # The second number in the sequence must <= 9**2 * power
    # The max occurs when the starting number consists only of nines
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

    # The iterator returns all possible combinations of digits.
    itr = combinations_with_replacement(range(0, 10), power)
    itr.__next__()  # Get rid of the zero tuple
    for digits in itr:
        summation = 0
        # Determine the second number in the sequence
        for digit in digits:
            summation += squares[digit]
        # Determines how many numbers enter the sequence with 89.
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
