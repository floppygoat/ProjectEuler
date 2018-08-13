from project_euler.library import file_to_matrix


def get_answer(filename="text_files/problem081.txt"):
    matrix = file_to_matrix(filename, ",")
    # Assume square matrix
    size = len(matrix)

    # Bottom-most row and right-most column
    for x in reversed(range(size - 1)):
        matrix[x][size - 1] += matrix[x + 1][size - 1]
        matrix[size - 1][x] += matrix[size - 1][x + 1]
    # Bottom-left to top-right diagonals from bottom-right corner to middle
    for x in reversed(range(size - 1)):
        for i, j in zip(range(x, size - 1), range(size - 2, x - 1, -1)):
            if matrix[i + 1][j] <= matrix[i][j + 1]:
                matrix[i][j] += matrix[i + 1][j]
            else:
                matrix[i][j] += matrix[i][j + 1]
    # Bottom-left to top-right diagonals from middle to top-right corner
    for x in reversed(range(size - 2)):
        for i, j in zip(range(0, x + 1), range(x, -1, -1)):
            if matrix[i + 1][j] <= matrix[i][j + 1]:
                matrix[i][j] += matrix[i + 1][j]
            else:
                matrix[i][j] += matrix[i][j + 1]
    return matrix[0][0]
