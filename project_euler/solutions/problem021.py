def get_answer(limit=10_000):
    """
    Using an algorithm similar to the Sieve of Eratosthenes,
    sums all the divisor together for all numbers less than <limit>,
    before checking each number to see if the sum of their divisors equals each other.
    :return: sum of all amicable numbers below <limit>
    """
    summation = 0
    sum_divisors = [1] * limit
    for i in range(2, limit // 2):
        for j in range(2 * i, limit, i):
            sum_divisors[j] += i
    for i in range(0, limit):
        try:
            if i == sum_divisors[sum_divisors[i]] and i != sum_divisors[i]:
                summation += i
        # If the sum of its divisors is greater than <limit>,
        # it is out of the array bounds and can't be an amicable number.
        except IndexError:
            pass
    return summation
