from project_euler.library import file_to_matrix


def get_answer(filename="text_files/problem018.txt"):
    triangle = file_to_matrix(filename, " ")
    for i in reversed(range(len(triangle) - 1)):
        for j in reversed(range(i + 1)):
            if triangle[i + 1][j + 1] > triangle[i + 1][j]:
                triangle[i][j] += triangle[i + 1][j + 1]
            else:
                triangle[i][j] += triangle[i + 1][j]
    return triangle[0][0]
