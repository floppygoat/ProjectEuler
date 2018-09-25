def get_answer(limit=1_000, number_of_digits=10):
    summation = 0
    for x in range(1, limit + 1):
        summation += x**x
    return int(str(summation)[(len(str(summation)) - number_of_digits):len(str(summation))])
