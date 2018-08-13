from project_euler.library import n_choose_k


def get_answer(colours=7, balls_per_colour=10, choose=20):
    """
    The probability that you will pick one colour is:
    1 - (((colours - 1) * balls_per_colour)choose(choose)/(colours * balls_per_colour)choose(choose).
    Thus the expected number of colours is colours * the probability of choosing one colour.
    :return: The expected number of distinct colours chosen from a pot of balls with colours colours
    and balls_per_colour balls per colour if you randomly choose choose from the pot.
    """
    total_balls = colours * balls_per_colour
    probability = 1 - (n_choose_k(total_balls - balls_per_colour, choose) / n_choose_k(total_balls, choose))
    return round(colours * probability, 9)
