def get_answer_slt(bound=1_000_000):
    """
    :return: The number with the longest Collatz sequence less than bound
    """
    max_count, longest = 0, 0
    sequence = [0] * bound
    sequence[0] = 1
    for i in range(1, bound):
        x, count = i, 0
        while True:
            if x % 2 == 0:
                x //= 2
                count += 1
            else:
                x = ((3 * x) + 1) // 2
                count += 2
            if x < len(sequence) and sequence[x - 1] != 0:
                count += sequence[x - 1]
                sequence[i - 1] = count
                break
        if count > max_count:
            max_count = count
            longest = i
    return longest
