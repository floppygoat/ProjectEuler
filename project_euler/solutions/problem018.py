from project_euler.library import file_to_matrix


def get_answer(filename="text_files/problem018.txt"):
    """
    To find the maximal sum to the top of the triangle,
    we start at the second bottom row and add to it whichever adjacent number in the row below is greater.
    Continuing this algorithm, the top of the triangle will be the maximal sum.
    :return: The maximal sum from the top to the bottom of the triangle.
    """
    triangle = file_to_matrix(filename, " ")
    for i in reversed(range(len(triangle) - 1)):
        for j in reversed(range(i + 1)):
            if triangle[i + 1][j + 1] > triangle[i + 1][j]:
                triangle[i][j] += triangle[i + 1][j + 1]
            else:
                triangle[i][j] += triangle[i + 1][j]
    return triangle[0][0]
