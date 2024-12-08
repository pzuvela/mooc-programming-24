# write your solution here
import os


def get_matrix() -> list[int]:
    with open(os.path.join(os.path.dirname(__file__), "matrix.txt"), "r") as f:
        matrix = [[int(el) for el in line.split(",")] for line in f]
    return matrix


def row_sums() -> list[int]:
    matrix = get_matrix()
    return [sum(row) for row in matrix]


def matrix_sum() -> int:
    matrix = get_matrix()
    return sum(row_sums())


def matrix_max() -> int:
    matrix = get_matrix()
    return max(max(row) for row in matrix)


if __name__ == "__main__":

    print(row_sums())
    print(matrix_sum())
    print(matrix_max())
