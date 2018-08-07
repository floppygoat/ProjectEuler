def get_answer(limit=4_000_000):
    """
    Every third Fibonacci number is an even number.  2 and 8 are the first two even Fibonacci numbers.
    If we do not want to check if a Fibonacci number is even, we can instead find a way to to get the next
    even Fibonacci number directly.
    As F(n) = F(n - 1) + F(n - 2), it can be shown that F(n) = 4 * F(n - 3) + F(n - 6).

    :return:  Returns the sum of all even Fibonacci numbers less than limit
    """
    a, b = 8, 2
    summation = a + b
    while a <= limit:
        summation += a
        a, b = 4 * a + b, a
    return summation
