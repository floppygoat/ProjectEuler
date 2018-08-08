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
        6: Problem6(100),
        7: Problem7(10_001),
        8: Problem8("text_files/problem8.txt", 13),
        9: Problem9(1000),
        10: Problem10(2_000_000),
        11: Problem11("text_files/problem11.txt", 4),
        12: Problem12(500),
        13: Problem13("text_files/problem13.txt", 10),
        92: Problem92(10_000_000),
        14: Problem14(1_000_000),
        52: Problem52(),
        53: Problem53(max_n=100, limit=1_000_000),
        81: Problem81(filename="text_files/problem81.txt"),
        82: Problem82(filename="text_files/problem82.txt"),
        83: Problem83(filename="text_files/problem83.txt"),
        97: Problem97(7_830_457, 28_433, 10),
        206: Problem206()
    }
    return project_euler_dictionary[problem_number]


class Problem6:
    """
    https://projecteuler.net/problem=6


    The sum of the squares of the first ten natural numbers is:
    1^{2} + 2^{2} + ... + 10^{2} = 385

    The square of the sum of the first ten natural numbers is:
    (1 + 2 + ... + 10)^{2} = 55^{2} = 3025

    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum
    is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum.
    """

    def __init__(self, bound):
        """
        :param bound: 100
        """
        self.bound = bound
        self.answer = None

    @staticmethod
    def get_answer(bound):
        """

        :param bound:
        :return:
        """
        sum_of_squares, square_of_sums = 0, 0
        for i in range(1, bound + 1):
            sum_of_squares += i ** 2
            square_of_sums += i
        return (square_of_sums ** 2) - sum_of_squares

    def run(self):
        """
        :return: 25_164_150
        """
        self.answer = self.get_answer(self.bound)
        return self.answer


class Problem7:
    """
    https://projecteuler.net/problem=7


    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    """

    def __init__(self, nth):
        """
        :param nth: 10_001
        """
        self.nth = nth
        self.answer = None

    @staticmethod
    def get_answer(nth):
        """

        :param nth:
        :return:
        """
        primes = [2]
        if nth > 1:
            primes.append(3)
        if nth > 3:

            count, i = 2, 5
            while count < nth:

                prime, j = True, 0
                while prime and j < count and primes[j] <= sqrt(i) + 1:
                    if i % primes[j] == 0:
                        prime = False
                    j += 1
                if prime:
                    primes.append(i)
                    count += 1
                if count == nth:
                    return primes[nth - 1]

                prime, j = True, 0
                while prime and j < count and primes[j] <= sqrt(i + 2) + 1:
                    if (i + 2) % primes[j] == 0:
                        prime = False
                    j += 1
                if prime:
                    primes.append(i + 2)
                    count += 1
                i += 6

        return primes[nth - 1]

    def run(self):
        """
        :return: 104_743
        """
        self.answer = self.get_answer(self.nth)
        return self.answer


class Problem8:
    """
    https://projecteuler.net/problem=8


    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
    What is the value of this product?
    """

    def __init__(self, filename, length):
        """
        :param filename: "text_files/problem8.txt"
        :param length: 13
        """
        self.filename = filename
        self.length = length
        self.answer = None

    @staticmethod
    def get_answer(filename, length):
        """

        :param filename:
        :param length:
        :return:
        """
        max_multiplied = 0

        f = open(filename, "r")
        string = f.read().replace('\n', '')
        f.close()
        digits = [int(x) for x in string]
        size = len(digits)

        for i in range(length - 1, size):
            multiplied = 1
            for x in range(i - length, i):
                multiplied *= digits[x]
            if multiplied > max_multiplied:
                max_multiplied = multiplied
        return max_multiplied

    def run(self):
        """
        :return: 23_514_624_000
        """
        self.answer = self.get_answer(self.filename, self.length)
        return self.answer


