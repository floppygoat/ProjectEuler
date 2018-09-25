def get_answer(limit=10_000, iterations=50):
    count = 0
    for num in range(limit):
        try:
            rev = reverse(num)
            for itr in range(iterations):
                num += rev
                rev = reverse(num)
                if rev == num:
                    raise StopIteration
            count += 1
        except StopIteration:
            continue
    return count


def reverse(number):
    rev = 0
    temp = number

    # Reverse the number
    while temp > 0:
        rev = (rev * 10) + (temp % 10)
        temp //= 10
    return rev
