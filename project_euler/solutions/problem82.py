from project_euler.library import file_to_matrix


def get_answer(filename="text_files/problem82.txt"):
    matrix = file_to_matrix(filename, ",")
    # Assume square matrix
    size = len(matrix)

    for length_index in range(size - 2, -1, -1):
        new_column = []
        for height_index in range(size):
            best_route_sum = matrix[height_index][length_index + 1]

            # check up
            check_sum = 0
            for i in range(height_index - 1, -1, -1):
                check_sum += matrix[i][length_index]
                if check_sum + matrix[i][length_index + 1] < best_route_sum:
                    best_route_sum = check_sum + matrix[i][length_index + 1]

            # check down
            check_sum = 0
            for i in range(height_index + 1, size):
                check_sum += matrix[i][length_index]
                if check_sum + matrix[i][length_index + 1] < best_route_sum:
                    best_route_sum = check_sum + matrix[i][length_index + 1]

            # put minimal route sum for each index in the column in the array
            new_column.append(best_route_sum)

        for height_index in range(size):
            matrix[height_index][length_index] += new_column[height_index]

    minimal_route_sum = matrix[0][0]
    for i in range(size):
        if matrix[i][0] < minimal_route_sum:
            minimal_route_sum = matrix[i][0]

    return minimal_route_sum
