def get_answer(bound=1_000_000):
    """
    :return: The number with the longest Collatz sequence less than bound
    """
    max_count, longest = 0, 0
    sequence = [0] * bound
    sequence[0] = 1

    # The longest sequence must be greater than bound // 2.  Therefore no point looking at values less than bound // 2
    for i in range(bound // 2, bound):
        x, count = i, 0
        seq = []
        while True:
            # If we have calculated the value before:
            if x < bound and sequence[x - 1] != 0:

                # If the starting value has already been calculated, there must be a longer sequence less than x
                # (as i -> 1 is a sub-sequence of x < i Collatz sequence).
                if i == x:
                    break

                # Update sequence list
                c = sequence[x - 1]
                for y in reversed(seq):
                    if y % 2 == 0:
                        c += 1
                    else:
                        c += 2
                    if y < bound:
                        sequence[y - 1] = c
                count += sequence[x - 1]

                # If longest sequence: update longest and max_count
                if count > max_count:
                    max_count = count
                    longest = i

                sequence[i - 1] = count
                break

            # Else, remember the next value of this chain
            seq.append(x)
            if x % 2 == 0:
                x //= 2
                count += 1
            else:
                x = ((3 * x) + 1) // 2
                count += 2

    return longest
