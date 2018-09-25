def get_answer(spiral_size=1_001):
    # i is the current number in the spiral
    i = 1
    summation = 1
    current_spiral_size = 2
    while current_spiral_size < spiral_size:
        # We do the following loop 4 times to hit each corner in our spiral size.
        for count in range(4):
            i += current_spiral_size
            summation += i
        current_spiral_size += 2
    return summation
