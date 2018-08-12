import time

# project_euler.solutions import * : all files are named in the form 'problem_', where _ is a numeral.
from project_euler.solutions import *

from project_euler import library
from math import sqrt, inf


def get_problem(problem_number):
    try:
        func = dictionary(problem_number)
        start_time = time.perf_counter()
        answer = func()
        runtime = time.perf_counter() - start_time
    except KeyError:
        answer = None
        runtime = 0
    except AttributeError:
        answer = None
        runtime = 0
    print()
    print("The answer to Problem", problem_number, "is:", answer)
    print("The elapsed time is", runtime, "seconds")
    return answer, runtime


def dictionary(problem_number):
    project_euler_dictionary = {
        1: problem1.get_answer,
        2: problem2.get_answer,
        3: problem3.get_answer,
        4: problem4.get_answer,
        5: problem5.get_answer,
        6: problem6.get_answer,
        7: problem7.get_answer,
        8: problem8.get_answer,
        9: problem9.get_answer,
        10: problem10.get_answer,
        11: problem11.get_answer,
        12: problem12.get_answer,
        13: problem13.get_answer,
        92: Problem92(10_000_000),
        14: problem14.get_answer,
        52: Problem52(),
        53: Problem53(max_n=100, limit=1_000_000),
        81: Problem81(filename="text_files/problem81.txt"),
        82: Problem82(filename="text_files/problem82.txt"),
        83: Problem83(filename="text_files/problem83.txt"),
        97: Problem97(7_830_457, 28_433, 10),
        206: Problem206()
    }
    return project_euler_dictionary[problem_number]


class Problem52:

    def __init__(self):
        self.answer = None

    @staticmethod
    def check(number):
        number_copy = number
        digits = []
        while number_copy > 0:
            digits.append(number_copy % 10)
            number_copy //= 10
        digits.sort()
        for i in range(2, 7):
            number_copy = number * i
            permutation = []
            while number_copy > 0:
                permutation.append(number_copy % 10)
                number_copy //= 10
            permutation.sort()
            if permutation != digits:
                return False
        return True

    @staticmethod
    def get_answer():
        i = 5
        while True:
            for number in range(1 * (10 ** i) + 2, int((10 / 6) * (10 ** i)) + 1, 3):
                if Problem52.check(number):
                    return number
            i += 1

    def run(self):
        self.answer = self.get_answer()
        return self.answer


class Problem53:
    """
    https://projecteuler.net/problem=53


    There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    In combinatorics, we use the notation, {5}C{3} = 10.

    In general,

    nCr = n!/{r!(n−r)!},

    where r ≤ n, n! = n × (n−1) × ... × 3 × 2 × 1, and 0! = 1.

    It is not until n = 23, that a value exceeds one-million: {23}C{10} = 1144066.

    How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
    """

    def __init__(self, max_n, limit):
        self.max_n = max_n
        self.limit = limit
        self.answer = None

    @staticmethod
    def get_answer(max_n, limit):
        count = 0
        for n in range(1, max_n + 1):
            for k in range(1, n + 1):
                if library.n_choose_k(n, k) >= limit:
                    count += 1
        return count

    def run(self):
        self.answer = self.get_answer(self.max_n, self.limit)
        return self.answer


class Problem81:

    def __init__(self, filename):
        self.filename = filename
        self.answer = None

    @staticmethod
    def get_answer(filename):
        f = open(filename, "r")
        strings = f.readlines()
        f.close()
        matrix = []
        for x in range(0, len(strings)):
            matrix.append(list(map(int, strings[x].split(","))))
        size = len(matrix)  # Assume square matrix

        for x in range(size - 2, -1, -1):
            matrix[x][size - 1] += matrix[x + 1][size - 1]
            matrix[size - 1][x] += matrix[size - 1][x + 1]
        for x in range(size - 2, -1, -1):
            for i, j in zip(range(x, size - 1), range(size - 2, x - 1, -1)):
                if matrix[i + 1][j] <= matrix[i][j + 1]:
                    matrix[i][j] += matrix[i + 1][j]
                else:
                    matrix[i][j] += matrix[i][j + 1]
        for x in range(size - 3, -1, -1):
            for i, j in zip(range(0, x + 1), range(x, -1, -1)):
                if matrix[i + 1][j] <= matrix[i][j + 1]:
                    matrix[i][j] += matrix[i + 1][j]
                else:
                    matrix[i][j] += matrix[i][j + 1]
        return matrix[0][0]

    def run(self):
        self.answer = self.get_answer(self.filename)
        return self.answer


