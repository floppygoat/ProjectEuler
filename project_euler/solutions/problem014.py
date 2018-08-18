def get_answer(bound=1_000_000):
    """
    :return: The number with the longest Collatz sequence less than bound
    """
    max_count, longest = 0, 0
    sequence = [0] * bound
    sequence[0] = 1
    for i in range(bound // 2, bound):
        x, count = i, 0
        seq = []
        while True:
            if x < bound and sequence[x - 1] != 0:
                if i == x:
                    break
                c = sequence[x - 1]
                for y in reversed(seq):
                    if y % 2 == 0:
                        c += 1
                    else:
                        c += 2
                    if y < bound:
                        sequence[y - 1] = c
                count += sequence[x - 1]
                sequence[i - 1] = count
                break
            seq.append(x)
            if x % 2 == 0:
                x //= 2
                count += 1
            else:
                x = ((3 * x) + 1) // 2
                count += 2
        if count > max_count:
            max_count = count
            longest = i
    return longest
