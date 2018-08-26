# project_euler.solutions import * : all files are named in the form 'problem_', where _ is the problem number.
from project_euler.solutions import *
import time


def get_problem(problem_number):
    try:
        func = dictionary(problem_number)
        start_time = time.perf_counter()
        answer = func()
        runtime = time.perf_counter() - start_time
        print()
        print("The answer to Problem", problem_number, "is:", answer)
        print("Elapsed time:", runtime, "seconds")
    except KeyError:
        answer = None
        runtime = 0
    #except AttributeError:
        answer = None
        runtime = 0
    return answer, runtime


def dictionary(problem_number):
    project_euler_dictionary = {
        1: problem001.get_answer,
        2: problem002.get_answer,
        3: problem003.get_answer,
        4: problem004.get_answer,
        5: problem005.get_answer,
        6: problem006.get_answer,
        7: problem007.get_answer,
        8: problem008.get_answer,
        9: problem009.get_answer,
        10: problem010.get_answer,
        11: problem011.get_answer,
        12: problem012.get_answer,
        13: problem013.get_answer,
        14: problem014.get_answer,
        15: problem015.get_answer,
        16: problem016.get_answer,
        22: problem022.get_answer,
        41: problem041.get_answer,
        42: problem042.get_answer,
        43: problem043.get_answer,
        52: problem052.get_answer,
        53: problem053.get_answer,
        81: problem081.get_answer,
        82: problem082.get_answer,
        83: problem083.get_answer,
        92: problem092.get_answer,
        97: problem097.get_answer,
        206: problem206.get_answer,
        493: problem493.get_answer,
        500: problem500.get_answer
    }
    return project_euler_dictionary[problem_number]