class Problem9:
    """
    https://projecteuler.net/problem=9


    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:

    a^{2}+ b^{2} = c^{2}

    For example, 3^{2} + 4^{2} = 9 + 16 = 25 = 5^{2}.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    def __init__(self, summation):
        """
        :param summation: 1_000
        """
        self.summation = summation
        self.answer = None

    @staticmethod
    def get_answer(summation):
        """

        :param summation:
        :return:
        """
        for a in range(2, summation):
            for b in range(1, a):
                c_squared = a * a + b * b
                c = int(sqrt(c_squared))
                if c * c == c_squared:
                    if a + b + c == summation:
                        return a * b * c
        return None

    def run(self):
        """
        :return: 31_875_000
        """
        self.answer = self.get_answer(self.summation)
        return self.answer


class Problem10:
    """
    https://projecteuler.net/problem=10


    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """

    def __init__(self, limit):
        """
        :param limit: 2_000_000
        """
        self.limit = limit
        self.answer = None

    @staticmethod
    def get_answer(limit):
        """

        :param limit:
        :return:
        """
        summation = 2  # To account for the number 2
        sieve = [True] * (limit // 2)  # Sieve indices i correspond to the number (i * 2) + 1
        sieve[0] = False  # 1 is not a prime number
        for i in range((int(sqrt(limit)) // 2) + 1):
            if sieve[i]:
                summation += (i * 2) + 1
                for j in range((i * 3) + 1, limit // 2, (i * 2) + 1):
                    sieve[j] = False
        for i in range((int(sqrt(limit)) // 2) + 1, len(sieve)):
            if sieve[i]:
                summation += (i * 2) + 1
        return summation

    def run(self):
        """
        :return: 142_913_828_922
        """
        self.answer = self.get_answer(self.limit)
        return self.answer


class Problem11:
    """
    https://projecteuler.net/problem=11


    In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

    What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20×20 grid?
    """

    def __init__(self, filename, length):
        self.filename = filename
        self.length = length
        self.answer = None

    @staticmethod
    def get_answer(filename, length):
        greatest_product = 1

        f = open(filename, "r")
        strings = f.readlines()
        f.close()
        array = []
        for x in range(0, len(strings)):
            array.append(list(map(int, strings[x].split())))

        # Assume that array is a square matrix
        size = len(array)

        for x in range(0, size):
            for y in range(0, size):

                # check down row
                if x + length < size:
                    product = 1
                    for z in range(0, length):
                        product *= array[x + z][y]
                    if product > greatest_product:
                        greatest_product = product

                # check right row
                if y + length < size:
                    product = 1
                    for z in range(0, length):
                        product *= array[x][y + z]
                    if product > greatest_product:
                        greatest_product = product

                # check down-right diagonal
                if x + length < size and y + length < size:
                    product = 1
                    for z in range(0, length):
                        product *= array[x + z][y + z]
                    if product > greatest_product:
                        greatest_product = product

                # check down-left diagonal
                if x + length < size and y - length + 1 >= 0:
                    product = 1
                    for z in range(0, length):
                        product *= array[x + z][y - z]
                    if product > greatest_product:
                        greatest_product = product

        return greatest_product

    def run(self):
        self.answer = self.get_answer(self.filename, self.length)
        return self.answer


class Problem12:
    """
    https://projecteuler.net/problem=12


    The sequence of triangle numbers is generated by adding the natural numbers.
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
    The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?
    """

    def __init__(self, divisor_count):
        """
        :param divisor_count: 500
        """
        self.divisor_count = divisor_count
        self.answer = None

    @staticmethod
    def number_of_divisors_prob_12(number, primes, num_divisors):
        """

        :param number:
        :param primes: A list of prime number up to number
        :param num_divisors:
        :return: The number of divisors that number has, including 1 and itself,
        """
        itr = iter(primes)
        divisor_count = 1
        size = len(num_divisors)
        while number > 1:
            next_prime = itr.__next__()
            if number < next_prime * next_prime:
                return divisor_count * 2
            if number < size:
                return divisor_count * num_divisors[number]
            count = 0
            while number % next_prime == 0:
                count += 1
                number //= next_prime
            if count != 0:
                divisor_count *= count + 1
        return divisor_count

    @staticmethod
    def get_answer(divisor_count):
        """

        :param divisor_count: 500
        :return:
        """
        primes = library.list_primes(1_000)
        num_divisors = [0]
        i = 1
        num_divisors.append(library.number_of_divisors(i, primes))
        while True:
            if divisor_count < num_divisors[i] * num_divisors[(i + 1) // 2]:
                return i * (i + 1) // 2
            i += 1
            num_divisors.append(library.number_of_divisors(i, primes))
            num_divisors.append(library.number_of_divisors(i + 1, primes))
            if divisor_count < num_divisors[i // 2] * num_divisors[i + 1]:
                return i * (i + 1) // 2
            i += 1

    def run(self):
        """
        :return: 76576500
        """
        self.answer = self.get_answer(self.divisor_count)
        return self.answer


class Problem13:
    """
    https://projecteuler.net/problem=13


    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    """

    def __init__(self, filename, number_of_digits):
        self.filename = filename
        self.number_of_digits = number_of_digits
        self.answer = None

    @staticmethod
    def get_answer(filename, number_of_digits):
        f = open(filename, "r")
        strings = f.readlines()
        f.close()
        summation = 0
        for x in range(len(strings)):
            summation += int(strings[x].replace('\n', ''))
        return int(str(summation)[:number_of_digits])

    def run(self):
        self.answer = self.get_answer(self.filename, self.number_of_digits)
        return self.answer


class Problem14:
    """
    https://projecteuler.net/problem=14


    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """

    def __init__(self, bound):
        self.bound = bound
        self.answer = None

    @staticmethod
    def get_answer(bound):
        max_count, longest = 0, 0
        i = 1
        sequence = [0] * bound
        sequence[0] = 1
        while i < bound:
            x, count = i, 0
            while True:
                if x < len(sequence) and sequence[x - 1] != 0:
                    count += sequence[x - 1]
                    sequence[i - 1] = count
                    break
                if x % 2 == 0:
                    x //= 2
                    count += 1
                else:
                    x = ((3 * x) + 1) // 2
                    count += 2
            if count > max_count:
                max_count = count
                longest = i
            i += 1
        return longest

    def run(self):
        self.answer = self.get_answer(self.bound)
        return self.answer


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
