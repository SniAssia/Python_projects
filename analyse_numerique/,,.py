def transpose_matrix(matrix):
    # Get the dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create an empty matrix to store the transposed values
    transposed_matrix = [[0] * rows for _ in range(cols)]

    # Iterate through each element in the original matrix
    for i in range(rows):
        for j in range(cols):
            # Assign the value from the original matrix to the corresponding position in the transposed matrix
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


# Example usage
matrix = [[1, 2], [3, 4], [5, 6]]
transposed_matrix = transpose_matrix(matrix)
print("Original matrix:")
print(matrix)
print("\nTransposed matrix:")
print(transposed_matrix)