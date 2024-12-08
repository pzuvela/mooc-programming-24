# Write your solution here
def correct(lst: list[int]) -> bool:
    lst = [el for el in lst if el != 0]
    return len(lst) == len(set(lst))


def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    filtered_flattened_sudoku_block = []
    for row in sudoku[row_no:row_no+3]:
        filtered_flattened_sudoku_block += [el for el in row[column_no:column_no+3]]
    return correct(filtered_flattened_sudoku_block)


def sudoku_grid_correct(sudoku: list) -> bool:
    
    for row in sudoku:
        row_correct = correct(row)
        if not row_correct:
            return False

    for col_idx in range(9):
        col_correct = correct([row[col_idx] for row in sudoku])
        if not col_correct:
            return False
    
    for row_no, column_no in (
        (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)
    ):
        block_correct_ = block_correct(sudoku, row_no, column_no)
        if not block_correct_:
            return False
    
    return True


if __name__ == "__main__":

    """
    Please write a function named sudoku_grid_correct(sudoku: list), which takes 
    a two-dimensional array representing a sudoku grid as its argument. 
    The function should use the functions from the three previous exercises to 
    determine whether the complete sudoku grid is filled in correctly. 
    Copy the functions from the exercises above into your Python code file for this exercise.

    The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. 
    If all contain each of the numbers 1 to 9 at most once, the function returns True. 
    If a single one is filled in incorrectly, the function returns False.

    The image of a sudoku grid above these exercises has the nine blocks within the grid 
    indicated with thicker borders. These are the blocks the function should check, 
    and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), 
    (6, 3) and (6, 6).
    """
    sudoku = [
        [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
        [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
        [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
        [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
        [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
        [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
        [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
        [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
        [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
    ]
    print(sudoku_grid_correct(sudoku))

    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
