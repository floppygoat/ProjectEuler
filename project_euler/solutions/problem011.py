from project_euler.library import file_to_matrix


def get_answer(filename="text_files/problem011.txt", length=4):
    """
    This is a brute-force solution.  It checks every possible sequence of adjacent numbers once and only once.
    :return: The greatest product of length adjacent numbers in the matrix found in file filename.
    """
    array = file_to_matrix(filename, " ")

    # Assume that array is a square matrix
    size = len(array)
    greatest_product = 0

    for x in range(0, size):
        for y in range(0, size):

            # check down row
            if x + length < size:
                product = 1
                for z in range(0, length):
                    product *= array[x + z][y]
                if product > greatest_product:
                    greatest_product = product

            # check right row
            if y + length < size:
                product = 1
                for z in range(0, length):
                    product *= array[x][y + z]
                if product > greatest_product:
                    greatest_product = product

            # check down-right diagonal
            if x + length < size and y + length < size:
                product = 1
                for z in range(0, length):
                    product *= array[x + z][y + z]
                if product > greatest_product:
                    greatest_product = product

            # check down-left diagonal
            if x + length < size and y - length + 1 >= 0:
                product = 1
                for z in range(0, length):
                    product *= array[x + z][y - z]
                if product > greatest_product:
                    greatest_product = product

    return greatest_product
