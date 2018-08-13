from project_euler.library import n_choose_k


def get_answer(m=20, n=20):
    """
    Since you can only move right and down, you make m+n moves in your traversal, in which m moves must be downward.
    Thus with a total of m+n moves, you have m moves to move down (or n moves to move right),
    This means that there is (m+n)choose(m) routes (which equals (m+n)choose(n) routes).
    :return: The number of routes from the upper right corner to the bottom left corner of a m * n grid,
    moving only right and down
    """
    return n_choose_k(m + n, m)
