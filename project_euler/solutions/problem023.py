import time


def get_answer(limit=28_124):
    start_time = time.perf_counter()
    limit = min(limit, 28_124)
    summation = 0
    sum_divisors = [0] * limit
    for i in range(1, limit // 2):
        for j in range(2 * i, limit, i):
            sum_divisors[j] += i
    abundant = [False] * limit
    for i in range(1, limit):
        if sum_divisors[i] > i:
            abundant[i] = True
    runtime = time.perf_counter() - start_time
    print("Elapsed time:", runtime, "seconds")
    for i in range(1, limit):
        check = False
        if i % 2 == 0:
            x, y = i // 2, i // 2
        else:
            x, y = i // 2, i // 2 + 1
        while not check and x > 0:
            if abundant[x] and abundant[y]:
                check = True
            x -= 1
            y += 1
        if not check:
            summation += i
    return summation
