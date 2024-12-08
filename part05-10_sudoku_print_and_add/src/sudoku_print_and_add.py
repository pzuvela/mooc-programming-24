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

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number


if __name__ == "__main__":

    """
    In this exercise we will complete two more functions for the sudoku project from the 
    previous section: print_sudoku and add_number.

    The function print_sudoku(sudoku: list) takes a two-dimensional array representing a 
    sudoku grid as its argument. The function should print out the grid in the format 
    specified in the examples below.

    The function add_number(sudoku: list, row_no: int, column_no: int, number: int) 
    takes a two-dimensional array representing a sudoku grid, 
    two integers referring to the row and column indexes of a single square, 
    and a single digit between 1 and 9, as its arguments. 
    The function should add the digit to the specified location in the grid.
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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)

    print("Test sudoku grid: ")

    s = [
        [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
        [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
        [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
        [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
        [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
        [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
        [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
        [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
        [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print_sudoku(s)
