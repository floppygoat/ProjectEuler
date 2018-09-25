def get_answer(bound=1_000_000):
    summation = 0
    for i in range(1, bound):
        if is_palindrome(i):
            if bin(i)[2:] == bin(i)[len(bin(i)) - 1: 1: -1]:
                summation += i
    return summation


def is_palindrome(number):
    palindrome, i = 0, number
    while i > 0:
        palindrome = (palindrome * 10) + (i % 10)
        i //= 10
    return number == palindrome
