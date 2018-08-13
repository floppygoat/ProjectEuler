from math import sqrt


def get_answer():
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
