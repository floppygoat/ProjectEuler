from math import sqrt


def get_answer():
    """
    It is mainly a brute force method, though one optimization was recognizing that the first underscore
    in the number 1_2_3_4_5_6_7_8_9_0 must be 0 (its square root must be a multiple of 10, which means
    its square must be a multiple of 100).  This reduces the search density by a factor of 10.
    :return: The unique number whose square is of the form 1_2_3_4_5_6_7_8_9_0.
    """
    for i in range(int(sqrt(1_92_93_94_95_96_97_98_99_90 // 100)),
                   int(sqrt(1_02_03_04_05_06_07_08_09_00 // 100)),
                   -1):
        if check((i * i)):
            return i * 10


def check(number):
    for digit in range(9, 0, -1):
        if number % 10 != digit:
            return False
        number //= 100
    return True
