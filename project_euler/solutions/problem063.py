def get_answer():
    """
    Since the base must be an integer,
    just keep checking if length(x^n) = n for all 1 <= x < 10 until the equality appears no more.
    """
    count = 0
    n = 0
    check = True
    while check:
        n += 1
        check = False
        for x in range(1, 10):
            num = pow(x, n)
            length = len(str(num))
            if length == n:
                count += 1
                check = True
    return count
