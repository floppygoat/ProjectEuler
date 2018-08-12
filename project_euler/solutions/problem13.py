def get_answer(filename="text_files/problem13.txt", number_of_digits=10):
    """
    Due to Python's arbitrary precision, you can just explicitly add all rows of filename together
    :param filename:
    :param number_of_digits:
    :return:
    """
    f = open(filename, "r")
    strings = f.readlines()
    f.close()
    summation = 0
    for x in range(len(strings)):
        summation += int(strings[x])
    return int(str(summation)[:number_of_digits])
