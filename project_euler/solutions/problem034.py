def get_answer():
    digit_fact = [1, 1, 2, 6, 24, 120, 720, 5_040, 40_320, 362_880]
    summation = 0
    for i in range(3, 1_000_000):
        if i == digit_factorial(i, digit_fact):
            summation += i
    return summation


def digit_factorial(number, digit_fact):
    answer = 0
    while number > 0:
        digit, number = number % 10, number // 10
        answer += digit_fact[digit]
    return answer
