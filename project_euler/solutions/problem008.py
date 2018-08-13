def get_answer(filename="text_files/problem008.txt", length=13):
    """
    No fancy Math, just simple for loops.
    :return: The maximum product of length adjacent digits in the number found in filename.
    """
    f = open(filename, "r")
    string = f.read().replace('\n', '')
    f.close()
    digits = [int(x) for x in string]
    size = len(digits)

    max_multiplied = 0

    for i in range(length - 1, size):
        multiplied = 1
        for x in range(i - length, i):
            multiplied *= digits[x]
        if multiplied > max_multiplied:
            max_multiplied = multiplied
    return max_multiplied
