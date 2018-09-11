UPPER_CASE_CORRECTION = -64


def get_answer(filename='text_files/problem042.txt'):
    """
    :return: The amount of words in <filename> whose alphabetical position sum is a triangle number.
    """
    count = 0
    f = open(filename, "r")
    words = f.read().replace("\"", "").split(",")
    f.close()
    triangle_numbers = [1]
    for word in words:
        summation = 0
        for character in word:
            summation += ord(character) + UPPER_CASE_CORRECTION

        # If the sum is less than the max triangle number found, see if some is a triangle number.
        if triangle_numbers[-1] >= summation:
            if triangle_numbers.__contains__(summation):
                count += 1
            continue
        # Else, find enough triangle numbers so we can evaluate if the word is a triangle number.
        n = len(triangle_numbers)
        triangle_number = triangle_numbers[-1]
        while triangle_number < summation:
            n += 1
            triangle_number = n * (n + 1) // 2
            triangle_numbers.append(triangle_number)
        if summation == triangle_number:
            count += 1
    return count
