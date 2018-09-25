def get_answer(expansions=1_000):
    count = 0
    denominator = 1
    numerator = 0
    for i in range(expansions):
        next_denominator = numerator + 2 * denominator
        numerator = denominator
        denominator = next_denominator
        if len(str(numerator + denominator)) > len(str(denominator)):
            count += 1
    return count
