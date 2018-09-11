UPPER_CASE_CORRECTION = -64


def get_answer(filename="text_files/problem022.txt"):
    """
    :return: The name score (row * (sum of numerical letter values (i.e a = 1, z = 26))) of the <filename>.
    """
    summation = 0
    f = open(filename, "r")
    string = f.read().replace("\"", "").split(",")
    f.close()
    string.sort()
    for x in range(len(string)):
        for y in range(len(string[x])):
            summation += (x + 1) * (ord(string[x][y]) + UPPER_CASE_CORRECTION)
    return summation
