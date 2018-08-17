def get_answer(filename="text_files/problem013.txt", number_of_digits=10):
    """
    Due to Python's arbitrary precision, you can just explicitly add all rows of filename together
    :return: The sum of all numbers (with each number on a newline) in file filename
    """
    f = open(filename, "r")
    strings = f.readlines()
    f.close()
    summation = 0
    for x in range(len(strings)):
        summation += int(strings[x])
    return int(str(summation)[:number_of_digits])