class Problem82:

    def __init__(self, filename):
        self.filename = filename
        self.answer = None

    @staticmethod
    def get_answer(filename):
        f = open(filename, "r")
        strings = f.readlines()
        f.close()
        matrix = []
        for x in range(0, len(strings)):
            matrix.append(list(map(int, strings[x].split(","))))
        size = len(matrix)  # Assume square matrix

        for length_index in range(size - 2, -1, -1):
            new_column = []
            for height_index in range(size):
                best_route_sum = matrix[height_index][length_index + 1]

                # check up
                check_sum = 0
                for i in range(height_index - 1, -1, -1):
                    check_sum += matrix[i][length_index]
                    if check_sum + matrix[i][length_index + 1] < best_route_sum:
                        best_route_sum = check_sum + matrix[i][length_index + 1]

                # check down
                check_sum = 0
                for i in range(height_index + 1, size):
                    check_sum += matrix[i][length_index]
                    if check_sum + matrix[i][length_index + 1] < best_route_sum:
                        best_route_sum = check_sum + matrix[i][length_index + 1]

                # put minimal route sum for each index in the column in the array
                new_column.append(best_route_sum)

            for height_index in range(size):
                matrix[height_index][length_index] += new_column[height_index]

        minimal_route_sum = matrix[0][0]
        for i in range(size):
            if matrix[i][0] < minimal_route_sum:
                minimal_route_sum = matrix[i][0]

        return minimal_route_sum

    def run(self):
        self.answer = self.get_answer(self.filename)
        return self.answer


class Problem83:

    def __init__(self, filename):
        self.filename = filename
        self.answer = None

    @staticmethod
    def get_answer(filename):
        f = open(filename, "r")
        strings = f.readlines()
        f.close()
        matrix = []
        for i in range(0, len(strings)):
            matrix.append(list(map(int, strings[i].split(","))))

        # Assume square matrix
        size = len(matrix)

        distance = [[inf] * size for x in range(size)]

        # Bellman-Ford algorithm with early exit
        distance[size - 1][size - 1] = matrix[size - 1][size - 1]
        while True:  # Note: The worst-case number of iterations is w*h
            finished = True
            for h in reversed(range(size)):
                for w in reversed(range(size)):

                    def get_distance(x, y):
                        if x < 0 or x >= size or y < 0 or y >= size:
                            return inf
                        else:
                            return distance[y][x]

                    temp = matrix[h][w] + min(
                        get_distance(w - 1, h),
                        get_distance(w + 1, h),
                        get_distance(w, h - 1),
                        get_distance(w, h + 1))

                    if temp < distance[h][w]:
                        distance[h][w] = temp
                        finished = False
            if finished:
                return distance[0][0]

    def run(self):
        self.answer = self.get_answer(self.filename)
        return self.answer


class Problem92:
    """
    https://projecteuler.net/problem=92


    A number chain is created by continuously adding the square of the digits in a number to form a new number
    until it has been seen before.

    For example,

    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

    Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
    What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

    How many starting numbers below ten million will arrive at 89?
    """

    def __init__(self, limit):
        self.limit = limit
        self.answer = None

    @staticmethod
    def get_answer(limit):
        # TODO Optimize
        sequences = [0] * limit
        sequences[1] = 1
        sequences[89] = 89
        count = 0
        for i in range(1, 81 * (len(str(limit)) - 1) + 1):
            seq = []
            while True:
                if sequences[i] == 0:
                    seq.append(i)
                    j = 0
                    while i > 0:
                        j += pow(i % 10, 2)
                        i //= 10
                    i = j
                elif sequences[i] == 89:
                    count += 1
                    for k in seq:
                        sequences[k] = 89
                    break
                else:
                    for k in seq:
                        sequences[k] = 1
                    break
        for i in range(81 * (len(str(limit)) - 1) + 1, limit):
            j = 0
            while i > 0:
                j += pow(i % 10, 2)
                i //= 10
            i = j
            if sequences[i] == 89:
                count += 1
        return count

    def run(self):
        self.answer = self.get_answer(self.limit)
        return self.answer


class Problem97:
    """
    https://projecteuler.net/problem=97


    The first known prime found to exceed one million digits was discovered in 1999,
    and is a Mersenne prime of the form 2^{6972593}−1; it contains exactly 2,098,960 digits.
    Subsequently other Mersenne primes, of the form 2^{p}−1, have been found which contain more digits.

    However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits:
    28433×2^{7830457}+1.

    Find the last ten digits of this prime number.
    """

    def __init__(self, power, multiple, amount_of_digits):
        self.power = power
        self.multiple = multiple
        self.amount_of_digits = amount_of_digits
        self.answer = None

    @staticmethod
    def get_answer(power, multiple, amount_of_digits):
        return (multiple * pow(2, power, 10 ** amount_of_digits) + 1) % (10 ** amount_of_digits)

    def run(self):
        self.answer = self.get_answer(self.power, self.multiple, self.amount_of_digits)
        return self.answer


class Problem206:
    """
    https://projecteuler.net/problem=206


    Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
    where each “_” is a single digit.
    """

    def __init__(self):
        self.answer = None

    @staticmethod
    def check(number):
        for digit in range(9, 0, -1):
            if number % 10 != digit:
                return False
            number //= 100
        return True

    @staticmethod
    def get_answer():
        for i in range(int(sqrt(1_92_93_94_95_96_97_98_99_90 // 100)),
                       int(sqrt(1_02_03_04_05_06_07_08_09_00 // 100)),
                       -1):
            if Problem206.check((i * i)):
                return i * 10

    def run(self):
        self.answer = self.get_answer()
        return self.answer
