from project_euler.library import n_choose_k


def get_answer(m=20, n=20):
    return n_choose_k(m + n, m)

