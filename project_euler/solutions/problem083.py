from math import inf
from project_euler.library import file_to_matrix


def get_answer(filename="text_files/problem083.txt"):
    matrix = file_to_matrix(filename, ",")
    # Assume square matrix
    size = len(matrix)

    distance = [[inf] * size for x in range(size)]

    # Bellman-Ford algorithm with early exit
    distance[size - 1][size - 1] = matrix[size - 1][size - 1]
    finished = False
    while not finished:
        finished = True
        for h in reversed(range(size)):
            for w in reversed(range(size)):

                def get_distance(x, y):
                    if x < 0 or y < 0:
                        return inf
                    else:
                        try:
                            return distance[y][x]
                        except IndexError:
                            return inf

                temp = matrix[h][w] + min(
                    get_distance(w - 1, h),
                    get_distance(w + 1, h),
                    get_distance(w, h - 1),
                    get_distance(w, h + 1))

                if temp < distance[h][w]:
                    distance[h][w] = temp
                    finished = False
    return distance[0][0]
