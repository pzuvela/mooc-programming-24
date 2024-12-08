# Write your solution here
def print_sudoku(sudoku: list):
    for row_idx, row in enumerate(sudoku):
        if row_idx > 0 and row_idx % 3 == 0:
            print("")
        for block_idx in range(0, 10, 3):
            print(
                " ".join(
                    ["_" if el == 0 else f"{el}" for el in row[block_idx:block_idx+3]]
                ), 
                end="\n" if block_idx == 9 else "  "
            )

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    sudoku_ = [[col for col in row] for row in sudoku]
    sudoku_[row_no][column_no] = number
    return sudoku_


if __name__ == "__main__":

    """
    This is the very last sudoku task. This time we will create a slightly different version of 
    the function for adding new numbers to the grid.

    The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) 
    takes a two-dimensional array representing a sudoku grid, two integers referring 
    to the row and column indexes of a single square, and a single digit 
    between 1 and 9, as its arguments. The function should return a 
    copy of the original grid with the new digit added in the correct location. 
    The function should not change the original grid received as a parameter.

    The print_sudoku function from the previous exercise could be useful for testing, 
    and it is used in the example below:
    """

    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
