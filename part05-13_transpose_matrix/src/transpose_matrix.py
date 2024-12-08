# Write your solution here
def transpose(matrix: list):
    """
    The function should transpose the matrix. 
    Transposing means essentially flipping the matrix over its diagonal: columns become rows, 
    and rows become columns.
    """

    """
    transposed_matrix = [[] for _ in range(len(matrix))]

    for row in matrix:
        for col_idx, el in enumerate(row):
            transposed_matrix[col_idx].append(el)

    for row_idx, row in enumerate(transposed_matrix):
        matrix[row_idx] = row
    
    """

    transposed_matrix = [list(row) for row in zip(*matrix)]
    for row_idx, row in enumerate(transposed_matrix):
        matrix[row_idx] = row


def print_matrix(matrix: list[list[int]]):
    for row in matrix:
        print(" ".join([f"{el}" for el in row]))


if __name__ == "__main__":

    matrix_: list[list[int]] = [
        [1, 1],
        [2, 2],
    ]
    print("Matrix: ")
    print_matrix(matrix_)
    transpose(matrix_)
    print("Transposed Matrix: ")
    print_matrix(matrix_)
