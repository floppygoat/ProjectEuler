from project_euler.library import file_to_matrix


def get_answer(filename="text_files/problem082.txt"):
    """
    Moving from columns right to left, for each number,
    we find the minimum sum to move to the right row and then sum it up.
    The minimum number in the left-most row is the minimum sum path.
    :return: The min sum from the left column to the right column moving right, up, and down.
    """
    matrix = file_to_matrix(filename, ",")
    # Assume square matrix
    size = len(matrix)

    for length_index in range(size - 2, -1, -1):
        new_column = []
        for height_index in range(size):
            # min route so far is just to move left to the next number
            best_route_sum = matrix[height_index][length_index + 1]

            # keep moving up and to the left to see if there is a lesser path found.
            check_sum = 0
            for i in range(height_index - 1, -1, -1):
                check_sum += matrix[i][length_index]
                if check_sum + matrix[i][length_index + 1] < best_route_sum:
                    best_route_sum = check_sum + matrix[i][length_index + 1]

            # keep moving down and to the left to see if there is a lesser path found.
            check_sum = 0
            for i in range(height_index + 1, size):
                check_sum += matrix[i][length_index]
                if check_sum + matrix[i][length_index + 1] < best_route_sum:
                    best_route_sum = check_sum + matrix[i][length_index + 1]

            # put minimal route sum for each index in the column in the array
            new_column.append(best_route_sum)

        # Once new column is complete, replace the old column with the new column
        for height_index in range(size):
            matrix[height_index][length_index] += new_column[height_index]

    # Find the minimum path in the left-most column
    minimal_route_sum = matrix[0][0]
    for i in range(size):
        if matrix[i][0] < minimal_route_sum:
            minimal_route_sum = matrix[i][0]

    return minimal_route_sum
