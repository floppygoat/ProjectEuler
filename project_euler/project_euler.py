import time

# project_euler.solutions import * : all files are named in the form 'problem_', where _ is the problem number.
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
    # except AttributeError:
        # answer = None
        # runtime = 0
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
        14: problem14.get_answer,
        15: problem15.get_answer,
        52: Problem52(),
        53: Problem53(max_n=100, limit=1_000_000),
        81: problem81.get_answer,
        82: problem82.get_answer,
        83: problem83.get_answer,
        92: problem92.get_answer,
        97: problem97.get_answer,
        206: problem206.get_answer,
        493: problem493.get_answer
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
