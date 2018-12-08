from project_euler.library import digit_factorial


def get_answer():
    summation = 0
    for i in range(3, 1_000_000):
        if i == digit_factorial(i):
            summation += i
    return summation
