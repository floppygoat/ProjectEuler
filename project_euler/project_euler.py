# project_euler.solutions import * : all files are named in the form 'problem_', where _ is the problem num.
from project_euler.solutions import *
import time


def get_problem(problem_number):
    '''try:'''
    func = dictionary(problem_number)
    start_time = time.perf_counter()
    answer = func()
    runtime = time.perf_counter() - start_time
    print()
    print("The answer to Problem", problem_number, "is:", answer)
    print("Elapsed time:", runtime, "seconds")
    '''except KeyError:
        answer = None
        runtime = 0
        # print("error")
    except AttributeError:
        answer = None
        runtime = 0
        # print("error")'''
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
        17: problem017.get_answer,
        18: problem018.get_answer,
        19: problem019.get_answer,
        20: problem020.get_answer,
        21: problem021.get_answer,
        22: problem022.get_answer,
        23: problem023.get_answer,
        24: problem024.get_answer,
        25: problem025.get_answer,
        26: problem026.get_answer,
        27: problem027.get_answer,
        28: problem028.get_answer,
        29: problem029.get_answer,
        30: problem030.get_answer,
        31: problem031.get_answer,
        32: problem032.get_answer,
        33: problem033.get_answer,
        34: problem034.get_answer,
        35: problem035.get_answer,
        36: problem036.get_answer,
        37: problem037.get_answer,
        38: problem038.get_answer,
        39: problem039.get_answer,
        40: problem040.get_answer,
        41: problem041.get_answer,
        42: problem042.get_answer,
        43: problem043.get_answer,
        44: problem044.get_answer,
        45: problem045.get_answer,
        46: problem046.get_answer,
        47: problem047.get_answer,
        48: problem048.get_answer,
        49: problem049.get_answer,
        50: problem050.get_answer,
        51: problem051.get_answer,
        52: problem052.get_answer,
        53: problem053.get_answer,
        54: problem054.get_answer,
        55: problem055.get_answer,
        56: problem056.get_answer,
        57: problem057.get_answer,
        58: problem058.get_answer,
        63: problem063.get_answer,
        81: problem081.get_answer,
        82: problem082.get_answer,
        83: problem083.get_answer,
        92: problem092.get_answer,
        97: problem097.get_answer,
        206: problem206.get_answer,
        315: problem315.get_answer,
        449: problem449.get_answer,
        493: problem493.get_answer,
        500: problem500.get_answer,
    }
    return project_euler_dictionary[problem_number]
