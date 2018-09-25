def get_answer(limit=100):
    max_digit_sum = 0
    for a in range(limit):
        for b in range(limit):
            exp = pow(a, b)
            digit_sum = 0
            while exp != 0:
                digit_sum += exp % 10
                exp //= 10
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
    return max_digit_sum
