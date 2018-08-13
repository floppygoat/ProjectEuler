def get_answer(max_n=1000, limit=1_000_000):
    count = 0
    pascals_triangle = [[1]]
    for n in range(1, max_n + 1):
        next_row = [1]
        c = 1
        for k in range(n):
            try:
                val = pascals_triangle[n - 1][k] + pascals_triangle[n - 1][k + 1]
            except IndexError:
                val = 1
            if val > limit:
                count += (n + 1) - 2 * c
                next_row.append(val)
                break
            else:
                c += 1
                next_row.append(val)
        pascals_triangle.append(next_row)
    return count
