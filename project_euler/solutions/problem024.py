from itertools import permutations


def get_answer(nth=1_000_000):
    """
    Using python's itertools.permutations, just iterate through it <nth - 1> times,
    then store and convert the nth iteration into a number.
    :return:
    """
    itr = permutations(range(10))
    for a in range(nth - 1):
        itr.__next__()
    p = itr.__next__()
    ans = 0
    for n in p:
        ans = ans * 10 + n
    return ans
