def get_answer(number=600_851_475_143):
    """
    This algorithm continually divides number evenly by i until i > number.
    This ensures that it will divide all prime numbers less than its largest prime factor,
    leaving you with the the largest prime factor
    This algorithm works well if the largest prime factor of number is relatively small (<10_000_000).

    :return: The largest prime factor of number
    """
    i = 2
    while i < number:
        while number % i == 0:
            number //= i
        i += 1
    return number
