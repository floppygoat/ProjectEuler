def get_answer(limit=28_124):
    """
    It first finds the sum of all its divisors (similar to problem 21).
    Afterwards, we build up a set up abundant numbers while checking
    if each number can be subtracted by an abundant number to obtain another
    abundant number.
    :return: The sum of all numbers that cannot be expressed as the sum of two non-abundant numbers.
    """
    limit = min(limit, 28_124)
    summation = 0
    sum_divisors = [0] * limit
    for i in range(1, limit // 2):
        for j in range(2 * i, limit, i):
            sum_divisors[j] += i
    abundant = set()
    for i in range(1, limit):
        if sum_divisors[i] > i:
            abundant.add(i)
        if not any((i - a in abundant) for a in abundant):
            summation += i
    return summation
